from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'ProlificUsage'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Prolific_use(Page):
    pass


class Demographics(WaitPage):
    pass


class Transition(WaitPage):
    pass


page_sequence = [Prolific_use, Demographics, Transition]
