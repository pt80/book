def main():
    book_path = 'books/frankenstein.txt'
    text = getBookText(book_path)
    words = text.split()
    print(text)
    print(len(words))
    print(countCharacters(text))
    charsSortedList(countCharacters(text))

def sort_on(d):
    return d['num']

def charsSortedList(dictionary):
    sortedList = []
    for ch in dictionary:
        sortedList.append({'name': ch, 'num':dictionary[ch]})
    sortedList.sort(reverse=True, key=sort_on)
    for i in sortedList:
        print('the character ' + str(i['name']) + ' was used ' + str(i['num']) + ' times!!!')


def countCharacters(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def getBookText(path):
    with open(path) as f:
        return f.read()

main()