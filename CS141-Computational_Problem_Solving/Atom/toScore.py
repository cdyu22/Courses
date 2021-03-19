def toLetter(score):
    if score >= 97:
        return 'A+'
    elif score >= 93:
        return 'A'
    elif score >= 90:
        return 'A-'

numeric = float(input("How did you do? "))
print(toLetter(numeric))
