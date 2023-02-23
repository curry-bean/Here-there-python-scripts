from tkinter import *
from forex_python.converter import CurrencyRates

# Initialize CurrencyRates object
c = CurrencyRates()

# Create Tkinter window
root = Tk()
root.title("Currency Converter")

# Create input label and field
input_label = Label(root, text="Enter amount:")
input_label.pack()
input_field = Entry(root)
input_field.pack()

# Create currency choice labels and drop-down menus
from_currency_label = Label(root, text="From currency:")
from_currency_label.pack()
from_currency_var = StringVar(root)
from_currency_var.set("USD")  # Set default currency
from_currency_menu = OptionMenu(root, from_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "KES")
from_currency_menu.pack()

to_currency_label = Label(root, text="To currency:")
to_currency_label.pack()
to_currency_var = StringVar(root)
to_currency_var.set("KES")  # Set default currency
to_currency_menu = OptionMenu(root, to_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "KES")
to_currency_menu.pack()

# Create convert button
def convert():
    # Get input amount and convert to float
    amount = float(input_field.get())

    # Get currency conversion rate
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    rate = c.get_rate(from_currency, to_currency)

    # Convert currency and round to 2 decimal places
    converted_amount = round(amount * rate, 2)

    # Display converted amount
    output_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")

convert_button = Button(root, text="Convert", command=convert)
convert_button.pack()

# Create output label
output_label = Label(root, text="")
output_label.pack()

root.mainloop()
