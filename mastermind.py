import random

class MastermindGame:
    def __init__(self):
        self.num = random.randrange(1000, 10000)
        self.attempts = 0
        self.max_attempts = 10

    def guess_number(self, guess):
        guess_str = str(guess)
        num_str = str(self.num)
        
        if guess_str == num_str:
            return True, 4, list(guess_str)

        count = 0
        correct = ['X'] * 4
        
        for i in range(4):
            if guess_str[i] == num_str[i]:
                count += 1
                correct[i] = guess_str[i]
        
        return False, count, correct
    
    def validate_input(self, guess):
        if guess.isdigit() and len(guess) == 4:
            return True
        return False
    
    def play(self):
        print("Welcome to the Mastermind Game!")
        
        while self.attempts < self.max_attempts:
            guess = input("Guess the 4-digit number: ")
            
            if not self.validate_input(guess):
                print("Invalid input! Please enter a 4-digit number.")
                continue
            
            self.attempts += 1
            guess = int(guess)
            
            is_correct, count, correct_digits = self.guess_number(guess)
            
            if is_correct:
                print(f"Great! You guessed the number in {self.attempts} tries! You're a Mastermind!")
                break
            else:
                if count > 0:
                    print(f"Not quite the number. But you did get {count} digit(s) correct: {''.join(correct_digits)}")
                else:
                    print("None of the numbers in your input match.")
        
        if self.attempts == self.max_attempts and not is_correct:
            print(f"You couldn't guess the code in {self.max_attempts} attempts. The correct number was {self.num}. Try again!")

if __name__ == "__main__":
    game = MastermindGame()
    game.play()
