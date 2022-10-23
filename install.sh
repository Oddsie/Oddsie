# INSTALL
cp oddsie.py ~
cd ~
chmod +x oddsie.py
echo 'function oddsie () {' >> .bashrc
echo './oddsie.py $1 $2' >> .bashrc
echo '}' >> .bashrc
echo 'export -f oddsie' >> .bashrc
