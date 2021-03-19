def toLetter(score):
    if score >= 97:
        to_return = 'A+'
    elif score >= 93:
        to_return = 'A'
    elif score >= 90:
        to_return = 'A-'
    return to_return

numeric = float(input('What did you get?' ))
print(toLetter(numeric))

#or

def toLetter(score):
    if score >= 90:
        to_return = 'A-'
    if score >= 93:
        to_return = 'A'
    if score >= 97:
        to_return = 'A+'
    return to_return

#or

def toLetter(score):
    if score >= 97:
        to_return = 'A+'
    if 97 > score >= 93:
        to_return = 'A'
    if 93 > score >= 90:
        to_return = 'A-'
    return to_return

#or

def toLetter(score):
    if score >= 97:
        return = 'A+'
    if score >= 93:
        return = 'A'
    if score >= 90:
        return = 'A-'
