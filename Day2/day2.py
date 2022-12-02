opponent_dict = {'A':1, 'B':2, 'C':3}
user_dict = {'X':1, 'Y':2, 'Z':3}
total_score = 0
score = 0

with open("day2input.txt", "r") as f:
    for line in f:
        line = line.strip()
        
        opponent = line[0]
        user = line[2]

        # Rock and Rock (D)
        if opponent == "A" and user == "X":
            score = user_dict[user] + 3

        # Rock and Paper (W)
        if opponent == "A" and user == "Y":
            score = user_dict[user] + 6

        # Rock and Scissors (L)
        if opponent == "A" and user == "Z":
            score = user_dict[user] + 0

        # Paper and Rock (L)
        if opponent == "B" and user == "X":
            score = user_dict[user] + 0

        # Paper and Paper (D)
        if opponent == "B" and user == "Y":
            score = user_dict[user] + 3

        # Paper and Scissors (W)
        if opponent == "B" and user == "Z":
            score = user_dict[user] + 6

        # Scissors and Rock (W)
        if opponent == "C" and user == "X":
            score = user_dict[user] + 6

        # Scissors and Paper (L)
        if opponent == "C" and user == "Y":
            score = user_dict[user] + 0

        # Scissors and Scissors (D)
        if opponent == "C" and user == "Z":
            score = user_dict[user] + 3

        total_score += score


print(f'What would your total score be if everything goes exactly according to your strategy guide? {total_score}')

total_score = 0
score = 0

with open("day2input.txt", "r") as f:
    for line in f:
        line = line.strip()
        
        opponent = line[0]
        user = line[2]

        # Rock and Lose (Scissors = Z)
        if opponent == "A" and user == "X":
            score = user_dict["Z"] + 0

        # Rock and Draw (Rock = X)
        if opponent == "A" and user == "Y":
            score = user_dict["X"] + 3

        # Rock and Win (Paper = Y)
        if opponent == "A" and user == "Z":
            score = user_dict["Y"] + 6

        # Paper and Lose (Rock = X)
        if opponent == "B" and user == "X":
            score = user_dict["X"] + 0

        # Paper and Draw (Paper = Y)
        if opponent == "B" and user == "Y":
            score = user_dict["Y"] + 3

        # Paper and Win (Scissors = Z)
        if opponent == "B" and user == "Z":
            score = user_dict["Z"] + 6

        # Scissor and Lose (Paper = Y)
        if opponent == "C" and user == "X":
            score = user_dict["Y"] + 0

        # Scissor and Draw (Scissor = Z)
        if opponent == "C" and user == "Y":
            score = user_dict["Z"] + 3

        # Scissor and Win (Rock = X)
        if opponent == "C" and user == "Z":
            score = user_dict["X"] + 6

        total_score += score

print(f'what would your total score be if everything goes exactly according to your strategy guide? {total_score}')
        
