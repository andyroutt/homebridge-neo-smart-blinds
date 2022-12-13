#!/bin/bash

name="Window 2"
controller="[smart controller ip_address]"
id="[smart controller id]"
id1="[room id1]"
id2="[room id2]"
channel="[controller channel for window 2]"
command="sp"
position=${1}
hash=`head -200 /dev/urandom | cksum | cut -c 1-7`
url="http://${controller}:8838/neo/v1/transmit?command=${id1}.${id2}-${channel}-${command}&id=${id}&hash=${hash}"

curl -X GET "${url}"

echo $position