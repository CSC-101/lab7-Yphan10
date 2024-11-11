import sys
from convert import str_to_float

def main():

    args = sys.argv[1:]  # Skip the first argument which is the script name
    numbers = [str_to_float(arg) for arg in args if str_to_float(arg) is not None]
    print(f"The sum of command-line arguments is: {sum(numbers)}")

if __name__ == '__main__':
    print(sys.argv)


