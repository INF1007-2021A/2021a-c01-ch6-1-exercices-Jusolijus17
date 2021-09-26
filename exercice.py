#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        valeurs = input("Entrez 10 valeurs (entier, float, str) séparées par des espaces : ")

        valueList = valeurs.split()
        valueList.sort()

    return valueList


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mots = input("Entrez les deux mots séparés d'un espace : ")
        mots = mots.split()
        print(mots[0][::-1])
        print(mots[0][::-1] == mots[1])
    return mots[0][::-1] == mots[1]


def contains_doubles(items: list) -> bool:
    hasDoubles = False
    for i, item in enumerate(items):
        for j, element in enumerate(items):
            if i != j and item == element:
                hasDoubles = True

    return hasDoubles


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    moyenne = 0
    listeMoyenne = {}
    for clé in student_grades:
        for grade in student_grades[clé]:
            moyenne += grade
        moyenne /= len(student_grades[clé])
        listeMoyenne[clé] = moyenne
        moyenne = 0
    print(listeMoyenne)
    meilleurMoyenne = 0
    for studentKey in listeMoyenne:
        meilleurMoyenne = listeMoyenne[studentKey]
        for otherStudentKey in listeMoyenne:
            if listeMoyenne[otherStudentKey] > meilleurMoyenne:
                meilleurMoyenne = otherStudentKey
    bestStudent = {otherStudentKey: meilleurMoyenne}
    return bestStudent


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
