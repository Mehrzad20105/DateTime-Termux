echo "Install DateTime - by @Mehrzad20105"

echo "Updating..."
apt update && apt upgrade
echo "Complete!"

echo "Installing lib.s..."
pip inatall arrow
echo ""
echo "Complete!"

echo ""
echo ""

echo "Copying files..."
mkdir $PREFIX/share/datetime
cp dt.py $PREFIX/share/datetime
ln -s $PREFIX/share/datetime/dt.py $PREFIX/bin/dt

echo "Install Complete!"
echo "Run DateTime by typing \"dt\""
