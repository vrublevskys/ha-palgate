import ctypes
import os


class LibWrapper:
    def __init__(self):
        self.lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), './libnative-lib.so'))

    def get_token(self, arg1: bytearray, arg2: int, arg3: int, arg4: int):
        return self.lib.Java_com_bluegate_shared_FaceDetectNative_getFacialLandmarks(arg1, arg2, arg3, arg4)
