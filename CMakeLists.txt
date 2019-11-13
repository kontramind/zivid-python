cmake_minimum_required(VERSION 3.8 FATAL_ERROR)



include("HunterGate.cmake")
HunterGate(
    URL "https://github.com/ruslo/hunter/archive/v0.10.9.tar.gz"
    SHA1 "53b198e364dc7bc8360fc545f798563229bd7e20"
)
hunter_add_package(Eigen)

project(zivid LANGUAGES CXX)
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
