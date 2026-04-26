def show_result(p1_name, p2_name, p1_roll, p2_roll, scores):
    print(f"{p1_name} rolled: {p1_roll}")
    print(f"{p2_name} rolled: {p2_roll}")

    if p1_roll > p2_roll:
        print(f"{p1_name} wins this round!")
    elif p2_roll > p1_roll:
        print(f"{p2_name} wins this round!")
    else:
        print("This round is a draw!")

    print(f"\nScore -> {p1_name}: {scores['p1']} | {p2_name}: {scores['p2']}")