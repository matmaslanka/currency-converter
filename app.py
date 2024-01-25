import tkinter as tk
from tkinter import messagebox, ttk
from libs.openexchange import OpenExchangeClient

APP_ID = "d3f8f1713f8f47058623feeda02c90d6"

client = OpenExchangeClient(APP_ID)

def input_currency():
    # get selected value
    from_value = currency_from.get()
    return from_value


def output_currency():
    # get selected value
    to_value = currency_to.get()
    return to_value


def amount_currency():
    amount_value = amount.get()
    return amount_value


def equation():
    multi = int(output_currency())*int(input_currency())*int(amount_currency())
    messagebox.showinfo(
        message=f"The selected value is: {multi}",
        title="Selected"
    )
    return multi


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

result = tk.Label(main_window, text=":)")
result.place(x=25, y=300)

button = ttk. Button(text="Poka co tam!", command=equation)  # To jest na razie tymczasowe
button.place(x=25, y=360)  # To jest na razie tymczasowe
main_window.mainloop()
