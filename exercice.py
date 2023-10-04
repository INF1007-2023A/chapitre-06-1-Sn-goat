#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order():
    values_input = input("Entrez une liste de valeur: ")
    values = values_input.split(",") 
    newList_str = [i for i in values if '"' in i ]
    newList_int_flot = [i for i in  values if '"' not in i ]
    newList_float = [i for i in newList_int_flot if float(i) % 1 != 0]
    newList_int = [i for i in newList_int_flot if float(i) % 1 == 0]
    newList = []
    newList.extend(newList_int)
    newList.extend(newList_float)
    newList.extend(newList_str)
    print(newList)


def anagrams():
    word1 = input("Entrez un mot: ")
    word1List = [i for i in word1]
    word1List.sort()
    word2 = input("Entrez un autre mot ")
    word2List = [i for i in word2]
    word2List.sort()

    if word1List == word2List:
        print("Les deux mots sont des anagrammes")
    else:
        print("Les deux mots ne sont pas des anagrammes")

def contains_doubles(my_list):
    for value in my_list:
        repeat = my_list.count(value) > 1
        if repeat == False:
            pass
        else:
            return repeat
    return repeat


def best_grades(grade):
    notei = 0
    nombre_de_notes = 0

    for list in grades:
        for note in grades[list]:
            notei +=  note
            nombre_de_notes += 1
        grades[list] = notei / nombre_de_notes
        notei = 0
        nombre_de_notes = 0
       
    return (max(grades, key=grades.get)), max(grades.values())



def frequence(sentence):
    letterListe = [letter for letter in sentence if letter.isalpha()]
    letterListe.sort()
    letterListe2 = [letter for letter in letterListe if letterListe.count(letter) > 5 ]
    letterListe2 = sorted(letterListe2,key=letterListe2.count,reverse=True)
    # List en ordre decroissant
    letterListe3 = []
    for letter in letterListe2:
        letterListe3.append(letter)
        if letterListe3.count(letterListe3[letterListe3.index(letter)]) > 1:
            letterListe3.remove(letter)
    #lite avec seulement une lettre de chaque repetition
    print(letterListe3)


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
    print(best_grades(grades))

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
