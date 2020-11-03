if [ "$EUID" -ne 0 ] then
  echo "[!] Please Run As Root"
  exit
fi

sudo apt update
pip3 install -r requirements.txt
