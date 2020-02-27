cmake_minimum_required(VERSION 2.8.3)
project(logic_prog)


include_directories(include)

add_library(intervall src/intervall.cpp)

add_executable(main src/main.cpp)
target_link_libraries(main intervall)
