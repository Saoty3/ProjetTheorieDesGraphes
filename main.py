import pandas as pd
from Function import *

matrice = txt_to_matrice(1)
df = pd.DataFrame(matrice)
print("Matrice initial : \n",df)

floyd_warshall(matrice)
new_df = pd.DataFrame(matrice)
print("\nMatrice amélioré : \n",new_df)