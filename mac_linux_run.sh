#!/bin/bash
echo "========================================"
echo "  Video-to-Shorts Uygulamasi"
echo "========================================"
echo ""
echo "Python paketleri yukleniyor..."
python3 -m pip install -r requirements.txt
echo ""
echo "Uygulama baslatiliyor..."
echo "Tarayicida acin: http://localhost:5000"
echo ""
python3 app.py