import os.path

from conan import ConanFile
from conan.tools.build import can_run
from conan.tools.layout import basic_layout



class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def layout(self):
        basic_layout(self, src_folder="src")

    def test(self):
        tools = ['7za', '7zr', '7z']
        for tool in tools:
            assert os.path.exists(os.path.join(self.dependencies[self.tested_reference_str].cpp_info.bindir, tool))
            if can_run(self):
                self.run(tool, env="conanrun")
