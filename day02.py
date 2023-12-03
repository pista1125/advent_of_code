with open("data/day_02.txt", mode="r", encoding='cp1250') as data:
    df = data.readlines()
df = [x.replace(f"\n", "") for x in df]
possible = "12 red cubes, 13 green cubes, and 14 blue"
print(df)
all_game_num = 0
for x in range(101):
    all_game_num += x

final_number = 0
for game in df:
    game_number = int(game.split(":")[0].split(" ")[1])
    game_set = game.split(":")[1].split(";")
    wrong_set = False
    for set in game_set:
        for x in range(len(set)):
            if  set[x].isdigit() and set[x+1].isdigit() and set[x+3] == "b" and set[x+4] == "l" and set[x+5] == "u" and set[x+6] == "e":
                if int(set[x] + set[x+1]) > 14:
                    wrong_set = True
            elif set[x].isdigit() and set[x+1].isdigit() and set[x+3] == "g" and set[x+4] == "r" and set[x+5] == "e" and set[x+6] == "e" and set[x+7] =="n":
                if int(set[x] + set[x+1]) > 13:
                    wrong_set = True
            elif set[x].isdigit() and set[x+1].isdigit() and set[x+3] == "r" and set[x+4] == "e" and set[x+5] == "d":
                if int(set[x] + set[x+1]) > 12:
                    wrong_set = True
    if wrong_set:
        final_number += game_number


correct_answer = all_game_num - final_number
print(correct_answer)