'''
project 4
'''
# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-10-10 23:05:55"
__modifytime__ = "2014-10-10 23:05:57"

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    '''
    build_scoring_matrix
    '''
    scoring_matrix = {}
    for letter_l in alphabet:
        scoring_matrix[letter_l] = {}
        for letter_r in alphabet:
            if letter_l == '-' or letter_r == '-':
                scoring_matrix[letter_l][letter_r] = dash_score
            elif letter_l == letter_r:
                scoring_matrix[letter_l][letter_r] = diag_score
            else:
                scoring_matrix[letter_l][letter_r] = off_diag_score
    return scoring_matrix


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    '''
    compute_alignment_matrix
    '''
    seq = []
    seq[0] = []
    seq[0] = None * 