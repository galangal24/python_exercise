def repeat(a, exclaim):
    result = a*3
    if exclaim:
        result = result + '!!!'
    return result


if __name__ == '__main__':
    a = repeat('A', True)
    print(a)