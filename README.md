# Currency Converter
A simple currency converter application built using Tkinter for the graphical user interface (GUI) and an external currency conversion API for real-time exchange rates.

## Features:
- Convert between multiple currencies using real-time exchange rates.
- Simple, user-friendly interface with Tkinter.
- Error handling for incorrect inputs.

## Installation

1. Clone the repository:
   `git clone https://github.com/matmaslanka/currency-converter.git`
2. Set up a virtual environment:
   python3 -m venv env <br/>
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install the dependencies from requirements.txt:
   `pip install -r requirements.txt`
  If `tkinter` is not installed automatically, install it manually:
  `sudo apt-get install python3-tk` # For Linux



## Running the project
1. Run the app.py:
   `python app.py`
2. The GUI will open where you can select the currencies and perform conversions.

## Usage
### GUI Overview:
Amount Input: Enter the amount of currency to be converted.
From Currency Dropdown: Select the currency to convert from.
To Currency Dropdown: Select the currency to convert to.
Convert Button: Click to fetch real-time rates and display the converted amount.

### Example Use Case:
1. Enter "100" in the "Amount" field.
2. Choose "USD" in the "From Currency" dropdown.
3. Choose "EUR" in the "To Currency" dropdown.
4. Click "Convert" to see the equivalent value in EUR.

