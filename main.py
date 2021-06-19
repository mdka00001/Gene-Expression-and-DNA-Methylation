from data_matrix import DataMatrix
from network import CorrelationNetwork
from correlation import CorrelationMatrix


def exercise_1():
    a_m = DataMatrix(r"D:\BIII\Assignment_8\BI3_assignment_8_supplement\expression.tsv")
    b_m = a_m.read_data()
    c_m = a_m.get_rows()
    d_m = a_m.not_normal_distributed(0.05, 1)
    a_m.to_tsv("D:\BIII\Assignment_8\BI3_assignment_8_supplement\Karim_Elamaldeniya_expression.tsv")

    a_e = DataMatrix(r"D:\BIII\Assignment_8\BI3_assignment_8_supplement\methylation.tsv")
    b_e = a_e.read_data()
    c_e = a_e.get_rows()
    d_e = a_e.not_normal_distributed(0.05, 1)
    a_e.to_tsv("D:\BIII\Assignment_8\BI3_assignment_8_supplement\Karim_Elamaldeniya_methylation.tsv")

def exercise_3():
    a_1=DataMatrix(r"D:\BIII\Assignment_8\BI3_assignment_8_supplement\expression.tsv")
    a_2=a_1.read_data()
    aa_1 = CorrelationMatrix(a_1, "Spearman", True)
    cc_1 = CorrelationNetwork(aa_1, 0.75)

    cc_1.to_sif("D:\BIII\Assignment_8\BI3_assignment_8_supplement\Karim_Elamaldeniya_expression_Spearman.sif")

    
#Please change the input variables for different outputs

# only execute the following if this module is the entry point of the program, not when it is imported into another file
if __name__ == '__main__':
    exercise_1()
    exercise_3()
