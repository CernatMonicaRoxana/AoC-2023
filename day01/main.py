import re
import string


def part1():
    sumi = 0
    txt = open("input.txt", "r")
    for line in txt:
        digits = re.findall("\d", line)
        if len(digits) == 1:
            sumi += int(digits[0] * 2)
            # print(num)
        else:
            sumi += int(digits[0] + digits[-1])

    txt.close()

    return sumi


def part2():
    nums = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': '4',
        'five': '5e',
        'six': '6',
        'seven': '7',
        'eight': 'e8t',
        'nine': '9',
    }

    txt = open("input.txt", "r")

    res = 0

    for line in txt:
        for k, v in nums.items():
            line = line.replace(k, v)

        digits = re.findall("\d", line)
        if len(digits) == 1:
            res += int(digits[0] * 2)
            # print(num)
        else:
            res += int(digits[0] + digits[-1])

    return res


if __name__ == '__main__':
    print(part2())
