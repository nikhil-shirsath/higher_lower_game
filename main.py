#import data file
from game_data import data
#import art file
import art
# import random
# from replit import clear

score = 0
is_true = True

#generate a_player and b_player randomly

while (is_true):
    clear()
    print(art.logo)
    print(f"Your score is {score}")

    b_player_dictionary = data[random.randint(0, len(data) - 1)]
    a_player_dictionary = data[random.randint(0, len(data) - 1)]

    print(
        f"Compare A: {a_player_dictionary['name']}, {a_player_dictionary['description']}, from {a_player_dictionary['country']}. "
    )

    print(art.vs)
    print(
        f"Against B: {b_player_dictionary['name']}, {b_player_dictionary['description']}, from {b_player_dictionary['country']}. "
    )
    #take users input
    user_answer = input("who has more follower_count ? Type 'A' or 'B' :")

    if a_player_dictionary['follower_count'] > b_player_dictionary[
            'follower_count'] and (user_answer == 'A' or user_answer == 'a'):
        score += 1

    elif a_player_dictionary['follower_count'] < b_player_dictionary[
            'follower_count'] and (user_answer == 'b' or user_answer == 'B'):
        score += 1

    else:
        clear()
        print(f"You lost , your score is {score}")
        is_true = False
