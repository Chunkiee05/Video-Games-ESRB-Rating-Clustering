import numpy as np
import pandas as pd


def Tscore(diff):
    mean = diff.agg('mean')
    std = diff.agg('std')
    Tscore = (mean - 0)/(std/(np.sqrt(diff.shape[0])))
    return Tscore