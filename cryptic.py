import sys

ALPHABET =        "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
POLISH_ALPHABET = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"


def rotate(alphabet, rotated_alphabet, character):
    index = alphabet.index(character)
    return rotated_alphabet[index]


def rot(sentence, alphabet, rotated_alphabet, reverse):
    if reverse:
        sentence = sentence[::-1]
    result = []
    for character in sentence:
        result.append(rotate(alphabet, rotated_alphabet, character))
    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        exit()
    filename = sys.argv[1]
    sentence = []
    with open(filename) as f:
        for line in f.readlines():
            elements = line.rstrip('\n').split(' ')
            page, char, word = elements
            sentence.append(char)
    sentence = ''.join(sentence).lower()
    for reverse in {False, True}:
        for alphabet in (ALPHABET, POLISH_ALPHABET):
            for rotation in range(len(alphabet) - 1):
                rotated_alphabet = alphabet[-rotation:] + alphabet[:-rotation]
                print(rot(sentence, alphabet, rotated_alphabet, reverse))
                print()


if __name__ == '__main__':
    main()

