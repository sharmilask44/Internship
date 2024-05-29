import random

def gen_code():
    return ''.join(random.choices('123456', k=4))

def evaluate_guess(code, guess):
    exact_matches = sum(code[i] == guess[i] for i in range(4))
    code_digits = {digit: code.count(digit) for digit in set(code)}
    guess_digits = {digit: guess.count(digit) for digit in set(guess)}
    total_matches = sum(min(code_digits[digit], guess_digits[digit]) for digit in set(guess))
    return exact_matches, total_matches - exact_matches

def main():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code.")
    code = gen_code()
    attempts = 0

    while True:
        guess = input("Enter your guess (4 digits from 1 to 6): ")
        if len(guess) != 4 or not guess.isdigit() or not all('1' <= digit <= '6' for digit in guess):
            print("Invalid guess. Please enter 4 digits from 1 to 6.")
            continue
        
        attempts += 1
        exact_matches, partial_matches = evaluate_guess(code, guess)
        print(f"Result: {exact_matches} exact matches, {partial_matches} partial matches.")

        if exact_matches == 4:
            print(f"Congratulations! You guessed the code '{code}' in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
