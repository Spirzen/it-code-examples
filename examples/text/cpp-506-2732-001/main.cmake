cmake_minimum_required(VERSION 3.20)
project(qt_quick_hello LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)

find_package(Qt6 REQUIRED COMPONENTS Quick Qml)

qt_add_executable(quick_hello
    main.cpp
    counter.cpp
    counter.hpp
)

qt_add_qml_module(quick_hello
    URI HelloApp
    VERSION 1.0
    QML_FILES qml/Main.qml
)

target_link_libraries(quick_hello PRIVATE Qt6::Quick)
