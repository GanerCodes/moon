#!/bin/bash -e
cd "$(dirname `realpath -s $0`)"

# b/c `zip` sometimes cares
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LC_CTYPE=UTF-8

ZF=`realpath ./wasm_stuff.zip`
export MOON_CACHEDIR="/tmp/cpy_wasm_cache"
export MOON_DISABLE_CUSTOM_ERRORS=1

rm -r "$ZF" "$MOON_CACHEDIR" || :
☾ load_caches.☾

cd /            ; zip "$ZF" -r /tmp/cpy_wasm_cache
                  cd -
cd `☾ --get-dir`; zip "$ZF" -r ☾.py Libraries Builtins           \
                       -x "Libraries/󰤱_Libraries/WebInterface/*" \
                       -x "Libraries/Glypher/*" -x "*/__pycache__/*"
                  cd -
[ $# -ge 1 ] && ☾ server.☾ || :