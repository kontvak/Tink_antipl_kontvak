
def cleaner(text):
    if text.count('"""') != 0:
        a = text.count('"""') // 2
        for i in range(a):
            first = text.find('"""')
            sec = text[first+3:].find('"""') + first + 3
            text = text[0:first] + text[sec+3:]

    if text.count("'''") != 0:
        a = text.count("'''") // 2
        for i in range(a):
            first = text.find("'''")
            sec = text[first+3:].find("'''") + first + 3
            text = text[0:first] + text[sec+3:]

    if text.count('#') != 0:
        a = text.count('#')
        for i in range(a):
            first = text.find('#')
            sec = text[first+1:].find('\n') + first + 1
            text = text[0:first] + '\n' + text[sec+1:]

    return text

