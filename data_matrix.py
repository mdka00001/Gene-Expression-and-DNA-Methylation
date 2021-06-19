import pandas as pd
import csv
from scipy.stats import shapiro
class DataMatrix:
    def __init__(self, file_path):
        """
        :param file_path: path to the input matrix file
        """
        self.file_path = file_path
        
    def read_data(self):
        """
        Reads data from a given matrix file, where the first line gives the names of the columns and the first column
        gives the names of the rows. Removes rows with empty or non-numerical values and merges rows with the same
        name into one.
        """
        with open(self.file_path, "r") as handle:
            table=csv.reader(handle, delimiter="\t")
            df1=pd.DataFrame(table)
            new_header = df1.iloc[0] #grab the first row for the header
            df = df1[1:] #take the data less the header row
            df.columns = new_header #set the header row as the df header
           
            df2 = df.iloc[:,1:]

            
            df3 = df1[0]
            df3.columns=["index"]

            df_final=pd.concat([df3,df2], axis=1)
            df_final1=df_final.iloc[1: , :]
            
            
            df5=df_final1.set_index([0])
            
            mod_df=df5.dropna()
            mod_df.drop_duplicates()
            
            
            mod=pd.DataFrame()
            for i in mod_df.columns:
                mod_new=mod_df[mod_df[i].apply(lambda x: str(x).isdigit())]
                mod=pd.concat([mod, mod_new], axis=0)

            
            new_df=mod.drop_duplicates()

            X_replace = new_df.replace('',0, regex=True)
            mod_f=X_replace.astype(float)
            new_df_T=mod_f.T
            avg=pd.DataFrame()
            for index1 in new_df_T:
                if index1==index1:
                
                    new_df_2 = new_df_T[[index1, index1]].mean(axis=1)
                    new_df_3=pd.DataFrame(new_df_2)
                    
                    new_df_3.columns=[index1]

                    avg=pd.concat([avg, new_df_3], axis=1)
            avg_T=avg.T

            self.final=avg_T.drop_duplicates()

            

    def get_rows(self):
        """
        :return: dictionary with keys = row names, values = list of row values
        """
        rows = {}
        for i in self.final.T:
            
            
            rows[i] = self.final.T[i].to_numpy().tolist()
        return rows
        
        

    def get_columns(self):
        """
        :return: dictionary with keys = column names, values = list of column values
        """
        
        cols = {}
        for i in self.final:
            cols[i] = self.final[i].to_numpy().tolist()
        return cols
            
        

        
        

    def not_normal_distributed(self, alpha, rows):
        """
        Uses the Shapiro-Wilk test to compute all rows (or columns) that are not normally distributed.
        :param alpha: significance threshold
        :param rows: True if the Shapiro-Wilk p-values should be computed for the rows, False if for the columns
        :return: dictionary with keys = row/columns names, values = Shapiro-Wilk p-value
        """
    
        shapiro_dict=dict()
        if rows == 0:
            for index in self.final:
                stat, p = shapiro(self.final[index])
                if p<alpha:
                    shapiro_dict[index]=p
        elif rows == 1:
            for index in self.final.T:
                stat, p = shapiro(self.final.T[index])
                if p<alpha:
                    shapiro_dict[index]=p
        print(shapiro_dict)

    def to_tsv(self, file_path):
        """
        Writes the processed matrix into a tab-separated file, with the same column order as the input matrix and
        the rows in lexicographical order.
        :param file_path: path to the output file
        """
        x_sorted=self.final.index.sortlevel()
        x_df=pd.DataFrame(x_sorted)
        
        x_df_2=x_df.drop([1])
        new=x_df_2.to_numpy()

        y_sorted=pd.DataFrame()
        for i in new:
            spd=self.final.T[i]
            y_sorted=pd.concat([y_sorted, spd], axis=0)
 
        y_sorted.T.to_csv(file_path, sep=" ")
        
