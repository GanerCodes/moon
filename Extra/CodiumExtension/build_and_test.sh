#!/bin/bash -e

# base VS theme: https://github.com/Amereyeu/Black-plus-plus-vscodium

cd "${0%/*}"
export PATH="$HOME/Programs/vscodium/vscode/build/node_modules/.bin:$PATH"
☾ ./configure_ext.☾
yes | vsce package
OUT="moon-0.0.1.vsix"
codium --uninstall-extension "$OUT" || :
codium   --install-extension "$OUT"
