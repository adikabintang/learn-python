from cffi import FFI
ffi = FFI()
ffi.cdef("""
    void help();
""")
C = ffi.dlopen("/home/bintang/github_personal/learn-python/23_cffi/libmylib.so")                     # loads the entire C namespace
#C.printf(b"hi there, %s.\n", arg)         # call printf
C.help()