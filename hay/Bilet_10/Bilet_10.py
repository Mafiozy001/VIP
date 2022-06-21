with open('Note.txt') as f:
    text = f.read()
    lines = text.count('\n') + 1

print(lines)
