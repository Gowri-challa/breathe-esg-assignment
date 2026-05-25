def normalize_value(value, unit):

    unit = unit.lower()

    if unit == "liters":
        return value * 2.31

    elif unit == "kwh":
        return value * 0.5

    elif unit == "km":
        return value * 0.2

    return value