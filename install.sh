#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


sudo mkdir -p ~/.local/share/nautilus-python/extensions/
sudo cp $DIR/open-vscodium.py ~/.local/share/nautilus-python/extensions/open-vscodium.py
nautilus -q
