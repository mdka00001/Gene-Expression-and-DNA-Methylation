from itertools import combinations
import collections
import numpy as np
import statistics
import math
import pandas as pd

import scipy.stats as stats

def rank(x):
    """
    :param x: a list of values
    :return: ranking of the input list
    """

    

    
    x_s=sorted(x, reverse=True)
    x_r=x
    
    for i in x_s:
        
        counter=collections.Counter(x_s)

        avg=0
        if counter[i] > 1:
            list2=[k for k in range(len(x_s)) if x_s[k] == i]
            avg = sum(list2)/len(list2)
        else:
            avg = x_s.index(i)

        for j in range(0,len(x)):
            if i == x[j]:
                x_r[j] = avg

    return(x_r)
                
        
    


def pearson_correlation(x, y):
    """
    :param x: a list of values
    :param y: a list of values
    :return: Pearson correlation coefficient of X and Y
    """
    
    x_dev2=[]
    y_dev2=[]
    for i in x:
        x_temp=i-(sum(x)/len(y))
        x_dev2.append(x_temp)
    for i in y:
        y_temp=i-(sum(y)/len(y))
        y_dev2.append(y_temp)
    x_dev=[float(i) for i in x_dev2]
    y_dev=[float(i) for i in y_dev2]

    x_b=pd.DataFrame(x_dev)
    y_b=pd.DataFrame(y_dev)
    
    xx = x_b**2
    
    yy = y_b**2
    

    multiply = x_b * y_b
    rou= sum(multiply.to_numpy())/(math.sqrt(sum(xx.to_numpy()))*math.sqrt(sum(yy.to_numpy())))
    
    for i in rou:
        return(i)

    


def spearman_correlation(x, y):
    """
    :param x: a list of values
    :param y: a list of values
    :return: Spearman correlation coefficient of X and Y
    """
    coef, p = stats.spearmanr(x, y)

    return(coef)


def kendall_correlation(x, y):
    """
    :param x: a list of values
    :param y: a list of values
    :return: Kendall-B correlation coefficient of X and Y
    """
    c, p = stats.kendalltau(x, y)
    return(c)


class CorrelationMatrix(dict):
    """
    This class behaves like a dictionary, where the correlation between two elements 1 and 2 is accessible via
    cor_matrix[(element_1, element_2)] or cor_matrix[(element_2, element_1)] since the matrix is symmetrical.
    It also stores the row (or column) names of the input DataMatrix.
    """
    def __init__(self, data_matrix, method, rows):
        """
        :param data_matrix: a DataMatrix (see data_matrix.py)
        :param method: string specifying the correlation method, must be 'Pearson', 'Spearman' or 'Kendall'
        :param rows: True if the correlation matrix should be constructed for the rows, False if for the columns
        """
        # initialise the dictionary
        super().__init__(self)

        # if rows = True, then compute the correlation matrix for the row data
        if rows:
            data = data_matrix.get_rows()
            
        # if rows = False, then compute the correlation matrix for the column data
        else:
            data = data_matrix.get_columns()
            

        # sorted list of row names (or column names) in the input data matrix
        self.names = list(sorted(data.keys()))

        # compute the correlation between all pairs of rows (or columns)
        for name_1, name_2 in combinations(data.keys(), 2):
            # use the specified correlation method
            if method == 'Pearson':
                correlation = pearson_correlation(data[name_1], data[name_2])
            elif method == 'Spearman':
                correlation = spearman_correlation(data[name_1], data[name_2])
            elif method == 'Kendall':
                correlation = kendall_correlation(data[name_1], data[name_2])
            else:
                raise ValueError('The correlation method not supported must be either Pearson, Spearman or Kendall.')

            # add the correlation symmetrically
            self[(name_1, name_2)] = correlation
            self[(name_2, name_1)] = correlation
