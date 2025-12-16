@echo off
REM Empacotar a GUI com PyInstaller
REM Requer: pip install pyinstaller
pyinstaller --onefile --noconsole --name calculadora_juros gui.py

echo Build finalizado. O executável estará em dist\calculadora_juros.exe
pause
