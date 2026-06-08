cmake_minimum_required(VERSION 3.20)
project(calc_test LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)

add_library(calc src/calc.cpp)
target_include_directories(calc PUBLIC include)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()
add_executable(calc_tests tests/calc_test.cpp)
target_link_libraries(calc_tests PRIVATE calc GTest::gtest_main)
include(GoogleTest)
gtest_discover_tests(calc_tests)
