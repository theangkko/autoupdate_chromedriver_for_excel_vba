# python setupcx.py build      for build exe
# autoupdate_chromedriver_for_excel_vba

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    'excludes':[
    	'tkinter','unittest'
    ],
    'packages': [
        'chromedriver_autoinstaller', 
        'json','logging','os','re','shutil','subprocess','sys','urllib','xml','zipfile','io','platform','typing'
    ]
}

# base="Win32GUI" should be used only for Windows GUI app
# base = "Win32GUI" if sys.platform == "win32" else None
base = None
 
setup(
    name='autoinupdate_chromedrive_vba',
    version='1.0',
    author='theangkko',
    icon="icon.ico",
    options = dict(build_exe = build_exe_options),
    executables=[Executable("main.py", base=base)],
)

