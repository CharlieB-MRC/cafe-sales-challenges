"""
AUTOMATED TESTS for the tournament_system project.

You don't need to edit this file! Run it with:
    pytest
from inside this tournament_system/ folder, once you've written some code
in player.py and tournament.py. Each test checks one small piece of
behaviour and will tell you exactly what passed (.) or failed (F).

Tip: work through the tests from top to bottom — later tests depend on
earlier code working correctly.
"""

import os

import pytest

from player import Player
from tournament import Tournament


def test_player_starts_with_no_scores():
    p = Player("Priya")
    assert p.name == "Priya"
    assert p.scores == []


def test_player_add_round_score():
    p = Player("Priya")
    p.add_round_score(42)
    p.add_round_score(37)
    assert p.scores == [42, 37]


def test_player_total_score():
    p = Player("Priya")
    p.add_round_score(42)
    p.add_round_score(37)
    assert p.total_score() == 79


@pytest.fixture
def four_players():
    return [Player("Priya"), Player("Sam"), Player("Mia"), Player("Leo")]


def test_tournament_starts_with_all_players(four_players):
    t = Tournament(four_players)
    assert len(t.players) == 4
    assert t.round_number == 1


def test_play_round_advances_higher_scorers(four_players):
    t = Tournament(four_players)
    t.play_round([42, 37, 50, 25])  # Priya beats Sam, Mia beats Leo
    names = [p.name for p in t.players]
    assert names == ["Priya", "Mia"]


def test_play_round_records_match_history(four_players):
    t = Tournament(four_players)
    t.play_round([42, 37, 50, 25])
    assert len(t.match_history) == 2
    first_match = t.match_history[0]
    assert first_match["winner"] == "Priya"


def test_play_round_increments_round_number(four_players):
    t = Tournament(four_players)
    t.play_round([42, 37, 50, 25])
    assert t.round_number == 2


def test_is_finished_and_get_champion(four_players):
    t = Tournament(four_players)
    t.play_round([42, 37, 50, 25])  # Priya, Mia advance
    assert t.is_finished() is False
    assert t.get_champion() is None

    t.play_round([60, 55])  # Priya beats Mia
    assert t.is_finished() is True
    assert t.get_champion().name == "Priya"


def test_save_results_creates_csv(tmp_path, four_players):
    t = Tournament(four_players)
    t.play_round([42, 37, 50, 25])
    t.play_round([60, 55])

    csv_path = tmp_path / "results.csv"
    t.save_results(str(csv_path))

    assert os.path.exists(csv_path)
    with open(csv_path) as f:
        contents = f.read()
    assert "Priya" in contents
    assert "winner" in contents
