def compte_occurences(liste):
    occurrences = {}
    for mot in liste:
        occurrences[mot] = occurrences.get(mot, 0) + 1
    return occurrences

print(compte_occurences(["alae", "react", "alae", "iise", "react", "apple"]))  

