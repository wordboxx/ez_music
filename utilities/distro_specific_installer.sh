#!/bin/bash

echo "Getting Linux Distro... (Debian, Arch, etc.)"

# Getting Distribution information
DIST_INFO=$(cat /etc/os-release)

if [[ $DIST_INFO == *"Debian"* ]]; then
	echo "Debian detected!"
	sudo apt-get install -qq python3 python3-pip python3-venv 
fi