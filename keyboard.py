from convert import str_to_float

def gather_numbers() -> list[float]:

    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == "done":
            break
        converted = str_to_float(user_input)
        if converted is not None:
            numbers.append(converted)
    return numbers


if __name__ == '__main__':
    result = gather_numbers()
    print(f"The sum of the numbers is: {sum(result)}")

