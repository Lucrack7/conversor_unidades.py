import tkinter as tk
from tkinter import ttk, messagebox

from converters.length import convert_length
from converters.weight import convert_weight
from converters.temperature import convert_temperature

CATEGORY_UNITS = {
    "Longitud": ["metros", "kilómetros", "millas", "pies"],
    "Peso": ["kilogramos", "gramos", "libras"],
    "Temperatura": ["Celsius", "Fahrenheit", "Kelvin"]
}

def convert():
    category = category_var.get()
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    try:
        value = float(value_entry.get())
        if category == "Longitud":
            result = convert_length(value, from_unit, to_unit)
        elif category == "Peso":
            result = convert_weight(value, from_unit, to_unit)
        elif category == "Temperatura":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            raise ValueError("Categoría no válida.")

        result_var.set(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_units(*args):
    category = category_var.get()
    units = CATEGORY_UNITS.get(category, [])
    from_unit_menu['values'] = units
    to_unit_menu['values'] = units
    from_unit_var.set(units[0])
    to_unit_var.set(units[1])

# GUI Setup
root = tk.Tk()
root.title("Conversor de Unidades")

category_var = tk.StringVar(value="Longitud")
from_unit_var = tk.StringVar()
to_unit_var = tk.StringVar()
value_entry = tk.Entry(root)
result_var = tk.StringVar()

# Widgets
ttk.Label(root, text="Categoría:").grid(row=0, column=0, padx=5, pady=5)
category_menu = ttk.Combobox(root, textvariable=category_var, values=list(CATEGORY_UNITS.keys()), state="readonly")
category_menu.grid(row=0, column=1)
category_menu.bind("<<ComboboxSelected>>", update_units)

ttk.Label(root, text="Convertir de:").grid(row=1, column=0)
from_unit_menu = ttk.Combobox(root, textvariable=from_unit_var, state="readonly")
from_unit_menu.grid(row=1, column=1)

ttk.Label(root, text="a:").grid(row=2, column=0)
to_unit_menu = ttk.Combobox(root, textvariable=to_unit_var, state="readonly")
to_unit_menu.grid(row=2, column=1)

ttk.Label(root, text="Valor:").grid(row=3, column=0)
value_entry.grid(row=3, column=1)

ttk.Button(root, text="Convertir", command=convert).grid(row=4, columnspan=2, pady=10)
ttk.Label(root, textvariable=result_var, font=('Arial', 12, 'bold')).grid(row=5, columnspan=2)

update_units()

root.mainloop()
