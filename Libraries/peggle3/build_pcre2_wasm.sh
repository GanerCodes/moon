#!/usr/bin/env bash
set -e

PCRE2_DIR="pcre2"
BUILD="wasm_build"
BUILDSRC="$BUILD/src"
rm -rf "$BUILD"
mkdir -p "$BUILDSRC"

echo "[1/4] Copying required PCRE2 sources"
cp "$PCRE2_DIR/src/"pcre2_*.h "$BUILDSRC"/
for f in "$PCRE2_DIR/src/"pcre2_*.c; do
    case "$(basename "$f")" in
        pcre2_dftables.c|pcre2_jit_test.c|pcre2test.c|pcre2grep.c|pcre2demo.c|pcre2posix_test.c)
            # Skip files containing main() or not suitable for WASM
            ;;
        pcre2_fuzzsupport.c|pcre2_jit_compile.c)
            # Skip JIT and fuzzing (not usable in wasm)
            ;;
        *)
            cp "$f" "$BUILDSRC/"
            ;;
    esac
done


echo "[2/4] Creating patched headers"

# sed -i '1s/^/#define PCRE2_CODE_UNIT_WIDTH 8\n/' "$BUILD/pcre2.h"

cat >> "$BUILD/config.h" <<EOF
#undef PCRE2_STATIC
#define PCRE2_STATIC 1
#undef LINK_SIZE
#define LINK_SIZE 4
#undef SUPPORT_UNICODE
#define SUPPORT_UNICODE 1
#undef PCRE2_CODE_UNIT_WIDTH
#define PCRE2_CODE_UNIT_WIDTH 8
#undef SUPPORT_PCRE2_8
#define SUPPORT_PCRE2_8
#undef SUPPORT_JIT

EOF
cat "$PCRE2_DIR/src/config.h.generic" >> "$BUILD/config.h"

# Patch pcre2.h.generic to include config.h FIRST
sed '1i #include "config.h"' "$PCRE2_DIR/src/pcre2.h.generic" > "$BUILD/pcre2.h"

echo "[3/4] Compiling PCRE2"

OBJFILES=""
for src in "$BUILDSRC"/*.c; do
    obj="${src%.c}.o"
    echo "  emcc -c $(basename "$src")"
    emcc -O3 -fPIC -c "$src" -I"$BUILD" -I"$BUILDSRC" \
         -DPCRE2_CODE_UNIT_WIDTH=8 -o "$obj"
    OBJFILES="$OBJFILES $obj"
done

echo "[4/4] Creating libpcre2-8-wasm.a"
emar rcs "$BUILD/libpcre2-8-wasm.a" $OBJFILES

echo "Done."
echo "Library: $BUILD/libpcre2-8-wasm.a"
echo "Headers: $BUILD/pcre2.h, $BUILD/config.h"