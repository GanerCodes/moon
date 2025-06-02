#!/bin/bash -e
export PATH="/home/ganer/Programs/vscodium/vscode/build/node_modules/.bin:$PATH"
yes | vsce package
OUT="moon-0.0.1.vsix"
codium --uninstall-extension "$OUT" || :
codium   --install-extension "$OUT"