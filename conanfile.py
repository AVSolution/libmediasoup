from conans import ConanFile, MSBuild

class MediaStreamerConan(ConanFile):
    name = "LibMediaSoup"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    generators = "visual_studio"
    exports_sources = "include*","libs*"

    def package(self):
        if self.settings.build_type=="Debug":
            self.copy("*.hpp", dst="include/libmediasoup", src="include")
            self.copy("*.h", dst="include/libmediasoup", src="include")	
            self.copy("*.dll", dst="bin", src="libs/debug/sdptransfrom")
            self.copy("*.dll", dst="bin", src="libs/debug/mediasoupclient")
            self.copy("*.dll", dst="bin", src="libs/debug/webrtc-broadcaster")
            self.copy("*.pdb", dst="bin", src="libs/debug/sdptransfrom")
            self.copy("*.pdb", dst="bin", src="libs/debug/mediasoupclient")
            self.copy("*.pdb", dst="bin", src="libs/debug/webrtc-broadcaster")
            self.copy("*.lib", dst="lib", src="libs/debug/sdptransfrom")
            self.copy("*.lib", dst="lib", src="libs/debug/mediasoupclient")
            self.copy("*.lib", dst="lib", src="libs/debug/webrtc-broadcaster")
        if self.settings.build_type=="Release":            
            self.copy("*.hpp", dst="include/libmediasoup", src="include")
            self.copy("*.h", dst="include/libmediasoup", src="include")
            self.copy("*.dll", dst="bin", src="libs/release/sdptransfrom")
            self.copy("*.dll", dst="bin", src="libs/release/mediasoupclient")
            self.copy("*.dll", dst="bin", src="libs/release/webrtc-broadcaster")
            self.copy("*.pdb", dst="bin", src="libs/release/sdptransfrom")
            self.copy("*.pdb", dst="bin", src="libs/release/mediasoupclient")
            self.copy("*.pdb", dst="bin", src="libs/release/webrtc-broadcaster")
            self.copy("*.lib", dst="lib", src="libs/release/sdptransfrom")
            self.copy("*.lib", dst="lib", src="libs/release/mediasoupclient")
            self.copy("*.lib", dst="lib", src="libs/release/webrtc-broadcaster")

    def package_info(self):
        self.cpp_info.libs = ["LibMediaSoup"]
