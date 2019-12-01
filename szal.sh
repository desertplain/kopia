#!/bin/sh
#echo "alla ma kitka"

ip address|grep enp0s3|grep -v mtu|awk '{print $2}'|cut -f1 -d/
