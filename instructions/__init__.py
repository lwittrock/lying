from otree.api import *

author = "Lars Wittrock"

doc = """
Instructions + Test for Lying Task
Separate to allow for grouping by arrival time in main app
"""


class C(BaseConstants):
    NAME_IN_URL = 'Instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Instruction(Page):
    pass


class InstructionTest(Page):
    pass


class InstructionFeedback(Page):
    pass


page_sequence = [Instruction, InstructionTest, InstructionFeedback]
