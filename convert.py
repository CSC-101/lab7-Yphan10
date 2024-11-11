from typing import Optional

def str_to_float(input_str: str) -> Optional[float]:

    try:
        return float(input_str)
    except ValueError:
        return None

