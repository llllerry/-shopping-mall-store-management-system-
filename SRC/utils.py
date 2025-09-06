# src/utils.py
def validate_number(value):
    try:
        return float(value)
    except ValueError:
        return 0
