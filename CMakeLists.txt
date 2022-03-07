#####################################################

cmake_minimum_required(VERSION 3.22 FATAL_ERROR)

project(smart_clock LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS NO)

include_directories(${CMAKE_SOURCE_DIR}/include)


#####################################################


add_executable(clock ${CMAKE_SOURCE_DIR}/src/main.cpp)


add_library(lcd
	STATIC
		${CMAKE_SOURCE_DIR}/src/lcd/lcd.cpp
		${CMAKE_SOURCE_DIR}/src/lcd/st7565r.cpp
)


target_link_libraries(lcd
		-static -lbcm2835
)

target_link_libraries(clock
		lcd
)

