#!/bin/bash

#target.execute('DEBIAN_FRONTEND=noninteractive {}'.format(d), as_root=True)

sudo apt install -y linux-tools-common linux-tools-`uname -r`
sudo apt-get install -y sysbench
sudo apt install python3-pip
sudo pip3 install mdutils
