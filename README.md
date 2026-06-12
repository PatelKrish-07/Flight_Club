# ✈️ Flight Club — Flight Deal Notifier

A Python automation tool that monitors flight prices from **any departure city** to your dream destinations and sends email alerts to subscribers whenever a cheaper deal is found. Destination data and subscriber emails are managed via a Google Sheet (through a REST API).

---

## ✨ Features

- **Automated price tracking** — Scans flight prices for all destinations stored in your Google Sheet
- **Smart fallback** — If no direct flights are found, automatically checks for indirect/connecting flights
- **Cheapest flight finder** — Parses Google Flights data (via SerpAPI) and picks the lowest price
- **Email notifications** — Sends deal alerts to all registered subscribers via Gmail SMTP
- **Price updates** — Automatically updates the lowest recorded price in your Google Sheet when a better deal is found
- **Multi-stop support** — Includes full airline and flight number details for connecting flights

---

## 🗂️ Project Structure

```
flight_club/
├── main.py                  # Entry point — orchestrates the full flow
├── flight_search.py         # Talks to SerpAPI (Google Flights engine)
├── flight_data.py           # Structures and finds the cheapest flight
├── data_manager.py          # Reads/writes destination & user data via REST API
├── notification_manager.py  # Sends email alerts via Gmail SMTP
├── .env                     # API keys and credentials (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```
main.py
  ├── DataManager       → Fetches destination list + subscriber emails from Google Sheet
  ├── FlightSearch      → Queries SerpAPI for flights from your chosen city to each destination
  ├── find_cheapest_flight → Picks the lowest priced flight from results
  ├── DataManager       → Updates Google Sheet if a new lowest price is found
  └── NotificationManager → Emails all subscribers with the deal details
```

1. Loads all destinations and their historical lowest prices from a Google Sheet
2. Searches Google Flights (via SerpAPI) for each destination for your specified travel dates
3. If no direct flights exist, falls back to indirect flights
4. If the found price beats the stored lowest price, it updates the sheet and fires email alerts to all subscribers

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [SerpAPI](https://serpapi.com/) account (free tier available)
- A Google Sheet set up with a REST API (e.g., via [Sheety](https://sheety.co/))
- A Gmail account with an [App Password](https://myaccount.google.com/apppasswords) enabled

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PatelKrish-07/Flight_Club.git
   cd Flight_Club
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file**

   Create a `.env` file in the project root:
   ```
   SHEET_ENDPOINT=https://api.sheety.co/your_sheet_endpoint/prices
   USERS_ENDPOINT=https://api.sheety.co/your_sheet_endpoint/users
   FLIGHT_ENDPOINT=https://serpapi.com/search
   SERPAPI_API_KEY=your_serpapi_key
   USER=your_sheety_username
   PASSWORD=your_sheety_password
   MY_EMAIL=your_gmail@gmail.com
   PASSS=your_gmail_app_password
   ```

4. **Set your travel dates and departure city in `main.py`**

   Update the travel dates to your preferred window:
   ```python
   from_day = datetime(2026, 7, 30).strftime("%Y-%m-%d")  # Your departure date
   till_day = datetime(2026, 8, 4).strftime("%Y-%m-%d")   # Your return date
   ```

   Update the departure airport IATA code to your city (currently set to Bangalore `"BLR"`):
   ```python
   flight = flight_search.check_flights("BLR", loc["iataCode"], from_day, till_day)
   ```
   Replace `"BLR"` with your own city's IATA code. For example:

   | City | IATA Code |
   |------|-----------|
   | Mumbai | `BOM` |
   | Delhi | `DEL` |
   | Chennai | `MAA` |
   | London | `LHR` |
   | New York | `JFK` |
   | Dubai | `DXB` |

   > 💡 Find any city's IATA code at [iata.org](https://www.iata.org/en/publications/directories/code-search/) or just Google `"<city name> IATA code"`.

5. **Run the script**
   ```bash
   python main.py
   ```

---

## 📊 Google Sheet Structure

Your sheet should have two tabs:

**Prices sheet** (destinations):
| id | city | iataCode | lowestPrice |
|----|------|----------|-------------|
| 1  | Paris | CDG | 45000 |
| 2  | Dubai | DXB | 18000 |

**Users sheet** (subscribers):
| whatIsYourEmail |
|-----------------|
| subscriber1@example.com |

---

## 🔒 Security Notes

- Never commit your `.env` file — it contains API keys and email credentials
- Use a **Gmail App Password**, not your actual Gmail password

---

## 📦 Dependencies

See [`requirements.txt`](requirements.txt) for the full list.

---

