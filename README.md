# Fireworks
A simple Python script that simulates a 10-second New Year's fireworks countdown, printing a celebratory message for a user-specified year.

# 🎆 Fireworks Countdown Simulator

This is a simple command-line program written in Python that simulates a 10-second countdown to a New Year's celebration.

The script prompts the user to enter the year they are celebrating. It then begins a countdown from 10 to 0, printing each number to the screen with a one-second delay. Once the countdown is complete, it prints a "Boom!" and a "Happy New Year" message.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `Fireworks.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is located and run the script:
    ```sh
    python Fireworks.py
    ```
5.  Enter the year you are celebrating (e.g., `2026`) when prompted and press Enter.
6.  Watch the 10-second countdown in your terminal!

## Logic

* **User Input:** The program first asks the user for the `year` to be included in the final message.
* **Countdown Loop:** A `for` loop is used with `range(10, -1, -1)` to iterate from the number 10 down to 0.
* **Timed Pauses:** Inside the loop, `time.sleep(1)` is called after printing each number, causing the program to pause for exactly one second.
* **Final Message:** After the loop finishes, a multi-line f-string is used to print the final celebratory "Boom!" and "Happy {year}!!!" message.

## Technologies Used

* **Python 3**
* `time` module (for the `sleep` function)
