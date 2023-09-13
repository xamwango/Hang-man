import random


def show_player_outcome(secret_word):
    number_of_guesses = 0
    guess_limit = 5
    outcome = ""

    while number_of_guesses < guess_limit:
        players_guess = input("Enter your guess here: ").lower()
        number_of_guesses += 1
        if players_guess != secret_word:
            trials = guess_limit - number_of_guesses
            if trials == 1:
                print("Wrong guess, last trial!!!")
            elif trials == 0:
                outcome = "lose"
            else:
                print(f"Wrong guess, {trials} trials remaining")
        else:
            outcome = "win"
            number_of_guesses = guess_limit
    return outcome


def show_computer_outcome(secret_word):
    number_of_guesses = 0
    guess_limit = 5
    outcome = ""
    computer_guesses = ["mouse", "keyboard", "printer", "monitor", "touchpad", "motherboard", "bios", "usb",
                        "speaker", "microphone", "wifi adapter", "cables", "screen", "cpu", "camera", "webcam",
                        "ram", "rom", "video card", "headphones", "sound card", "hard disk", "ups", "microprocessor"]
    while number_of_guesses < guess_limit:
        computers_guess = random.choice(computer_guesses)
        number_of_guesses += 1
        if computers_guess != secret_word:
            trials = guess_limit - number_of_guesses
            if trials == 0:
                outcome = "lose"
        else:
            outcome = "win"
            number_of_guesses = guess_limit
    return outcome


