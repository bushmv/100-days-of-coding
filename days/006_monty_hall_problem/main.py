from random import SystemRandom


sr = SystemRandom()


def play(swap_decision: bool) -> bool:
    doors = [1, 2, 3]  # sum(doors) = 6
    winning_door = sr.choice(doors)
    choosen_door = sr.choice(doors)
    candidates_to_reveal = [
        door for door in doors if door not in (winning_door, choosen_door)
    ]
    door_to_reveal = sr.choice(candidates_to_reveal)
    # swap_door = [door for door in doors if door not in (choosen_door, door_to_reveal)][0]
    swap_door = 6 - choosen_door - door_to_reveal
    if swap_decision:
        choosen_door = swap_door
    return winning_door == choosen_door


def main() -> None:
    N = 1_000_000
    score = 0
    for i in range(N):
        if play(True):
            score += 1
    print(f"If swap: {score / N * 100}")
    score = 0
    for i in range(N):
        if play(False):
            score += 1
    print(f"If no swap: {score / N * 100}")


if __name__ == "__main__":
    main()
