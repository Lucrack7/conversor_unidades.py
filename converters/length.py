def convert_length(value, from_unit, to_unit):
    units = {
        "metros": 1,
        "kilómetros": 1000,
        "millas": 1609.34,
        "pies": 0.3048
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Unidad de longitud no válida.")

    value_in_meters = value * units[from_unit]
    return value_in_meters / units[to_unit]
