"""
CHALLENGE PART 3 of 3: Putting It All Together

Complete player.py and tournament.py first. This file ties them all
together into a program you can actually run: a 4-player single
elimination tournament for The Trendiest's game night.

Run it with:
    python main.py
"""

from player import Player
from tournament import Tournament


def main():
    players = [Player("Priya"), Player("Sam"), Player("Mia"), Player("Leo")]
    tournament = Tournament(players)

    print("The Trendiest Game Night Tournament!")
    print("Round 1: Priya vs Sam, Mia vs Leo")

    # TODO: call tournament.play_round(...) with a list of 4 scores (one
    # per player, in the order they appear in `players` above) to decide
    # the semi-final results. Then print tournament.players to see who
    # advanced.

    print("Round 2 (final): the two round 1 winners face off")

    # TODO: call tournament.play_round(...) again with a list of 2 scores
    # (one per remaining player) to decide the final.

    # TODO: once tournament.is_finished() is True, print the champion's
    # name using tournament.get_champion(), and call
    # tournament.save_results() to write results.csv.


if __name__ == "__main__":
    main()
