def to_snake_case(s):
    result = ''
    for token in s.lower().split('_'):
        result += token.capitalize()

    return result


def to_camel_case(s):
    result = ''

    for c in s:
        # add '_' before first capitalized letter
        if c.lower() != c:
            result += '_'
        # add all letters in lower case
        result += c.lower()

    # remove first '_'
    result = result[1:]

    return result


def to_another_case(s):
    # lets' assume each snake_case stuff starts with character in lowercase
    if s[0:1].lower() == s[0:1]:
        return to_snake_case(s)

    # otherwise it's CamelCase
    return to_camel_case(s)


# tests
assert to_another_case('foo') == 'Foo'
assert to_another_case('Foo') == 'foo'
assert to_another_case('my_first_func') == 'MyFirstFunc'
assert to_another_case('AnotherFunction') == 'another_function'
assert to_another_case('my_first_func_') == 'MyFirstFunc'
assert to_another_case('AnotherF') == 'another_f'

# exec
print('tests passed')
