#!/bin/bash -e
export PATH="/home/ganer/Programs/vscodium/vscode/build/node_modules/.bin:$PATH"
yes | vsce package
OUT="moonverter-0.0.1.vsix"
codium --uninstall-extension "$OUT" || :
codium   --install-extension "$OUT"
# "`npm root -g`/vsce/vsce" package
# `command -v codium || echo "vscode"` --install-extension "`ls *.vsix | tail -n1`"