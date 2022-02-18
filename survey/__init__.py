from otree.api import *

author = "Lars Wittrock"

doc = """
Post experiment survey after lying experiment
"""


class C(BaseConstants):
    NAME_IN_URL = 'FinalSurvey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Transition(Page):
    pass


class Beliefs(Page):
    pass


class Likert(Page):
    pass


class Controls(Page):
    pass


class FinalPage(Page):
    pass


page_sequence = [Transition, Beliefs, Likert, Controls, FinalPage]
