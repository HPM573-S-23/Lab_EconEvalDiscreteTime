from enum import Enum

import numpy as np

import InputData as Data


class Therapies(Enum):
    """ mono vs. combination therapy """
    MONO = 0
    COMBO = 1


class Parameters:
    def __init__(self, therapy):

        # selected therapy
        self.therapy = therapy

        # initial health state
        self.initialHealthState = Data.HealthStates.CD4_200to500

        # annual treatment cost
        if self.therapy == Therapies.MONO:
            self.annualTreatmentCost = Data.Zidovudine_COST
        else:
            self.annualTreatmentCost = Data.Zidovudine_COST + Data.Lamivudine_COST

        # transition probability matrix of the selected therapy
        self.probMatrix = []

        # calculate transition probabilities between hiv states
        if self.therapy == Therapies.MONO:
            # calculate transition probability matrix for the mono therapy
            self.probMatrix = get_prob_matrix_mono(trans_matrix=Data.TRANS_MATRIX)

        elif self.therapy == Therapies.COMBO:
            # calculate transition probability matrix for the combination therapy
            self.probMatrix = get_prob_matrix_combo(
                prob_matrix_mono=get_prob_matrix_mono(trans_matrix=Data.TRANS_MATRIX),
                combo_rr=Data.TREATMENT_RR)

        # annual state costs and utilities
        self.annualStateCosts = Data.ANNUAL_STATE_COST
        self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY

        # discount rate
        self.discountRate = Data.DISCOUNT


def get_prob_matrix_mono(trans_matrix):
    """
    :param trans_matrix: transition matrix containing counts of transitions between states
    :return: transition probability matrix
    """

    # initialize transition probability matrix
    trans_prob_matrix = []

    # for each row in the transition matrix
    for row in trans_matrix:
        # calculate the transition probabilities
        prob_row = np.array(row)/sum(row)
        # add this row of transition probabilities to the transition probability matrix
        trans_prob_matrix.append(prob_row)

    return trans_prob_matrix


def get_prob_matrix_combo(prob_matrix_mono, combo_rr):
    """
    :param prob_matrix_mono: (list of lists) transition probability matrix under mono therapy
    :param combo_rr: relative risk of the combination treatment
    :returns (list of lists) transition probability matrix under combination therapy """

    # create an empty list of lists
    matrix_combo = []
    for row in prob_matrix_mono:
        matrix_combo.append(np.zeros(len(row)))  # adding a row [0, 0, 0, 0]

    # populate the combo matrix
    # calculate the effect of combo-therapy on non-diagonal elements


    # diagonal elements are calculated to make sure the sum of each row is 1


    return matrix_combo


# # tests
# matrix_mono = get_prob_matrix_mono(Data.TRANS_MATRIX)
# matrix_combo = get_prob_matrix_combo(matrix_mono, Data.TREATMENT_RR)
#
# print(matrix_mono)
# print(matrix_combo)
