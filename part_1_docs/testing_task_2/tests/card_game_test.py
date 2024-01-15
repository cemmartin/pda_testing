import unittest
from src.card_game import CardGame
from src.card import Card

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame("War")
        self.card_1 = Card("ace of spades", 1, "spades", "black")
        self.card_2 = Card("queen of diamonds", 12, "diamonds", "black")
        self.card_3 = Card("2 of hearts", 2, "hearts", "red")
        self.card_4 = Card("2 of diamonds", 2, "diamonds", "black")
        

    def test_count_cards(self):
        self.assertEqual([], self.card_game.cards)

    
    def test_cards_in_deck(self):
        self.card_game.add_card_to_deck(self.card_1)
        self.card_game.add_card_to_deck(self.card_3)
        self.assertEqual(2, self.card_game.check_number_of_cards())


#The commented out bit are parts of the test I tried which weren't passing
    def test_check_card_is_ace(self):
        self.card_game.add_card_to_deck(self.card_1)
        self.card_game.check_for_ace(self.card_1)
        # self.assertTrue(self.card_1.value)
        self.assertTrue(self.card_game.check_for_ace(self.card_1))
        # self.assertEqual(True, self.card_1.value)

    def test_check_card_is_not_ace(self):
        self.card_game.add_card_to_deck(self.card_2)
        self.card_game.check_for_ace(self.card_2)
        # self.assertEqual(False, self.card_2.value)
        self.assertFalse(self.card_game.check_for_ace(self.card_2))

    def test_check_card_is_higher(self):
        self.assertEqual(self.card_2, self.card_game.highest_card(self.card_2, self.card_1))
        self.assertEqual(self.card_3, self.card_game.highest_card(self.card_1, self.card_3))

    def test_for_tie(self):
        self.assertEqual("It's a tie!", self.card_game.highest_card(self.card_3, self.card_4))
        #the line below should fail
        # self.assertEqual("It's a tiedfbdfdv!", self.card_game.highest_card(self.card_3, self.card_4))

    def test_total(self):
        self.card_game.add_card_to_deck(self.card_1)
        self.card_game.add_card_to_deck(self.card_2)
        self.assertEqual(f"You have a total of 13", self.card_game.cards_total())

