def is_palindrome(s):
    return s == s[::-1]


def is_mirrored_string(s):

    mirror_m = {
    'A': 'A',
    'H': 'H',
    'I': 'I',
    'M': 'M',
    'O': 'O',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    '1': '1',
    '8': '8',
    'E': 'З',
    'J': 'L',
    'S': '2',
    'Z': '5',
    }
    mirrored_s = ''.join([mirror_m.get(char, '') for char in s])
    return mirrored_s == s[::-1]


def main():

    s = input()

    if is_palindrome(s) and is_mirrored_string(s):
        print(f'"{s}" is a mirrored palindrome.')
    elif is_mirrored_string(s):
        print(f'"{s}" is a mirrored string.')
    elif is_palindrome(s):
        print(f'"{s}" is a regular palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')


if __name__ == "__main__":
    main()
