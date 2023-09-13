from logging import exception
from hang_man import show_player_outcome, show_computer_outcome
import random

game_type = input("Game type: enter one for one player, two for two player and practice for a demo: ").lower()
if game_type == "one" or game_type == "two":
    number_of_rounds = int(input("Enter the number of rounds to play per game: "))
else:
    number_of_rounds = 1
round_number = 1
total_points = {
    "player1": 0,
    "player2": 0,
    "computer": 0
}
while round_number <= number_of_rounds:
    practice_secret = random.choice(["soccer", "football", "netball", "baseball", "handball", "tennis", "badminton",
                                     "chess", "darts", "archery", "basketball", "volleyball", "hockey"])
    computer_secret = random.choice(["mouse", "keyboard", "printer", "monitor",
                                     "touchpad", "motherboard", "bios", "usb"])
    print(f"Round {round_number}")
    if game_type == "two":
        player1_secret_word = input("Player1 enter your secret word: ").lower()
        print("Player2's turn to play")
        player2_outcome = show_player_outcome(player1_secret_word)
        player2_secret_word = input("Player 2 enter your secret word: ").lower()
        print("Player1's turn to play")
        player1_outcome = show_player_outcome(player2_secret_word)
        if player1_outcome == "win":
            total_points["player1"] += 1
        else:
            pass
        if player2_outcome == "win":
            total_points["player2"] += 1
        else:
            pass
    elif game_type == "one":
        print("It's player's turn to play")
        player_outcome = show_player_outcome(computer_secret)
        player_secret_word = input("Enter your secret word, it must be in the domain of a computer part: ").lower()
        print("Computer now playing")
        computer_outcome = show_computer_outcome(player_secret_word)
        if player_outcome == "win":
            total_points["player1"] += 1
        else:
            pass
        if computer_outcome == "win":
            total_points["computer"] += 1
        else:
            pass
    elif game_type == "practice":
        print("You're now playing in demo mode")
        clue = input("Do you need a clue?☺ Y for yes and N for no: ").lower()
        if clue == "y":
            print(f"The secret word is name of a game with {len(practice_secret)} letters and associated with a body "
                  f"part😊")
        else:
            print("Alright😉, you can proceed")
        player_outcome = show_player_outcome(practice_secret)
        if player_outcome == "win":
            print("You win!!!☺")
        else:
            print("You lose!!!😞")
    else:
        raise exception("Invalid input")
    round_number += 1
if game_type == "two":
    if total_points["player1"] > total_points["player2"]:
        print(f'Player1 wins the game with {total_points["player1"]} point(s) !!!')
    elif total_points["player1"] < total_points["player2"]:
        print(f'Player2 wins the game with {total_points["player2"]} point(s) !!!')
    else:
        print("Both players has the same number of point(s), game ends as a draw")
elif game_type == "one":
    if total_points["player1"] > total_points["computer"]:
        print(f'Player wins the game with {total_points["player1"]} point(s) !!!')
    elif total_points["player1"] < total_points["computer"]:
        print(f'The computer wins the game with {total_points["computer"]} point(s) !!!')
    else:
        print("The player and the computer have same number of point(s), game ends as a draw!!!🤗")