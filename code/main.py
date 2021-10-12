import pandas as pd
import glob
import os
import numpy as np
from scipy import interpolate

class Cattle:

    matriz = []

    def buildMatrix(self):
        path = os.getcwd()
        csv_files = glob.glob(os.path.join(path, "*.csv"))

        for f in csv_files:
            df = pd.read_csv(f)
            print('Location:', f)
            print('Content:')
            print(df)
            print()
            self.matriz=df.to_numpy()
            
    def interpolate(self):
        print(self.matriz.shape)
        y,x = np.where(self.matriz!=0)      
        f = interpolate.interp2d(x,y,self.matriz[self.matriz!=0],kind='linear')
        X = np.arange(len(self.matriz))
        print(f(X,X)) 

    def generateFile(self):
        np.savetxt('myfile.csv', self.matriz, delimiter=',')



class main():
    cattle = Cattle()
    cattle.buildMatrix()
    cattle.generateFile()
    cattle.interpolate()
