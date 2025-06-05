"""
DIVINEX — sin_selector.py
This file handles the player's Sin selection at the beginning of the game.
"""

import random

# List of all 13 forbidden sins
SINS = [
    "Obsession", "Betrayal", "Envy", "Glory", "Lust",
    "Memory", "Rage", "Worship", "Isolation", "Mercy",
    "Power", "Blame", "Hunger"
]

def display_intro():
    print("\n🔮 You approach the fractured mirror...")
    print("Your blood pulses. The glass responds.")
    print("You are not chosen. You are claimed.\n")

def present_sins():
    print("The forbidden Sins whisper:")
    for i, sin in enumerate(SINS, 1):
        print(f"  [{i}] {sin}")
    print()

def choose_sin():
    while True:
        try:
            choice = int(input("Enter the number of the Sin that pulls at you most: "))
            if 1 <= choice <= len(SINS):
                return SINS[choice - 1]
            else:
                print("That Sin does not answer you. Try again.")
        except ValueError:
            print("The gods don't understand that. Use a number.")

def main():
    display_intro()
    present_sins()
    chosen_sin = choose_sin()
    print(f"\n⚠️ The Sin of {chosen_sin} binds to your blood. It will shape everything.\n")

if __name__ == "__main__":
    main()
