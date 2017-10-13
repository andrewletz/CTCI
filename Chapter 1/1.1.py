'''
		Cracking the Code Interview 1.1
		Authors: Andrew Letz, Justin Robles
		Problem: Is Unique
'''

def isUnique(s):
	i = 1
	for c in s:
		if c in s[i:]:
			return False
		i += 1
	return True

def driver():
		# Inputs that should return true
		input1 = "azsxdcfvgbhnjm"
		input2 = "qawsedrftgyhuj"
		input3 = "a"

		# Inputs that should return false
		input4 = "aaaaaaaaa"
		input5 = "asdfghjklaaa"
		input6 = "tt"

		print("Testing {}: {}".format(input1, isUnique(input1)))
		print("Testing {}: {}".format(input2, isUnique(input2)))
		print("Testing {}: {}".format(input3, isUnique(input3)))

		print("Testing {}: {}".format(input4, isUnique(input4)))
		print("Testing {}: {}".format(input5, isUnique(input5)))
		print("Testing {}: {}".format(input6, isUnique(input6)))

if __name__ == "__main__":
    driver()
