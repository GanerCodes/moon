#!/bin/bash -e
{
cd "$(dirname `realpath -s $0`)"

# b/c `zip` sometimes cares
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LC_CTYPE=UTF-8

ZF=`realpath ./moon_wasm.zip`
export MOON_TMPDIR="/tmp"
export MOON_CACHEDIR="$MOON_TMPDIR/moon_wasm_cache"
export MOON_DISABLE_CUSTOM_ERRORS=1

rm -r "$ZF" "$MOON_CACHEDIR" || :
☾ load_caches.☾

pushd "$MOON_TMPDIR"; zip "$ZF" -r `basename "$MOON_CACHEDIR"`
                      popd
pushd `☾ --get-dir`; zip "$ZF" -r Libraries Builtins         \
                               -x "Libraries/WebInterface/*" \
                               -x "Libraries/Glypher/*"
                     cp moon.py "$MOON_CACHEDIR/moon.py"
                     pushd "$MOON_CACHEDIR"; zip "$ZF" moon.py
                                             popd
                     popd
[ $# -ge 1 ] && ☾ server.☾ || :
exit 0
}
# rm -r /tmp/moon{,moon_wasm_cache} ; mkdir -p /tmp/moon ; cp ~/Projects/moon/Libraries/WebInterface/moon_wasm.zip /tmp/moon ; cd /tmp/moon ; unzip moon_wasm.zip ; mv moon_wasm_cache /tmp/moon_wasm_cache ; { export MOON_TMPDIR="/tmp"; export MOON_CACHEDIR="/tmp/moon_wasm_cache"; export MOON_NO_FORK="1"; export MOON_DISABLE_CUSTOM_ERRORS="1"; export MOON_LOG_IMPORTS="1"; python; }
