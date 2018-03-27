from random import randint

step = ['Rock', 'Paper', 'Scissors']


def abc(player=False):
    if player:
        return step.index(step[int(raw_input("What do you choose?\n1: %s, 2: %s, 3: %s.\nPaste input here =======>"
                                           % (step[0], step[1], step[2]))) - 1]) + 1
    else:
        return randint(1, 3)


def point_value(p1, p2):
    points = p1 -p2
    if points == 0:
        print("\nIt is a Tie!\n")
    elif points in (1, -2):
        print("\nYou Win!\n")
    else:
        print("\nYou Lose!\n")

if __name__ == "__main__":
    print("Welcome to the Rock, Paper, Scissors game! Hope you have a nice time! Please go ahead!")
    while True:
        print("You are up!\n")
        one = abc(True)
        two = abc()
        point_value(one, two)
        try:
            break_ = raw_input("Would you like to play again? Enter 1 if you would like to quit. If you want to continue, dab ENTER.\n\nPaste input here =======>")
            if 1 == int(break_):
                print("\nEND. Thank you for playing!")
            break
        except ValueError:
            print("\nAGAIN...\n")
