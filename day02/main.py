def part_1():
    games = open("input.txt")
    res = 0
    for game in games:
        game_id, hands = get_hands_from_game_1(game.strip())

        if valid_game_1(hands):
            res += int(game_id)

    return res


def get_hands_from_game_1(game):
    game_id, hands = game.split(": ")
    game_id = game_id.split(" ")[1]
    return game_id, hands


def valid_game_1(game):
    bag_1 = {"red": 12, "green": 13, "blue": 14}

    hands = game.split("; ")

    for hand in hands:
        hand_1 = hand.split(", ")
        for cube in hand_1:
            no, color = cube.split(" ")
            if bag_1[color] < int(no):
                return False

    return True


def part_2():
    games = open("input.txt")
    max_conf = {}
    sumi = 0
    for game in games:
        power = 1
        game_id, hands = get_hands_from_game_2(game.strip())
        max_conf = valid_game_2(hands)

        for item in max_conf:
            power *= max_conf[item]

        sumi += power

    return sumi


def get_hands_from_game_2(game):
    game_id, hands = game.split(": ")
    game_id = game_id.split(" ")[1]
    return game_id, hands


def valid_game_2(game="3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"):
    bag_1 = {"red": 12, "green": 13, "blue": 14}
    max_cubes = {"red": 0, "green": 0, "blue": 0}

    hands = game.split("; ")
    for hand in hands:
        hand_1 = hand.split(", ")
        for cube in hand_1:
            no, color = cube.split(" ")
            if max_cubes[color] < int(no):
                max_cubes[color] = int(no)

    return max_cubes


if __name__ == '__main__':
    print(part_2())
