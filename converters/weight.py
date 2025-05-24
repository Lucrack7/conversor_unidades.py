def convert_weight(value, from_unit, to_unit):
    units = {
        "kilogramos": 1,
        "gramos": 0.001,
        "libras": 0.453592
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Unidad de peso no válida.")

    value_in_kg = value * units[from_unit]
    return value_in_kg / units[to_unit]
