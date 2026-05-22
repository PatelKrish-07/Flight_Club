Flight Price Tracker & Alert System
A Python-based automated flight search and alert system that monitors flight prices from Bengaluru (BLR) to multiple destinations listed in a Google Sheet. If a direct or indirect flight drops below the target budget ("Lowest Price") specified in the spreadsheet, the application updates the sheet and automatically broadcasts email notifications to all registered users.

The project leverages the SerpAPI (Google Flights Engine) to fetch real-time flight details and features an intelligent multi-stop fallback mechanism if direct flights are unavailable.

🚀 Features
Google Sheets Integration: Dynamically fetches destination queries and tracking parameters (IATA codes, current floor prices, and subscriber mailing lists) using a REST API.

Real-time Flight Search: Queries real-time information via SerpAPI, complete with specific handling for currencies, dates, and dynamic flight routes.

Intelligent Routing Fallback: Automatically searches for multi-stop (indirect) itineraries if no non-stop options are found within the target window.

Dynamic Price Floor Updating: Updates the destination spreadsheet instantly when a cheaper configuration is located.

Automated Email Broadcasts: Transmits clean, structured mail alerts specifying structural details (airline names, flight numbers, connections, and dates) using an smtplib mail routine.
