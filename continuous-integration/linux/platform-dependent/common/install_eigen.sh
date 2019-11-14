#!/bin/bash

echo "Start $(basename "$0") script...." || exit $?

# Elevate permissions
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

# conan install eigen/3.3.7@conan/stable || exit $?
# 
# # conan profile new default --detect  || exit $? # Generates default profile detecting GCC and sets old ABI
# conan profile update settings.compiler.libcxx=libstdc++11 default  || exit $? # 
# 
# [ -x build ] || mkdir -p build
# cd build || exit $? # 
# conan install .. || exit $? # 
# cd .. || exit $?
# conan create . conan/stable || exit $?


#mkdir build && cd build && conan install .. || exit $?




#SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#ROOT_DIR="$SCRIPT_DIR/../../../.."
#
#DEPS_DIR="$ROOT_DIR/zivid-python-dependencies"
#[ -x $DEPS_DIR ] || mkdir -p $DEPS_DIR
#
#
## Get STM32 firmware
#echo "Downloading and unpacking Eigen"
#wget --no-verbose http://bitbucket.org/eigen/eigen/get/3.3.7.zip || exit $?
#unzip -q -o 3.3.7.zip -d "$DEPS_DIR" || exit $?
#rm 3.3.7.zip || exit $?
#
#ORIGINAL_DIR="$PWD"
#
#echo "----------"
#ls "$DEPS_DIR"
#echo "----------"
#ls "$DEPS_DIR/eigen-eigen-323c052e1731" || exit $?
#
#cd "$DEPS_DIR/eigen-eigen-323c052e1731" || exit $?
#mkdir "build" || exit $?
#cd "build" || exit $?
#cmake "$DEPS_DIR/eigen-eigen-323c052e1731" || exit $?
#make install || exit $?
#
#cd "$ORIGINAL_DIR" || exit $?

# echo "hello1"
# git clone https://github.com/Microsoft/vcpkg.git || exit $?
# echo "hello2"
# cd vcpkg || exit $?
# echo "hello3"
# ./bootstrap-vcpkg.sh || exit $? ## got here
# echo "hello4"
# ./vcpkg integrate install || exit $? # got here
# echo "hello5"
# git --version || exit $?
# echo "hello5.5"
# ./vcpkg install eigen3 || exit $? # failed
# echo "hello6"
# cd - || exit $?
# echo "hello7"