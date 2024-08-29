class PolkadotDecipher:
    def __init__(self, start_value, end_value):
        if start_value > end_value:
            start_value, end_value = end_value, start_value

        self.start_value = start_value
        self.end_value = end_value

    def calculate_total(self):
        total = 0
        for number in range(self.start_value, self.end_value + 1):
            if number % 15 == 0:
                continue
            elif number % 3 == 0:
                total += number
            elif number % 5 == 0:
                total -= number
        return total

    @staticmethod
    def get_values():
        while True:
            try:
                begin = int(input("Type the start value: "))
                end = int(input("Type the end value: "))

                if begin == end:
                    print("Both values can't be equal. Please try again.")
                    continue

                return begin, end

            except ValueError:
                print("The input needs to be an integer. Please try again.")

def main():
    begin, end = PolkadotDecipher.get_values()
    decipher = PolkadotDecipher(begin, end)
    print(f"The total value is: {decipher.calculate_total()}")

if __name__ == "__main__":
    main()
