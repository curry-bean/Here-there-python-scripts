import ccxt
from forex_python.converter import CurrencyRates
import tkinter as tk

# Initialize the CCXT exchange instance and the Forex converter instance
exchange = ccxt.binance()
converter = CurrencyRates()

# Create the tkinter window
root = tk.Tk()
root.title("Cryptocurrency Converter")

# Create the widgets
currency_label = tk.Label(root, text="Select Currency:")
currency_label.grid(row=0, column=0, padx=10, pady=10)

currency_options = ["BTC", "ETH", "LTC", "XRP", "BCH"]
currency_var = tk.StringVar(root)
currency_var.set(currency_options[0])

currency_menu = tk.OptionMenu(root, currency_var, *currency_options)
currency_menu.grid(row=0, column=1, padx=10, pady=10)

usd_label = tk.Label(root, text="USD Equivalent:")
usd_label.grid(row=1, column=0, padx=10, pady=10)

usd_value = tk.Label(root, text="0.00")
usd_value.grid(row=1, column=1, padx=10, pady=10)

# Function to update the USD value based on the selected cryptocurrency
def update_usd_value(*args):
    # Get the selected currency
    currency = currency_var.get()

    # Get the current cryptocurrency price in USD
    ticker = exchange.fetch_ticker(f"{currency}/USDT")
    price = ticker["last"]
    
    # Get the current USD exchange rate
    usd_rate = converter.get_rate("USD", "KES")
    
    # Calculate the USD equivalent
    usd_equivalent = price * usd_rate
    
    # Update the USD value label
    usd_value.config(text=f"{usd_equivalent:.2f}")

# Bind the update function to the currency menu
currency_var.trace("w", update_usd_value)

# Run the tkinter event loop
root.mainloop()
