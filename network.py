import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
class CorrelationNetwork:
    def __init__(self, correlation_matrix, threshold):
        """
        Constructs a co-expression network from a correlation matrix by adding edges between nodes with absolute
        correlation bigger than the given threshold.
        :param correlation_matrix: a CorrelationMatrix (see correlation.py)
        :param threshold: a float between 0 and 1
        """
        

        val = []
        a=[]
        b=[]

        
        for i in correlation_matrix:

            if abs(correlation_matrix[i]) >= threshold:
                
                x=i
                val.append(correlation_matrix[i])
                a.append(i)
        for i in a:
            for j in i:
                b.append(j)
        
        lim=int(len(b)/2)

        first = b[0:lim]
        second = b[lim:int(len(b)+1)]

        val2=[]
        for i in val:
            y=round(i, 2)
            val2.append(y)

        
        df1 = pd.DataFrame(first)
        df2 = pd.DataFrame(val2)
        df3 = pd.DataFrame(second)
        self.df=pd.concat([df1, df2, df3], axis=1)
        


    def to_sif(self, file_path):
        """
        Write the network into a simple interaction file (SIF).
        Column 0: label of the source node
        Column 1: interaction type
        Columns 2+: label of target node(s)
        :param file_path: path to the output file
        """
        with open (file_path, 'w') as sif:
            for row in self.df.index:
                for col in self.df.columns:
                    sif.write('{}\t{}\t{}'.format(row, self.df[col][row], col))
