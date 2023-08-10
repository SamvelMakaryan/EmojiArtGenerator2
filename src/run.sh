#!/bin/bash

# Create a build directory if it doesn't exist
if [ ! -d "build" ]; then
    mkdir build
fi

cd build

cmake ..

make

cd ..

python3 main.py

