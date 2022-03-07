
# smart-clock
## description

A smart clock that uses a browser to change its settings, and some buttons to control it.

## How to compile
```
mkdir build && cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=../environment/rpi.toolchain.cmake
cmake --build .
```
The output is an ARM 32 bit executable named "clock". This should run directly on the Raspberry pi without the need of installing external libraries. 

**PROGRAM MUST HAVE ROOT PRIVILEGES (requirement for SPI)**