#!/bin/bash -e
{
# clear

# ls -l BOOTSTRAP_Δ.py

# python BOOTSTRAP_Δ.py b
# ls -l /tmp/Δ_bootstrap.py

# python /tmp/Δ_bootstrap.py b /home/ganer/Projects/Moon_BETA/STAGES/BOOTSTRAP_ε.py
# python BOOTSTRAP_ε.py aR '⨡ text_format ; padc(‹egg›,25,␛─)☾'
# python BOOTSTRAP_ε.py aR '⨡ text_format ⭸ *'

# python BOOTSTRAP_ζ.py aR '⨡ text_format ⭸ x=dotrim'
# python BOOTSTRAP_ζ.py ar '1☾'
# python BOOTSTRAP_ε.py b BOOTSTRAP_ζ.py
# python BOOTSTRAP_ζ.py b BOOTSTRAP_η.py

python BOOTSTRAP_η.py b BOOTSTRAP_θ.py
echo "Generated θ"
python BOOTSTRAP_θ.py b BOOTSTRAP_ι.py
echo "Generated ι"
python BOOTSTRAP_ι.py r 1☾

exit

}