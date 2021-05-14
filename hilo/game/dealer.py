import random

class Dealer:
    """A code template for a person who throws the dice for the game. The responsibility of 
    this class of objects is to throw the dice, tally the points, 
    and check if its possible to throw again.
    
    Attributes:
        dice (list): Lists the five dice that were thrown.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Thrower): an instance of Thrower.
        """
        
        
        
    def can_throw(self, score):
        """Determines whether or not the Thrower can throw again according to 
        the rules. 

        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            boolean: True if the list of dice has at least a five, or a one, or 
            the number of throws is zero; false if otherwise.
        """

        return (score > 0)

    def get_points(self, guess):
        """Calculates the total number of points for the current throw. Fives 
        are worth 50 points. Ones are worth 100 points. 

        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            number: The total points for the current throw.
        """
        score = 0
        if self.new_card < self.next_card:
            if guess == "h": 
                score += 100
            else:
                score -= 75
        else:
            if guess == "l":
                score += 100
            else:
                score -= 75
        return score

    def throw_card(self):
        """Throws the dice by randomly generating five new values. 

        Args: 
            self (Thrower): An instance of Thrower.
        """
        
        self.card = [*range(1,14)]

        self.new_card_index = (random.randint(0,12))

        self.new_card = self.card[self.new_card_index]

        self.card.pop(self.new_card_index)

        self.next_card = self.card[random.randint(0,11)]