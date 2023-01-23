#! /usr/bin/sh

if ! command -v pip3 &> /dev/null
then
    echo "Please install python3-pip from your package manager."
    exit -1
fi
pip3 install cursesplus
#Finished