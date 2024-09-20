# E-Hallway Pass

E-Hallway Pass is a simple Python application that tracks the time a user is away by scanning their ID before and after leaving. It provides feedback based on how much time the user has been out.

## Features
- Scans an ID at the beginning and when the user returns.
- Tracks time spent between the scans.
- Provides feedback based on the time duration:
  - If the user is out for 20 seconds or less, they are asked if they even left.
  - If the user is out for less than a minute, they are welcomed back with the time spent in seconds.
  - If the user is out between 1 and 10 minutes, they are welcomed back with the time spent in minutes.
  - If the user is out for more than 10 minutes, they are questioned about their whereabouts.

## How to Use
1. Run the script in a Python environment.
2. When prompted, scan your ID to the card read connected to your device (or input any unique string to simulate the ID).
3. After some time, scan the ID again when you return.
4. The program will give feedback based on the time you were away.

## Code Explanation
- The `newSCAN()` function runs in a loop, prompting the user to scan their ID when they leave and return.
- The time between scans is measured and feedback is given based on the time spent away.
- The `newLine()` function prints separators for better output readability.

## Important Notes
- This code uses `input()` to simulate scanning IDs. In a real-world application, you would integrate actual scanning hardware or software.
- The program runs indefinitely in a loop. To exit, you may need to manually stop the script (e.g., by pressing `Ctrl+C`).

## License
This project is licensed under the MIT License.
