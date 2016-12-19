import re


regex_pattern = re.compile(r"[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}")

def validate(code):
    """validate initial code to the uk postal code format.""" 

    return regex_pattern.match(str(code).upper()) is not None
