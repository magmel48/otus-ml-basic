def encrypt(text, key):
    result = ''

    for c in text:
        new_ascii_position = ord(c) + key
        if new_ascii_position > ord('z'):
            new_ascii_position -= 26
        if new_ascii_position < ord('a'):
            new_ascii_position += 26

        result += chr(new_ascii_position)

    return result


def decrypt(text, key):
    return encrypt(text, -key)


def interactive_test():
    key = 0
    text = input('Enter the text: ')

    while True:
        try:
            key_str = input('Enter the key: ')
            key = int(key_str)
            break
        except:
            continue

    print('Encryption result: {r}'.format(r=encrypt(text, key)))

# tests
assert encrypt('dog', 3) == 'grj'
assert encrypt('python', 5) == 'udymts'
assert decrypt('grj', 3) == 'dog'
assert decrypt('udymts', 5) == 'python'

# exec
interactive_test()
