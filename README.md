# Guess the Number Game

Welcome to the "Guess the Number" game! This is a simple Python game where the player tries to guess a random number within a specified range. The game provides feedback on each guess, guiding the player to find the secret number.

## How to Play

1. Run the game by executing the Python script `guess_the_number.py`.
   ```bash
   python guess_the_number.py
   ```

2. The game will generate a random number within a specified range (by default, between 1 and 100).

3. You'll be prompted to input your guesses. Enter a number and press Enter.

4. The game will tell you if your guess is too high or too low compared to the secret number. Keep guessing until you find the correct number.

5. The game will display the number of attempts it took for you to guess correctly.

6. Enjoy the sense of accomplishment when you find the secret number!

## Customization

You can customize the game by modifying the code in the `guess_the_number.py` script:

- You can change the range of numbers by editing the arguments of `random.randint()` function.
- You can set a limit on the number of attempts allowed by adding a counter and breaking out of the loop when the player exceeds the limit.
- You can add more features or messages to make the game more engaging.

## Contributing

If you'd like to contribute to this game or improve its features, feel free to fork the repository and submit a pull request.
