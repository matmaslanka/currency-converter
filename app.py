import tkinter as tk
# import time
from tkinter import ttk
from libs.openexchange import OpenExchangeClient

APP_ID = "d3f8f1713f8f47058623feeda02c90d6"

client = OpenExchangeClient(APP_ID)


def input_currency():
    # get selected value
    from_value = currency_from.get()
    if from_value == "":
        return "USD"
    else:
        return str(from_value)


def output_currency():
    # get selected value
    to_value = currency_to.get()
    if to_value == "":
        return "PLN"
    else:
        return str(to_value)


def amount_currency():
    amount_value = amount.get()
    if amount_value == "":
        return 0
    else:
        return float(amount_value)


def equation():
    multi = client.convert(amount_currency(), input_currency(), output_currency())
    return multi


def result():
    info = f"{amount_currency():.2f} {input_currency()} = {equation():.2f} {output_currency()}"
    message = tk.Label(main_window, text=info)
    message.place(x=25, y=300)
    return message


# I need to add when was last update
# def last_update():
#     update_info =
#     update_info.place(x=25, y= 330)


main_window = tk.Tk()
main_window.geometry("400x600")
main_window.minsize(400, 600)
main_window.maxsize(400, 600)
main_window.title("Currency converter")

title_label = tk.Label(main_window, text="Currency Conventer", fg="white", bg="black", height=10)
title_label.pack(side="top", fill="x")

from_label = tk.Label(main_window, text="FROM:")
from_label.place(x=25, y=170)

currency_from = ttk.Combobox(main_window, state="readonly", values=client.current_list)
currency_from.place(x=25, y=200)

to_label = tk.Label(main_window, text="TO:")
to_label.place(x=220, y=170)

currency_to = ttk.Combobox(main_window, state="readonly", values=client.current_list)
currency_to.place(x=220, y=200)

amount_label = tk.Label(main_window, text="AMOUNT")
amount_label.place(x=25, y=230)

amount = tk.Entry(main_window)
amount.place(x=25, y=260)

button = ttk. Button(text="Convert!", command=lambda: [equation(), result()])
button.place(x=25, y=360)
main_window.mainloop()
