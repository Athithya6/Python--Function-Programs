def vow_string(s):
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    s1 = s.lower()
    string_set = set(s1)
    #print(string_set)
    string_set_vowel = set()
    for i in string_set:
        if i in vowels_set:
            string_set_vowel.add(i)
    print(string_set_vowel)
    if(string_set_vowel==vowels_set):
        print("lovely string")
    else:
        print("ugly string")


vow_string("")
