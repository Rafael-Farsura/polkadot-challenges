import random

class BingoGame:
    def __init__(self):
        self.card = self.generate_card()
        self.drawn_numbers = set()
        self.total_draws = 0

    def generate_card(self):
        return random.sample(range(1, 50), 5)

    def draw_number(self):
        while True:
            number = random.randint(1, 49)
            if number not in self.drawn_numbers:
                self.drawn_numbers.add(number)
                self.total_draws += 1
                return number

    def play_game(self):
        print(f"Your Bingo card: {self.card}")
        remaining_numbers = set(self.card)

        while remaining_numbers:
            drawn_number = self.draw_number()
            print(f"Drawn number: {drawn_number}")

            if drawn_number in remaining_numbers:
                remaining_numbers.remove(drawn_number)
                print(f"You guessed correctly! Numbers left on your card: {remaining_numbers}")
            else:
                print(f"Number {drawn_number} was not on your card.")

        print(f"Congratulations! You completed your card in {self.total_draws} draws.")

def main():
    game = BingoGame()
    game.play_game()

if __name__ == "__main__":
    main()
