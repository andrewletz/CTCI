# Cracking the Code Interview 1.4
# Authors: Andrew Letz, Justin Robles
# Problem: Palindrome Permutation


def pal_perm(word):
    char_count = {}
    word = word.replace(" ", "")

    for c in word:
        char_count[c] = char_count.get(c, 0) + 1

    if len(word) % 2 == 0:
        for key in char_count:
            if char_count[key] % 2 is not 0:
                return False
    else:
        odd_count = 0
        for key in char_count:
            if char_count[key] % 2 is not 0:
                odd_count += 1
                if odd_count > 1:
                    return False

    return True


def driver():
    assert pal_perm("tact coa")
    assert pal_perm("aaa")
    assert not pal_perm("bca")


if __name__ == "__main__":
    driver()
