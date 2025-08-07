echo "los gehts..."
apt-get update
apt-get install -y git cmake make gcc libusb-1.0-0-dev gcc-arm-none-eabi
rm -rf stlink
git clone https://github.com/stlink-org/stlink.git
make -C stlink release
make -C stlink/build/Release install
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
echo "/usr/local/lib" | tee /etc/ld.so.conf.d/stlink.conf
ldconfig