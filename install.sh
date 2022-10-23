# INSTALL
cp oddsie.py ~
cd ~
chmod +x oddsie.py
echo 'oddsie () {' >> .bashrc
echo './oddsie.py $1 $2' >> .bashrc
echo '}' >> .bashrc
