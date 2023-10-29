#!/usr/bin/bash

if command -v pip3 &> /dev/null
then
    pip3 install cursesplus
    exit 0
else
    #Attempt manual install
    if [ ! -d "src" ]; then
        echo "Please run this from the same directory as src"
        exit -1
    fi
    if [ ! -d "/usr/lib/python3/dist-packages" ]; then
        mkdir -p /usr/lib/python3/dist-packages
    fi
    cp -r src/* /usr/lib/python3/dist-packages
fi

echo "Installed successfully"
#Finished