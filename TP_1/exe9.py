def analyse_texte(texte):
    mots = texte.split()
    return {
        "NombreDeMots": len(mots),
        "NombreDeCaracteres": len(texte)
    }


print(analyse_texte("React js better than angular"))  

