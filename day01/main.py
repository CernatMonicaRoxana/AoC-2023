import re


def find_digits():
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


if __name__ == '__main__':
    print(find_digits())
