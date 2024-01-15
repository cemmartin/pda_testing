class CardGame:

  def __init__(self, name):
    self.name = name
    self.cards = []

#checks how many cards are in the deck
  def check_number_of_cards(self):
    return len(self.cards)

#adds a card to the decl
  def add_card_to_deck(self, card):
    self.cards.append(card)

  def check_for_ace(self, card):
    if card.value == 1: 
      return True
    else:
      return False
    

  def highest_card(self, card1, card2):  
    if card1.value > card2.value:
      return card1
    elif card1.value < card2.value:
      return card2
    else:
      return "It's a tie!"
    

  def cards_total(self):
    total = 0

    for card in self.cards:
      total += card.value

    return f"You have a total of {total}"