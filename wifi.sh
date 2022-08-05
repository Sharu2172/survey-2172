Path='/etc/NetworkManager/system-connections'
command="sudo grep 314e $Path/*"
echo "$($command | grep psk)"