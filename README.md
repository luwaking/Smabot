# Web Trading Bot

Mobile-friendly web dashboard + Flask backend for automated trading.

## Features
- SMA crossover signal automatic
- Lot size & stop loss / take profit calculation
- Mobile-friendly dashboard
- Live logs of trades

## How to run

### Backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
