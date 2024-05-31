from cx_Freeze import setup, Executable

# Define the build options
build_exe_options = {
    "packages": [],  # Add any additional packages here
    "includes": [],  # Add any additional modules to include here
    "excludes": [],  # Add any modules to exclude here
    "include_files": []  # Add any additional files to include here
}

# Define the executable
executable = Executable(
    script="CycleCount_Updater.py",
    base=None,  # Set to "Win32GUI" for GUI applications on Windows
    icon="Style\engineering_EYb_icon.ico"
)

# Setup cx_Freeze
setup(
    name="CycleCount_Updater",
    version="0.1",
    description="Description of your application",
    options={"build_exe": build_exe_options},
    executables=[executable]
)
