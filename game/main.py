from game.logic import play_round, update_score
from game.player import get_player_names
from game.result import show_result

def menu():
    print("\n🎲 Dice Roll Game")
    print("1. Play Round")
    print("2. Show Score")
    print("3. Reset Score")
    print("4. Exit")

def main():
    p1_name, p2_name = get_player_names()

    scores = {"p1": 0, "p2": 0}   

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            p1_roll, p2_roll = play_round()
            scores = update_score(p1_roll, p2_roll, scores)
            show_result(p1_name, p2_name, p1_roll, p2_roll, scores)

        elif choice == "2":
            print(f"\nScore -> {p1_name}: {scores['p1']} | {p2_name}: {scores['p2']}")

        elif choice == "3":
            scores = {"p1": 0, "p2": 0}
            print("Score reset!")

        elif choice == "4":
            print("Exiting game...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()