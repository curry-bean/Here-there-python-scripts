from forex_python.converter import CurrencyRates
import tkinter as tk

# create instances of the currency and cryptocurrency converters
currency_converter = CurrencyRates()

# create the GUI
window = tk.Tk()
window.title("Currency Converter")

# create labels for the input and output amounts
input_label = tk.Label(window, text="Amount:")
input_label.grid(row=0, column=0, padx=5, pady=5)

output_label = tk.Label(window, text="Converted amount:")
output_label.grid(row=1, column=0, padx=5, pady=5)

# create entry boxes for the input and output amounts
input_entry = tk.Entry(window)
input_entry.grid(row=0, column=1, padx=5, pady=5)

output_entry = tk.Entry(window)
output_entry.grid(row=1, column=1, padx=5, pady=5)

# create drop-down menus for the input and output currencies
input_currency_var = tk.StringVar(window)
input_currency_var.set("USD")

output_currency_var = tk.StringVar(window)
output_currency_var.set("USD")

input_currency_menu = tk.OptionMenu(window, input_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF")
input_currency_menu.grid(row=0, column=2, padx=5, pady=5)

output_currency_menu = tk.OptionMenu(window, output_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "BTC", "ETH", "XRP", "LTC", "BCH")
output_currency_menu.grid(row=1, column=2, padx=5, pady=5)

# create a button to initiate the conversion
def convert():
    input_amount = float(input_entry.get())
    input_currency = input_currency_var.get()
    output_currency = output_currency_var.get()
    
    if output_currency == "BTC":
        output_amount = crypto_converter.get_crypto_rate("BTC", input_currency) * input_amount
    elif output_currency == "ETH":
        output_amount = crypto_converter.get_crypto_rate("ETH", input_currency) * input_amount
    elif output_currency == "XRP":
        output_amount = crypto_converter.get_crypto_rate("XRP", input_currency) * input_amount
    elif output_currency == "LTC":
        output_amount = crypto_converter.get_crypto_rate("LTC", input_currency) * input_amount
    elif output_currency == "BCH":
        output_amount = crypto_converter.get_crypto_rate("BCH", input_currency) * input_amount
    else:
        output_amount = currency_converter.convert(input_currency, output_currency, input_amount)
    
    output_entry.delete(0, tk.END)
    output_entry.insert(0, round(output_amount, 2))

convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.grid(row=2, column=1, padx=5, pady=5)

window.mainloop()
