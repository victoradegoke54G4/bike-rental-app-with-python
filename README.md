# bike-rental-app-with-python
*A simple Python app that allows users to rent bikes with respect to time.*

## How It Works
- The user runs `main.py`.  
- A `Customer` instance is created (via `customer.py`), storing name, bikes rented, rental time, rental type.  
- The `BikeRental` class (in `bike_rental.py`) manages the shop’s stock, handles renting and returning, and uses `datetime` to determine the rental period.  
- All business logic (stock changes, rental time) is separated from user interaction—so the app is modular and clean.  
- You can extend it later to integrate a database if you want to save rental history permanently.

## Features
- Rent bikes by hourly, daily or weekly models  
- Track how long the bike was rented (via `datetime`)  
- Real-time stock update of available bikes  
- Clear separation of concerns:  
  - Customer data in `customer.py`  
  - Rental logic in `bike_rental.py`  
  - User flow in `main.py`

## Getting Started
1. Clone the repo  
   ```bash
   git clone https://github.com/victoradegoke54G4/bike-rental-app-with-python.git

2. Navigate to the project folder
   ```bash
    cd bike-rental-app-with-python

3. Make sure you have python 3 installed

4. Run the app
    ```bash
    python main.py
