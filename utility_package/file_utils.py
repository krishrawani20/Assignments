def count_line(n):
    file = open(n,'r') 
    f = file.read()
    lines = len(f.splitlines)
    return lines


def count_words(n):
    f = open(n,'r')
    f = f.read()
    words = len(f.split())
    return words