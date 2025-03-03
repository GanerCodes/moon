#!/bin/bash
# used to build the stuff run the tests and smork the crack
set -e
cd "$(☾ --get-dir)"
pushd FontCompose
	☾ CONFIGURE.☾
	popd
pushd Extra/WebInterface
	./wasm_setup.sh
	popd
git add .
git commit -m Auto
git push
