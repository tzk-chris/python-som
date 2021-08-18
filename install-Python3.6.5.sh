#!/bin/bash

# 安装python3.65
yum groupinstall 'Development Tools' -y
yum install -y sqlite-devel ncurses-devel ncurses-libs zlib-devel mysql-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel openssl-devel
wget wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar -zxvf Python-3.6.5.tgz
cd Python-3.6.5
./configure --prefix=/usr/local/python3.6  --enable-shared
make  && make install
ln -s /usr/local/python3.6/bin/python3 /usr/bin/python3
cp /usr/local/python3.6/lib/libpython3.6m.so.1.0 /usr/local/lib64
cp /usr/local/python3.6/lib/libpython3.6m.so.1.0 /usr/lib64
ln -s /usr/local/python3.6/bin/pip3 /usr/bin/pip3

# 虚拟环境管理
/usr/bin/pip3 install virtualenv
ln /usr/local/python3.6/bin/virtualenv /usr/bin/virtualenv

# 虚拟环境管理器安装
/usr/bin/pip3 install virtualenvwrapper
cat>>~/.bashrc<<EOF
# 设置python环境管理的变量
if [ -f /usr/local/python3.6/bin/virtualenvwrapper.sh ]; then
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/local/python3.6/bin/python3
    source /usr/local/python3.6/bin/virtualenvwrapper.sh
fi
EOF
source ~/.bashrc
