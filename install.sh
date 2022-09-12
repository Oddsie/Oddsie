echo "Where is oddsie located? (full directory)"
read location
cd location
echo python3 oddsie.py $1 $2 > oddsie
chmod +x oddsie
