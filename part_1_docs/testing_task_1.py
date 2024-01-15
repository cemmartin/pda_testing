#need to import the class Card

class CardGame:

  #it's fully missing a declaration of state!

  def check_for_ace(self, card):
    if card.value = 1: #should be ==. not =
      return True
    else #missing : after else
      return False
   
  #lines 15-18 should be indented more than they are; also this fails to address situations in which two cards are equal
  dif highest_card(self, card1 card2): #should be def not dif; also missing a comma between cards 1 and 2 
  if card1.value > card2.value:
    return card #should be card 1 not just card
  else:
    return card2
  

#if card_total is a method of CardGame then it needs to be indented (i.e. actually within the class CardGame)
def cards_total(self, cards): #this should be card not cards
  total #total needs to be set to = 0
  for card in cards: #this is currents meaningless as "cards" is not defined
    total += card.value
    return "You have a total of" + total #the return statement needs to be outside the loop