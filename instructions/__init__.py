from otree.api import *
import random

author = "Lars Wittrock"

doc = """
Instructions + Test for Lying Task
Separate to allow for grouping by arrival time in main app
"""

""" Do the treatment randomization in this app. save variables in participant vars """


class C(BaseConstants):

    # From Otree
    NAME_IN_URL = 'Instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # test questions
    test1_label = '1. ...?'
    test1_choices = []

    test2_label = '2. ...?'
    test2_choices = []

    test3_label = '3. ...?'
    test3_choices = []

    test4_label = '4. ...?'
    test4_choices = []

    test_questions_solution = [1, 1, 1, 1]
    test_questions_required = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Variables for test questions
    test1 = models.IntegerField(doc='Test question 1',
                                label=C.test1_label,
                                choices=C.test1_choices,
                                widget=widgets.RadioSelect)
    test2 = models.IntegerField(doc='Test question 2',
                                label=C.test2_label,
                                choices=C.test2_choices,
                                widget=widgets.RadioSelect)
    test3 = models.IntegerField(doc='Test question 3',
                                label=C.test3_label,
                                choices=C.test3_choices,
                                widget=widgets.RadioSelect)
    test4 = models.IntegerField(doc='Test question 4',
                                label=C.test4_label,
                                choices=C.test4_choices,
                                widget=widgets.RadioSelect)

    test_correct = models.IntegerField(doc='Number of correct test questions')


def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        participant = player.participant
        participant.treat = random.randint(1, 4)  # equal numbers for all treatments. to be adjusted later


# PAGES
class Transition(Page):
    pass


class Instruction(Page):
    form_model = 'player'
    form_fields = ['test1', 'test2', 'test3', 'test4']

    # Correct answers for test questions
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.test1 == C.test_questions_solution[0]:
            test1_correct = 1
        else:
            test1_correct = 0

        if player.test2 == C.test_questions_solution[1]:
            test2_correct = 1
        else:
            test2_correct = 0

        if player.test3 == C.test_questions_solution[2]:
            test3_correct = 1
        else:
            test3_correct = 0

        if player.test4 == C.test_questions_solution[3]:
            test4_correct = 1
        else:
            test4_correct = 0

        player.test_correct = test1_correct + test2_correct + test3_correct + test4_correct


class InstructionFeedback(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # Returns correct solution for each question
        test1_solution = C.test1_choices[C.test_questions_solution[0] - 1][1]
        test2_solution = C.test2_choices[C.test_questions_solution[1] - 1][1]
        test3_solution = C.test3_choices[C.test_questions_solution[2] - 1][1]
        test4_solution = C.test4_choices[C.test_questions_solution[3] - 1][1]

        return {
            'test1_solution': test1_solution,
            'test2_solution': test2_solution,
            'test3_solution': test3_solution,
            'test4_solution': test4_solution
        }


page_sequence = [Transition, Instruction, InstructionFeedback]
