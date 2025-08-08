#!/bin/bash -e
{
cd "$(dirname `realpath -s $0`)"

ZF=`realpath ./moon_wasm.zip`
export MOON_TMPDIR="/tmp"
export MOON_CACHEDIR="$MOON_TMPDIR/moon_wasm_cache"
export MOON_DISABLE_CUSTOM_ERRORS=1
export MOON_NO_FORK=1

rm -r /tmp/moon{,_wasm_cache} || :
mkdir -p /tmp/moon
cp "$ZF" /tmp/moon
cd /tmp/moon
unzip moon_wasm.zip
python
exit 0
}