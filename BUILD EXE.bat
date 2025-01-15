uv sync
call .venv/Scripts/activate

pyinstaller --noconfirm --onefile --console --icon "assets\app_icon.ico" --clean  "main.py"

del main.spec
rmdir /s /q build 

move dist\main.exe PC_ON_NOTIFIER.exe

rmdir /s /q dist