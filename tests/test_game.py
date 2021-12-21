import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        
        #on verifie le type du grid qui doit etre une liste
        self.assertIsInstance(grid, list, msg="grid doit être une liste")
        
        #on regarde la taille qui est 9
        self.assertEqual(len(grid), 9, msg="la liste a une taille de 9")

        #on verifie si tous lettre son bon et majuscule
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_game_if_empty(self):
        new_game = Game()
        self.assertFalse(new_game.is_valid(""))

   
    def test_game_is_valid(self):
        new_game = Game()
        new_game.grid = str("OQUWRBAZE")
        word = "BAROQUE"

        #on verifie si un mot est valide
        self.assertTrue(new_game.is_valid(word))

        self.assertTrue(new_game.is_valid("ARE"))

        #on test si grid n'a pas été modifier
        self.assertEqual(new_game.grid, str("OQUWRBAZE"))


    def test_game_is_invalid(self):
        new_game = Game()
        new_game.grid = str("OQUWRBAZE")
        self.assertFalse(new_game.is_valid("QUEROBA"))

        self.assertFalse(new_game.is_valid("THERE"))

         #on test si grid n'a pas été modifier
        self.assertEqual(new_game.grid, str("OQUWRBAZE"))

