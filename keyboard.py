from convert import str_to_float

# Define the gather_numbers function which prompts the user to enter numbers until they type 'done'.
# It returns a list of successfully converted floats.
def gather_numbers() -> list[float]:
# Initialize an empty list to store the valid float numbers entered by the user
    numbers = []
    while True:
# Loop to continually prompt the user for input until they type "done"
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

