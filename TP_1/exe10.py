def fusionner_dicts(dict1, dict2):
    fusion = dict1.copy()
    for cle, valeur in dict2.items():
        fusion[cle] = fusion.get(cle, 0) + valeur
    return fusion


print(fusionner_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  

