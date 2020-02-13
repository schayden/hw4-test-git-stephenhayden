import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code


#########################################
##### Name: Stephen Hayden      #####
##### Uniqname: schayden        #####
#########################################


## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)
    def test_1_queen(self):
        card = cards.Card(rank = 12)
        self.assertEqual(card.rank_name, "Queen")
    def test_2_clubs(self):
        card = cards.Card(suit = 1)
        self.assertEqual(card.suit_name, "Clubs")
    def test_3_str_method(self):
        card = cards.Card(suit = 3, rank = 13)
        self.assertEqual(cards.Card.__str__(card), "King of Spades")
    def test_4_52Deck(self):
        deck = cards.Deck()
        cards_in_deck = deck.cards
        self.assertEqual(len(deck.cards), 52)
    def test_5_deal_card(self):
        deck = cards.Deck()
        card = cards.Card()
        test_card = deck.deal_card()
        self.assertEqual(type(test_card), type(card))
    def test_6_pop_deck(self):
        deck = cards.Deck()
        deck_length_one = len(deck.cards)
        pop_card = deck.deal_card()
        deck_len_2 = len(deck.cards)
        length_difference = deck_length_one - deck_len_2
        self.assertEqual(deck_length_one - 1, deck_len_2)
        self.assertEqual(length_difference, 1)
    def test_7_replace_card(self):
        deck = cards.Deck()
        remove_card = deck.deal_card()
        deck_len_7_one = len(deck.cards)
        to_replace = deck.replace_card(remove_card)
        deck_len_problem_7_2 = len(deck.cards)
        self.assertEqual(deck_len_7_one +1, deck_len_problem_7_2)

    def test_8_replace_present_card(self):
        deck = cards.Deck()
        deck_len_problem_8_one = len(deck.cards)
        card = cards.Card(suit = 3, rank = 13)
        card_replace = deck.replace_card(card)
        deck_len_problem_8_two = len(deck.cards)
        self.assertEqual(deck_len_problem_8_one, deck_len_problem_8_two)

############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()