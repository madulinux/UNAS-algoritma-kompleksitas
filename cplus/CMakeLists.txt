cmake_minimum_required(VERSION 3.10)

# Set the project name
project(SearchProgram)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the include directory for the JSON library
include_directories(include)

# Add the executable
add_executable(search_program main.cpp helper.cpp)