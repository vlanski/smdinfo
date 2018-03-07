@echo off
@pip install pyinstaller
@mkdir build
@copy smdinfo.py build
@cd build
@pyinstaller -F -w --icon=..\tree.ico smdinfo.py
@cd ..
@copy build\dist\smdinfo.exe smdinfo.exe
@rmdir /Q /S build
@pause