from typing import Optional
# Define the str_to_float function, which takes a single string parameter
# and returns either a float (if conversion is successful) or None (if conversion fails)
def str_to_float(input_str: str) -> Optional[float]:

    try:
        return float(input_str)
    except ValueError:
        return None

