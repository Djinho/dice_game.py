import random

def roll(double=False):
    """
    Simulate rolling a die. If double is True, simulate rolling two dice but
    consider the outcome as double the value rolled, unless a 1 is rolled,
    which ends the turn.
    """
    min_value = 1
    max_value = 6
    # Increased chance of rolling a 1 for double rolls
    if double and random.random() <= 0.15:
        return 1
    else:
        roll = random.randint(min_value, max_value)
        return roll * 2 if double else roll

# Collect player names
player_names = []
while True:
    num_players = input("Enter the amount of participants (2-4): ")
    if num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players <= 4:
            for i in range(1, num_players + 1):
                name = input(f"Enter player {i}'s name: ")
                player_names.append(name)
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 75
player_scores = [0 for _ in range(num_players)]

while max(player_scores) < max_score:
    for player_idx, player_name in enumerate(player_names):
        print(f"{player_name}'s turn has just started!\n")
        print(f"Your total score is {player_scores[player_idx]}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y/n) ")
            if should_roll.lower() != "y":
                break

            double_roll = input("Do you want to double roll? (y/n) ")
            value = roll(double=(double_roll.lower() == "y"))
            if value == 1:
                print("You rolled a 1! Your turn is over, and you score nothing this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled: {value}")

        player_scores[player_idx] += current_score
        print(f"Your total score is now: {player_scores[player_idx]}")

print("Game over.")
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"{player_names[winning_idx]} is the winner with a score of: {max_score}")
