from conan import ConanFile
from conan.tools.cmake import cmake_layout

class Test1Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualBuildEnv"

    def requirements(self):
        self.requires("protobuf/3.21.9")
        self.requires("boost/1.77.0")


    def build_requirements(self):
        self.tool_requires("protobuf/3.21.9")

    def layout(self):
        cmake_layout(self)
