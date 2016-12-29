'''''''''''''''''''''''''''''''''
@Author	: Vic P.
@Email  : vic4key@gmail.com
@Name   : Routines
'''''''''''''''''''''''''''''''''

# -*- coding: utf-8 -*-

import os, math, traceback, binascii, struct, array, ctypes

KB = 1000
MB = KB**2
GB = KB**3
TB = KB**4
PB = KB**5
EB = KB**6
ZB = KB**7
YB = KB**8

KiB = 1024
MiB = KiB**2
GiB = KiB**3
TiB = KiB**4
PiB = KiB**5
EiB = KiB**6
ZiB = KiB**7
YiB = KiB**8

def rf(file_name):
    r = ""
    f = open(file_name, "rb")
    r = f.read()
    f.close()
    return r

def wf(file_name, data):
    f = open(file_name, "wb")
    f.write(data)
    f.close()
    return

def ReadFile(FilePath): return rf(FilePath)
def WriteFile(FilePath, Data): wf(FilePath, Data)

LE = 0 # Little Endian
BE = 1 # Big Endian

def I2D(v):
    p = ctypes.pointer(ctypes.c_ulonglong(v))
    p = ctypes.cast(p, ctypes.POINTER(ctypes.c_double))
    return p.contents.value

def I2F(v):
    p = ctypes.pointer(ctypes.c_ulong(v))
    p = ctypes.cast(p, ctypes.POINTER(ctypes.c_float))
    return p.contents.value

def numberic_to_hex(N):
    r = ""
    l = [type(0), type(0L)]
    if type(N) in l:
        r = hex(N)[2:]
        if type(N) == type(0L): r = r[:-1]
    return r

def LE2BE(d):
    #a = binascii.unhexlify(numberic_to_hex(d))
    #b = array.array("h", a)  
    #b.byteswap()
    #c = struct.Struct("<Id")
    #print b
    return 0 #c.unpack_from(b)

def rx(d, z, n = 0):
    r = 0
    if z < 0:
        if n > 0: r = d & int("F"*n, 16)
    else: r = d & int("FF"*z, 16)
    return r

def ReadX(Value, Position): return rx(Value, Position)

rb = lambda d = 0: rx(d, 1)
rw = lambda d = 0: rx(d, 2)
rd = lambda d = 0: rx(d, 4)

ReadBYTE = lambda d = 0: rx(d, 1)
ReadWORD = lambda d = 0: rx(d, 2)
ReadDWORD = lambda d = 0: rx(d, 4)

'''
def rx(D, i, z = 1, e = LE):
    allow_types = [type(0), type(0L)]
    if type(D) in allow_types:
        d = hex(D)[2:]
        if type(D) == type(0L): d = d[:-1]
        print "'%s'" % d
        n = 0
        for j in range(0, z): n += (ord(d[i + j]) << 4*2*j) if e == LE else (ord(d[i + z - 1 - j]) << 4*2*j)
    else: n = 0
    return n

rb = lambda d, i = 0: rx(d, i, 1, LE)
rw = lambda d, i = 0, e = LE: rx(d, i, 2, e)
rd = lambda d, i = 0, e = LE: rx(d, i, 4, e)

def readex(d, i, z = 1, e = LE):
    return rx(d, i, z, e)

def read_byte(d, i = 0):
    return rb(d, i)

def read_word(d, i = 0):
    return rw(d, i)

def read_dword(d, i = 0):
    return rd(d, i)
'''

def ExtractFileDirectory(FilePath): return os.path.split(FilePath)[0]

def ExtractFileName(FilePath): return os.path.split(FilePath)[1]

def ExtractFileExtension(FilePath, IncludedDOT=True):
    s = os.path.splitext(FilePath)[1]
    if IncludedDOT == False: s = s[1:]
    return s

def LogException(obj):
    t, v, tb = obj
    
    file_name     = ExtractFileName(tb.tb_frame.f_code.co_filename)
    line_number   = tb.tb_lineno
    routine_name  = tb.tb_frame.f_code.co_name
    type_name     = t.__name__
    message_error = "Cancelled by user!" if t == KeyboardInterrupt else v

    IDLE_WIDTH = 80
    
    print("")
    print(" Exception Infomation ".center(IDLE_WIDTH, "*"))
    print("* File Name :", file_name)
    print("* Line      :", line_number)
    print("* Routine   :", routine_name)
    print("* Type      :", type_name)
    print("* Message   :", message_error)
    print("".center(IDLE_WIDTH, "*"))
    return

def InitBrowser(Headers=[], EnableDebugging=False, Robots=False, Redirect=True, Referer=True, Equiv=True):
    import mechanize
    import cookielib
    
    browser = mechanize.Browser()
    
    cookiejar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookiejar)

    browser.set_handle_robots(Robots)
    browser.set_handle_equiv(Equiv)
    browser.set_handle_referer(Referer)
    browser.set_handle_redirect(Redirect)
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    browser.addheaders = Headers

    if EnableDebugging == True:
        browser.set_debug_http(True)
        browser.set_debug_redirects(True)
        browser.set_debug_responses(True)
    pass
    
    return browser

def WriteLog(name="", text=""):
    f = open(name, "a+")
    f.write(text + "\n")
    f.close()
    return

def FormatBytes(N, u = 1024):
    s = ""
    e = 0
    l = ["B", "KiB", "MiB", "GiB", "TiB"]
    if N > 0: e = int(math.log(N, u))
    s = "%0.2f %s" % (float(N) / u**e, l[e])
    return s
