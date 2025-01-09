# setup.py

from cx_Freeze import setup, Executable
import sys

# Application parameters
app_name = "HEIC Converter"
app_version = "1.1"
app_description = "A tool to batch convert HEIC images to PNG or JPG format."

# Dependencies
build_exe_options = {
    "packages": [
        "os",
        "logging",
        "shutil",
        "concurrent.futures",
        "multiprocessing",
        "PIL",
        "pillow_heif",
        "converter",
        "PyQt5",
    ],
    "includes": [
        "converter",
    ],
    "excludes": [
        "PyQt5.QtQml",  # Exclude PyQt5.QtQml to prevent KeyError
    ],
    "include_files": [],
    "build_exe": "build_exe"
}

# Base setting for Windows GUI application
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Define the main executable
executables = [
    Executable(
        script="gui.py",
        base=base,
        target_name="HEICConverter.exe",
        icon=None
    )
]

setup(
    name=app_name,
    version=app_version,
    description=app_description,
    options={"build_exe": build_exe_options},
    executables=executables
)