#!/bin/bash -e
{ cd "${0%/*}"

# Credit for the VS theme base: https://github.com/Amereyeu/Black-plus-plus-vscodium

☾ ./configure_ext.☾
yes | npx vsce package
code=$(command -v codium || command -v vscodium || command -v vscode)
$code --uninstall-extension "moon-0.0.1.vsix" || :
$code   --install-extension "moon-0.0.1.vsix"

exit $?; }