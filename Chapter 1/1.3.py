# Cracking the Code Interview 1.3
# Authors: Andrew Letz, Justin Robles
# Problem: URLify


def URLify(name, length):
    new_str = name[:length]
    for i in new_str:
        if i == " ":
            first_slice = new_str[:new_str.index(i)]
            second_slice = new_str[new_str.index(i) + 1:]
            first_slice += ["%", "2", "0"]
            new_str = first_slice + second_slice
    for x in range(len(new_str)):
        name[x] = new_str[x]


def driver():
    input1_1 = list("Mr John Smith    ")
    input1_2 = 13

    URLify(input1_1, input1_2)

    assert input1_1 == ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h']


if __name__ == "__main__":
    driver()




