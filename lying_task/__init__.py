from otree.api import *


author = 'Lars Wittrock'

doc = """
Main Lying Task
"""


class C(BaseConstants):
    NAME_IN_URL = 'AdditionalPayoff'
    PLAYERS_PER_GROUP = 2
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


class Roll1(Page):
    pass


class WaitPage1(WaitPage):
    pass


class Results1(Page):
    pass


class Roll2(Page):
    pass


class WaitPage2(WaitPage):
    pass


class Results2(Page):
    pass


page_sequence = [Instruction, InstructionTest, InstructionFeedback, WaitPage1,
                 Roll1, Results1, WaitPage2, Roll2, Results2]
