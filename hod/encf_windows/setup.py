from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\\Program Files\\Python35-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Program Files\\Python35-32\\tcl\\tk8.6'

executables = [Executable("encf.py")]
packages = ["encodings", "asyncio", "idna", "zlib", "glob", "smtplib", "webbrowser", "docx2txt", "PyPDF2", "cryptography",
            "cffi", "asn1crypto", "colorama", "pycparser", "six", "time", "win32api"]
options = {"build_exe" : {"packages" : packages,},}

setup(name="test",
      options=options,
      version="0.1",
      description="this is a test",
      executables=executables)
