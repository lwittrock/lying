from otree.api import *


author = 'Lars Wittrock'

doc = """
Main Lying Task
"""


comments = """

group_by_arrival_time, works only if waitpage is first in page sequence. maybe make instructions separate app?

wait page timeouts

wait page customization are possible

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
class WaitPageStart(WaitPage):
    pass


class Roll1(Page):
    pass


class WaitPage1(WaitPage):
    title_text = "This is a custom wait page title"
    body_text = "This is a custom body text on the wait page"


class Results1(Page):
    pass


class Roll2(Page):
    pass


class WaitPage2(WaitPage):
    title_text = "This is a custom wait page title"
    body_text = "This is a custom body text on the wait page"


class Results2(Page):
    pass


page_sequence = [WaitPageStart, Roll1, WaitPage1, Results1, Roll2, WaitPage2, Results2]
