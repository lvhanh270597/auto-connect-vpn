GA=$1
USER="username"
PIN=yourpin
PASS="$PIN$GA"
printf "$USER\n$PASS" > auth.txt
openvpn --config client.ovpn
