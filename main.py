# Chuong 5
from AcitivitySelection import AcitivitySelection
from FloydWarshall import Warshall, Floyd
from FractionalKnapsack import FractionalKnapsack
from HuffmanCode import HuffmanCode
from Knapsack import KnapsackUnique, KnapsackUnlimited
from LongestCommonSubsequence import LongestCommonSubsequence
from MatrixChainMultiplication import MatrixChainMultiplication
# Chuong 6
from GeneratePermutation import GeneratePermutation
from JobAssignment import JobAssignment
from KnightTour import KnightTour
from nQueensPuzzle import nQueensPuzzle
from SubsetSum import SubsetSum
# Chuong 8
from nQueensPuzzle import nQueensPuzzle
from BinPacking import BinPacking
from Schedule import Schedule




menu_options = {
    1: 'AcitivitySelection',
    2: 'Warshall',
    3: 'Floyd',
    4: 'FractionalKnapsack',
    5: 'HuffmanCode',
    6: 'KnapsackUnique',
    7: 'KnapsackUnlimited',
    8: 'LongestCommonSubsequence',
    9: 'MatrixChainMultiplication',
    10: 'GeneratePermutation',
    11: 'JobAssignment',
    12: 'KnightTour',
    13: 'nQueensPuzzle',
    14: 'SubsetSum',
    15: 'nQueensPuzzle',
    16: 'BinPacking',
    17: 'Schedule',
}

def print_menu():
    print("="*10)
    print('    0 -- Exit')
    for key in menu_options.keys():
        print ("    " + str(key), '--', menu_options[key] )

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('[+] Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option in menu_options:
            print("_"*10)
            print(menu_options[option])
            globals()[menu_options[option]]()
            input("[.] Press enter key to continue!")
        elif option == 0:
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')