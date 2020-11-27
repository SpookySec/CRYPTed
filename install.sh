#!/bin/bash
if [ "$EUID" -ne 0 ]; then
  echo "[!] Please Run As Root"
  exit
fi

clear
echo "[*] INSTALLING NOW..."
sudo apt update

sudo apt-get install libssl-dev
sudo apt-get install python3 python3-pip
pip3 install -r requirements.txt

sudo git clone https://github.com/ripmeep/easycracker && cd easycracker

sudo bash install.sh

cd ../ && sudo rm -rf easycracker
clear
echo "[*] FINISHED INSTALLING!"