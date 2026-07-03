@echo off
REM Video-to-Shorts Windows Batch File
echo ========================================
echo   Video-to-Shorts Uygulamasi
echo ========================================
echo.
echo Python paketleri yukleniyor...
python -m pip install -r requirements.txt
echo.
echo Uygulama baslatiliyor...
echo Tarayicida acin: http://localhost:5000
echo.
python app.py
pause