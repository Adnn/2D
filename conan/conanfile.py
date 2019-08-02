from conans import ConanFile, CMake, tools


class TwodConan(ConanFile):
    name = "2d"
    version = "0.0.1"
    license = "The Unlicense"
    author = "adnn"
    url = "https://github.com/Adnn/2D"
    description = "2D graphics with OpenGL"
    topics = ("opengl", "2D")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake_paths"

    requires = [
        ("glad/0.1.29@bincrafters/stable"),
        ("glfw/3.3@bincrafters/stable"),
    ]