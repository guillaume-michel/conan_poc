* Notes
-------
cross compiling with Ninja Multi-Config
```
mkdir build && \
cd build && \
conan install .. -pr:b=../profiles/mypc -pr:h=../profiles/raspberry -g cmake_multi -s build_type=Release --build=missing && \
conan install .. -pr:b=../profiles/mypc -pr:h=../profiles/raspberry -g cmake_multi -s build_type=Debug --build=missing && \
conan install .. -pr:b=../profiles/mypc -pr:h=../profiles/raspberry -g cmake_multi -s build_type=RelWithDebInfo --build=missing && \
source generators/conanbuildenv-release-armv7hf.sh && \
cmake -DCMAKE_TOOLCHAIN_FILE=generators/conan_toolchain.cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -G "Ninja Multi-Config" .. && \
cmake --build . --config Release && \
cmake --build . --config Debug && \
cmake --build . --config RelWithDebInfo && \
source generators/deactivate_conanbuild.sh
```
