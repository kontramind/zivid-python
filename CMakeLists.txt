cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project(zivid LANGUAGES CXX)

# Download automatically, you can also just copy the conan.cmake file
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
   message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
   file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake"
                  "${CMAKE_BINARY_DIR}/conan.cmake")
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

message(INFO "CURRENT BIN DIR: ${CMAKE_BINARY_DIR}")

conan_cmake_run(REQUIRES eigen/3.3.7@conan/stable
                BASIC_SETUP)


# include("HunterGate.cmake")
# HunterGate(
#     URL "https://github.com/ruslo/hunter/archive/v0.10.9.tar.gz"
#     SHA1 "53b198e364dc7bc8360fc545f798563229bd7e20"
# )
# hunter_add_package(Eigen)


find_package(Eigen3 REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

OPTION(ZIVID_PYTHON_VERSION "Version number to be compiled into the module" "UNKNOWN")
OPTION(ZIVID_SDK_VERSION "Zivid SDK version to link with" 0.0.0)

if(MSVC)
    add_compile_options(/bigobj)
endif()

#message(FATAL_ERROR "cmake prefix path: ${CMAKE_PREFIX_PATH} \n eigen_oath: ${Eigen3_DIR}")

find_package(Zivid ${ZIVID_SDK_VERSION} EXACT COMPONENTS Core REQUIRED)
find_package(pybind11 2.2.4 REQUIRED)
#find_package(Eigen3 3.3 REQUIRED NO_MODULE)

add_subdirectory(src)
