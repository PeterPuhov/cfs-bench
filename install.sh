#!/bin/bash

#target.execute('DEBIAN_FRONTEND=noninteractive {}'.format(d), as_root=True)
# tools/perf$ sudo make prefix=/usr install

sudo apt install -y linux-tools-common
sudo apt install -y linux-tools-`uname -r`
sudo apt-get install -y sysbench
sudo apt install -y python3-pip

sudo pip3 install mdutils
sudo pip3 install tabulate
sudo pip3 install cython
sudo pip3 install numpy


sudo apt-get install -y rt-tests

