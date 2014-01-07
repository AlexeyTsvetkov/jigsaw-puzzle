# -*-coding: utf-8 -*-

import math
import numpy as np
import relations


def _avg_difference(npiece, side):
    if side == relations.LEFT:
        difference = npiece[:, 0] - npiece[:, 1]
    elif side == relations.RIGHT:
        difference = npiece[:, -1] - npiece[:, -2]
    elif side == relations.UP:
        difference = npiece[0, :] - npiece[1, :]
    else:
        difference = npiece[-1, :] - npiece[-2, :]

    return sum(difference)/float(len(difference))


def _gradient(pieces_difference, average_side_difference):
    grad = pieces_difference - average_side_difference
    grad_t = np.transpose(grad)
    cov = np.cov(grad_t)
    try:
        cov_inv = np.linalg.inv(cov)
    except np.linalg.LinAlgError as e:
        cov_inv = np.ones((3, 3))

    return grad.dot(cov_inv).dot(grad_t)


def mgc(np1, np2, relation):
    if relation == relations.LEFT:
        grad_12 = _gradient(np2[:, 0] - np1[:, -1], _avg_difference(np1, relations.RIGHT))
        grad_21 = _gradient(np1[:, -1] - np2[:, 0], _avg_difference(np2, relations.LEFT))
    else:
        grad_12 = _gradient(np2[0, :] - np1[-1, :], _avg_difference(np1, relations.DOWN))
        grad_21 = _gradient(np1[-1, :] - np2[0, :], _avg_difference(np2, relations.UP))

    return np.sum(grad_12 + grad_21)


def rgb(np1, np2, relation):
    if relation == relations.LEFT:
        difference = np1[:, -1] - np2[:, 0]
    else:
        difference = np1[-1, :] - np2[0, :]

    exponent = np.vectorize(lambda x: math.pow(x, 2))
    dissimilarity = np.sum(exponent(difference))
    return math.sqrt(dissimilarity)


def rgb_mgc(*args):
    return rgb(*args)*mgc(*args)