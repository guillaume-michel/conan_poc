cmake_minimum_required(VERSION 3.25)
project(test1 CXX)

find_package(Protobuf REQUIRED)
find_package(Boost REQUIRED)

add_executable(test1
  proto/animal.proto
  src/test1.cpp
)

protobuf_generate(TARGET test1
PROTOS proto/animal.proto)

target_link_libraries(test1
  protobuf::libprotobuf
  Boost::program_options
)

target_include_directories(test1 PUBLIC
  ${CMAKE_CURRENT_BINARY_DIR}
)
