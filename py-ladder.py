import dice
import player
import S_L
import Assets
import time

print(Assets.welcome)
time.sleep(2)
player_count = int(input("Number of players: "))
time.sleep(2)

Players = []
for i in range(player_count):

    variant = input(f"\nEnter name for player {i+1}: ")
    Temp_variant = player.Plr(variant,0)
    Players.append(Temp_variant)

time.sleep(2)
initiator = input("\nPress enter to start game! ")
time.sleep(2)
print(Assets.start)

while True:
    time.sleep(2)
    #Exits the program after game over message
    if len(Players) == 0:
        break


    for j in Players:
        initiator = input(f"{j.name}, press enter to roll dice! ")
        time.sleep(1)


        rolled = dice.roll()
        print (f"\nDice rolled {rolled}!\n")
        time.sleep(1)

        #repeates rolling for the current player if and as long as the dice value is 6
        while True:

            if rolled == 6:
                print("You get an extra roll!\n")
                time.sleep(1)

            if j.current_position == 0:
                j.current_position = j.first_move(rolled)


                #first-move: updates current_position to 1 only if dice rolled 1
                if j.current_position == 1:
                    print(f"Yay!, {j.name} started playing. Current position is {j.current_position}\n")
                    time.sleep(1)
                else:
                    print(f"Oops! {j.name} could't start playing because dice didn't roll 1\n")
                    time.sleep(1)

            #increments/decrements player position based on die roll/ladder_climb/caught_by_snake 
            elif j.current_position >= 1 and j.current_position + rolled <= 100:
                j.current_position = j.main_move(rolled, j.current_position)
                print(f"{j.name} moved to {j.current_position}\n")
                time.sleep(1)

                if str(j.current_position) in Assets.snakes:
                    j.current_position = S_L.swallow(j.current_position, Assets.snakes[str(j.current_position)])
                    print(f"Oh no! {j.name} got swallowed by a snake. Back to {j.current_position}\n")
                    time.sleep(1)


                if str(j.current_position) in Assets.ladders:
                    j.current_position = S_L.climb(j.current_position, Assets.ladders[str(j.current_position)])
                    print(f"Aww yea! {j.name} found a ladder. Climbed to {j.current_position}\n")
                    time.sleep(1)


            elif j.current_position + rolled > 100:
                print(f"you can't move past 100. Die must roll {100 - j.current_position} to win\n")
                time.sleep(1)


            if j.current_position == 100:
                print(f"Woohoo!... {j.name} won the game!\n")
                time.sleep(1)
                updated_Players = []
                for k in Players:
                    if k.current_position != 100:
                        updated_Players.append(k)

                Players = updated_Players
                print(f"Players left: {len(Players)}\n")
                time.sleep(1)
                if len(Players) < 1:
                    print(Assets.game_over)
                    time.sleep(1)
                    break
            #Manages extra roll situations and breaks the iterator if extra roll is not 6
            if rolled == 6:
                initiator = input(f"{j.name},press enter to roll the extra roll\n")
                time.sleep(1)
                rolled = dice.roll()
                print (f"Dice rolled {rolled}!\n")
                time.sleep(1)
                continue
            elif rolled != 6:
                break