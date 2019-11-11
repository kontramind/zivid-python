#!/bin/bash

echo "Start $(basename "$0") script...." || exit $?

# Elevate permissions
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

conan install eigen/3.3.7@conan/stable || exit $?
mkdir build && cd build && conan install .. || exit $?


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
