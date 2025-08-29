import os

try:
    os.system(
        "nuitka --standalone --onefile --follow-imports --remove-output --windows-console-mode=disable --lto=yes --enable-plugin=tk-inter QR_Generator.py"
    )
except Exception as e:
    print(f"Error occurred while creating executable: {e}")
