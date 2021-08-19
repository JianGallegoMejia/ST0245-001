import pandas as pd
import glob
import os

class Cattle:

    def buildMatrix(self):
        path = os.getcwd()
        csv_files = glob.glob(os.path.join(path, "*.csv"))
        
        for f in csv_files:
            df = pd.read_csv(f)
            print('Location:', f)
            print('Content:')
            print(df)
            print()

class main():
    cattle = Cattle()
    cattle.buildMatrix()
