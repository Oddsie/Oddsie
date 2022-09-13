echo "Where is Oddsie located? (full directory)"
read location
cd ~
echo python3 oddsie.py $1 $2 > oddsie
echo alias oddsie="/home/$location/oddsie">>.bashrc
