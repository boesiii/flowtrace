@echo off
call "C:\Program Files\QGIS 3.2\bin\o4w_env.bat"
call "C:\Program Files\QGIS 3.2\bin\qt5_env.bat"
call "C:\Program Files\QGIS 3.2\bin\py3_env.bat"

@echo on
"C:\Program Files\QGIS 3.2\apps\Python36\Scripts\pyrcc5" -o resources.py resources.qrc