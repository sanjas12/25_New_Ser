#0.0.0.1
import sys
from cx_Freeze import setup, Executable


file = "setup.py"

with open(file, 'r+', encoding='utf-8') as f:
    version = f.readline().split('.')
    version[-1] = str(int(version[-1]) + 1)
    version = '.'.join(version)
    f.seek(0)
    f.write(version)

# для включения конкретных файлов в build
# files = [("install.cmd")]


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest", "http",
                "PyQT5.QtopenGL4",
                "pydoc_data", "email",
                "concurent", "xml",
                # "asyncio", "curses", "distutils", "html", "multiprocessing",
                "sqlite3", "test", "urlib"],
    "optimize": 0,      # c 2 exe не запускается
    "zip_include_packages": ["PyQt5", "matplotlib"],
    # "include_files" : files
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="new_ser",
    version="0.0.1.0",
    description="My TG-Naladka",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", target_name="TG-Naladka",  base=base)],
)