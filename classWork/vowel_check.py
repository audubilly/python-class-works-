def vowel_check():
    my_str = input("Enter a name:  ")
    my_vowels = ["a", "e", "i", "o", "u"]
    for i in my_vowels:
        if i in my_str:
            return print(my_str, "contains vowel")

    return print(my_str, "does not contain vowel")


vowel_check()
