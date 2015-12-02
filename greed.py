"""
= Playing Greed

Greed is a dice game played among 2 or more players, using 5
six-sided dice.

== Playing Greed

Each player takes a turn consisting of one or more rolls of the dice.
On the first roll of the game, a player rolls all five dice which are
scored according to the following:

  Three 1's => 1000 points
  Three 6's =>  600 points
  Three 5's =>  500 points
  Three 4's =>  400 points
  Three 3's =>  300 points
  Three 2's =>  200 points
  One   1   =>  100 points
  One   5   =>   50 points

A single die can only be counted once in each roll.  For example,
a "5" can only count as part of a triplet (contributing to the 500
points) or as a single 50 points, but not both in the same roll.

Example Scoring

   Throw       Score
   ---------   ------------------
   5 1 3 4 1   50 + 2 * 100 = 250
   1 1 1 3 1   1000 + 100 = 1100
   2 4 4 5 4   400 + 50 = 450

The dice not contributing to the score are called the non-scoring
dice.  "3" and "4" are non-scoring dice in the first example.  "3" is
a non-scoring die in the second, and "2" is a non-score die in the
final example.

After a player rolls and the score is calculated, the scoring dice are
removed and the player has the option of rolling again using only the
non-scoring dice. If all of the thrown dice are scoring, then the
player may roll all 5 dice in the next roll.

The player may continue to roll as long as each roll scores points. If
a roll has zero points, then the player loses not only their turn, but
also accumulated score for that turn. If a player decides to stop
rolling before rolling a zero-point roll, then the accumulated points
for the turn is added to his total score.

== Getting "In The Game"

Before a player is allowed to accumulate points, they must get at
least 300 points in a single turn. Once they have achieved 300 points
in a single turn, the points earned in that turn and each following
turn will be counted toward their total score.

== End Game

Once a player reaches 3000 (or more) points, the game enters the final
round where each of the other players gets one more turn. The winner
is the player with the highest score after the final round.

== References

Greed is described on Wikipedia at
http://en.wikipedia.org/wiki/Greed_(dice_game), however the rules are
a bit different from the rules given here.
"""

import random


class Player:
    pass


class Game:
    pass


class DiceSet:
    def __init__(self):
        self._values = []

    @property
    def values(self):
        return self._values

    def roll(self, n):
        self._values = []
        for _ in range(n):
            self._values.append(random.randint(1, 6))


def score(dice):
    # * A set of three ones is 1000 points
    # * A set of three numbers (other than ones) is worth 100 times the
    #   number. (e.g. three fives is 500 points).
    # * A one (that is not part of a set of three) is worth 100 points.
    # * A five (that is not part of a set of three) is worth 50 points.
    return_values = []
    score = 0
    tracker = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # Count up all of the dice occurrances
    for num in dice:
        tracker[num] += 1

    # Handle triplets
    for key in tracker:
        if key == 1 and tracker[key] >= 3:
            score += 1000
            tracker[1] -= 3
        elif tracker[key] >= 3:
            score += key*100
            tracker[key] -= 3

    # Handle individual ones and fives
    score += 100 * tracker[1]
    tracker[1] -= tracker[1]
    score += 50 * tracker[5]
    tracker[5] -= tracker[5]

    # Return both the score and the dict of non-contributing dice
    return_values.extend([score, tracker])
    return return_values
