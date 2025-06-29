# 🎰 Florida Lottery Digital Signage System

This project displays real-time Florida Lottery scratch-off tickets on a TV screen using a Raspberry Pi or smart display. It automatically scrapes ticket data and images from the official Florida Lottery site and displays them in a rotating fullscreen interface.

## 🔧 Features
- Automated scraping of scratch-off ticket numbers, names, and images
- Local CSV + image caching
- Flask API for ticket data
- Fullscreen rotating UI for digital signage

## 📁 Folder Structure
- `app/`: Scraper + API logic
- `ticket_images/`: Ticket images (auto-downloaded)
- `templates/`: Frontend UI for digital signage
- `data/`: Stored data (CSV or SQLite)
- `main.py`: App entry point

## 🚀 To Run

1. Clone repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run scraper: `python app/scraper.py`
4. Run app: `python main.py`
5. Open `http://localhost:5000/display` in fullscreen

## 🛑 Disclaimer

This project is for **personal/educational use only**. All data is scraped from [https://flalottery.com](https://flalottery.com), which holds the rights to its content.