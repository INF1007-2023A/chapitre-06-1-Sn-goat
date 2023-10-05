#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order():
    values_input = input("Entrez une liste de valeur: ")
    values = values_input.split(",") 
    newList_str = [i for i in values if '"' in i ]
    newList_int_flot = [i for i in  values if '"' not in i ]
    newList_float = [i for i in newList_int_flot if float(i) % 1 != 0]
    newList_int = [i for i in newList_int_flot if float(i) % 1 == 0]
    print(newList_int + newList_float + newList_str)


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
    print("Is my liste contains doubles?: " + str(len(set(my_list)) !=  len(my_list)))


def best_grades(grades):
    for list in grades:
        grades[list] =  sum(grades[list])/ len(grades[list])
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

    name = input("Quel est le nom de votre recette?\n")
    ingredient = input("Entrer la liste d'ingrédients? Séparer les ingrédiants par une ,\n")
    listeIngredient = ingredient.split(",")

    return {name: listeIngredient}


def print_recipe(listIngredients) -> None:
    name = input("Quel est le nom de votre recette?\n")

    if name in listIngredients:
        print(listIngredients[name])
    else:
        print("Cette recette n'est pas dans le livre!")
        print_recipe(listIngredients)


def main() -> None:
   
    order()
    
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    contains_doubles(my_list)

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
