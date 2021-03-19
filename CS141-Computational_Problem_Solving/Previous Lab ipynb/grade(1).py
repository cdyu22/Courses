def toLetter(score):
	if score >= 97:
		return 'A+'
	elif score < 97 and score >= 93:
		return 'A'
	elif score < 93 and score >= 90:
		return 'A-'
	elif score < 90 and score >= 87:
		return 'B+'
	elif score < 87 and score >= 83:
		return 'B'
	elif score < 83 and score >= 80:
		return 'B-'
	elif score < 80 and score >= 77:
		return 'C+'
	elif score < 77 and score >= 73:
		return 'C'
	elif score < 73 and score >= 70:
		return 'C-'
	elif score < 70 and score >= 67:
		return 'D+'
	elif score < 67 and score >= 63:
		return 'D'
	elif score < 63 and score >= 60:
		return 'D-'
	elif score < 60:
		return 'F'

numeric = float(input("How'd you do? "))
print(toLetter(numeric))
