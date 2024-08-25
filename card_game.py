import random
from functools import total_ordering


@total_ordering
class Card:
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __lt__(self, other):
        self_rank = self.RANKS.index(self.rank)
        other_rank = other.RANKS.index(other.rank)
        if self_rank != other_rank:
            return self_rank < other_rank
        return self.SUITS.index(self.suit) < other.SUITS.index(other.suit)

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class DeckOfCards:
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self._cards)

    def deal_card(self):
        return self._cards.pop(0) if self._cards else None


class CardGame:
    def __init__(self):
        self.deck = DeckOfCards()

    def play(self):
        print("Nothing to play...")


class War(CardGame):
    def __init__(self):
        super().__init__()
        self.player1_hand = []
        self.player2_hand = []

    def play(self):
        self.player1_hand = self.__deal_hand()
        self.player2_hand = self.__deal_hand()
        self.__battle()

    def __deal_hand(self):
        return [self.deck.deal_card() for _ in range(5)]

    def __battle(self):
        player1_pile = []
        player2_pile = []
        player1_score = 0
        player2_score = 0
        ties = 0

        while self.player1_hand and self.player2_hand:
            card1 = self.player1_hand.pop()
            card2 = self.player2_hand.pop()
            print(f"{card1} vs {card2}")

            if card1 > card2:
                player1_pile.extend([card1, card2])
                player1_score += 1
                print(f"Player 1 wins with {card1}")
            elif card2 > card1:
                player2_pile.extend([card1, card2])
                player2_score += 1
                print(f"Player 2 wins with {card2}")
            else:
                ties += 1
                print("Tie! Both players draw a card and play again")

        print("------------------------------------------")
        print("Game over!")
        print("------------------------------------------")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")
        print(f"Ties: {ties}")
        print("==========================================")


### Example Usage


def main():
    war_game = War()
    war_game.play()


if __name__ == "__main__":
    main()
