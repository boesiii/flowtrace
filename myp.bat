@echo off
REM call "C:\OSGeo4W64\bin\o4w_env.bat"
REM call "C:\OSGeo4W64\bin\qt5_env.bat"
REM call "C:\OSGeo4W64\bin\py3_env.bat"

@echo on
call "C:\Python37\Scripts\pyrcc5" -o resources.py resources.qrc

pause