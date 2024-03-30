def input_num():
    n_str = ''

    while True:
        n_str = input('Enter the number: ')

        try:
            int(n_str)
            break
        except:
            continue

    return n_str


def split(n_str):
    result = ''

    # start at the end and get by 3 letters
    for i in range(len(n_str) - 1, -1, -3):
        result = ' ' + n_str[max(0, i - 2):i + 1] + result

    return result[1:]


# tests
assert split('1') == '1'
assert split('12') == '12'
assert split('123') == '123'
assert split('1234') == '1 234'
assert split('12345') == '12 345'
assert split('123456') == '123 456'
assert split('1234567') == '1 234 567'

# exec
print(split(input_num()))
