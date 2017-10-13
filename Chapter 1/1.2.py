'''
		Cracking the Code Interview 1.2
		Authors: Andrew Letz, Justin Robles
		Problem: Check Permutation
'''

def checkPermutation(s1, s2):
	return sorted(s1) == sorted(s2)


def driver():
		# Should return true
		input1_1 = "abcdefg"
		input1_2 = "gfedcba"

		# Should return false
		input2_1 = "AaAaAaAaAa"
		input2_2 = "BbBbBbBbBb"

		# Should return true
		input3_1 = "101010"
		input3_2 = "010101"

		print("Testing {} and {}: {}".format(input1_1, input1_2, checkPermutation(input1_1, input1_2)))
		print("Testing {} and {}: {}".format(input1_1, input1_2, checkPermutation(input1_1, input1_2)))
		
		print("Testing {} and {}: {}".format(input2_1, input2_2, checkPermutation(input2_1, input2_2)))
		print("Testing {} and {}: {}".format(input2_1, input2_2, checkPermutation(input2_1, input2_2)))

		print("Testing {} and {}: {}".format(input3_1, input3_2, checkPermutation(input3_1, input3_2)))
		print("Testing {} and {}: {}".format(input3_1, input3_2, checkPermutation(input3_1, input3_2)))


if __name__ == "__main__":
    driver()
