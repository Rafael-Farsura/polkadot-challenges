class NumberUtils:

    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))


class MagicNumberFinder:

    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start value must be less than or equal to end value.")
        self.start = start
        self.end = end

    def find_magic_number(self):
        for num in range(self.start, self.end + 1):
            if self._is_magic_number(num):
                return num
        return None

    def _is_magic_number(self, num):
        return (num % 4 == 0 and
                NumberUtils.is_prime(num) and
                NumberUtils.sum_of_digits(num) % 2 == 1)


class UserInput:

    @staticmethod
    def get_interval():
        while True:
            try:
                start = int(input("Enter the start value of the interval: "))
                end = int(input("Enter the end value of the interval: "))
                if start > end:
                    print("Start value must be less than or equal to end value. Please try again.")
                    continue
                return start, end
            except ValueError:
                print("Input must be an integer. Please try again.")


def main():
    start, end = UserInput.get_interval()
    finder = MagicNumberFinder(start, end)
    magic_number = finder.find_magic_number()

    if magic_number is not None:
        print(f"The magic number found is: {magic_number}")
    else:
        print("No magic number found in the interval.")

if __name__ == "__main__":
    main()
