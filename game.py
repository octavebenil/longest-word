import string
import random
import requests

class Game():
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for i in range(9)]
    
    def is_valid(self, word):

        #on regarde si word est vide
        if word == "":
            return False

       #on regarde les mots données si c'est dans notre grille
        for letter in word:
            if self.grid.count(letter) == 0:
                #lettre qui n'est pas dans notre grille
                return False

        #on verifie si le mot est dans le dictionnaire anglais et francais
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
