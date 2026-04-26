import random

def roll_dice():
    return random.randint(1, 6)

def play_round():
    p1 = roll_dice()
    p2 = roll_dice()
    return p1, p2

def update_score(p1_score, p2_score, scores):
    if p1_score > p2_score:
        scores["p1"] += 1
    elif p2_score > p1_score:
        scores["p2"] += 1
    return scores