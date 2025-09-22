def convert_units(amount, from_unit, to_unit):
    conversions = {
        ("km", "miles"): lambda x: x * 0.621371,
        ("miles", "km"): lambda x: x / 0.621371,
        ("kg", "lbs"): lambda x: x * 2.20462,
        ("lbs", "kg"): lambda x: x / 2.20462,
        # Add more as needed
    }
    key = (from_unit.lower(), to_unit.lower())
    if key in conversions:
        return f"{amount} {from_unit} = {conversions[key](float(amount)):.2f} {to_unit}"
    return "Sorry, I can't convert those units."