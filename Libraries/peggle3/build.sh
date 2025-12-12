#!/bin/bash -e
name="peggle3"
ulimit -s unlimited

☾ noparen.☾ "$name" || :
gcc -O3 c-vector/vec.c "${name}.c" -Ic-vector -lpcre2-8 -Wno-implicit-int \
    -flto -fPIC -shared -o "lib${name}.so"
☾ TEST.☾

exit 0
emcc -O3 -fPIC -Wno-implicit-int \
    peggle3.c \
    c-vector/vec.c \
    wasm_build/libpcre2-8-wasm.a \
    -Ic-vector \
    -Iwasm_build \
    -Iwasm_build/src \
    -DPCRE2_CODE_UNIT_WIDTH=8 \
    -s MODULARIZE=1 \
    -s WASM_BIGINT=1 \
    -s EXPORT_ALL=1 \
    -o libpeggle3.wasm \
    -s SIDE_MODULE=1

# export LD_LIBRARY_PATH="$(realpath ./pcre2/local/lib)"
# DEBUG_FLAGS="-g -fsanitize=undefined -fsanitize-address-use-after-scope -fsanitize=address -fsanitize=bounds -fsanitize=leak -fno-omit-frame-pointer"
# gcc $NORMAL_FLAGS -fPIC -shared -Wl,-rpath,'/home/ganer/Projects/moon/Libraries/peggle3/pcre2/local/lib' -o "lib${name}.so"
# gcc $DEBUG_FLAGS -O3 c-vector/vec.c "${name}.c" -Ic-vector -Ipcre2/local/include \
#     pcre2/local/lib/libpcre2-8.a -Wno-implicit-int -fPIC -shared -o "lib${name}.so" \
# export ASAN_OPTIONS="detect_leaks=0"
# export LD_PRELOAD=$(gcc -print-file-name=libasan.so)
# NORMAL_FLAGS="-O3 c-vector/vec.c "${name}.c" -Ic-vector -Ipcre2/local/include -Lpcre2/local/lib -lpcre2-8 -Wno-implicit-int"
# DEBUG_FLAGS="$NORMAL_FLAGS -g -fsanitize=undefined -fsanitize-address-use-after-scope -fsanitize=address -fsanitize=bounds -fsanitize=leak -fno-omit-frame-pointer"
# sed '/^#include / s/^/#/' "${name}.c" | clang -E -P - > "${name}_expanded.c"
# gcc $DEBUG_FLAGS -o "${name}"
# time "./$name" || :
# rm "${name}"
# exit
# gcc $NORMAL_FLAGS -fPIC -shared -o "lib${name}.so"
# gcc $NORMAL_FLAGS -fPIC -shared -Wl,-rpath,'$ORIGIN/pcre2/local/lib' -o "lib${name}.so"
# export LD_PRELOAD=$(gcc -print-file-name=libasan.so)
# ☾ "${name}.☾"
# gcc $NORMAL_FLAGS -fPIC -shared \
#     -Wl,-rpath,'$ORIGIN/pcre2/local/lib' \
#     -Wl,-rpath-link,'pcre2/local/lib' \
#     -Wl,--disable-new-dtags \
#     -o "lib${name}.so"
