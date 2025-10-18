import pandas as pd

arquivo = pd.read_csv('/workspaces/Machine-Learning/01-Fundamentos/wine_dataset.csv')

arquivo.head()

arquivo['style'] = arquivo['style'].replace['red', 0]
arquivo['style'] = arquivo['style'].replace['white', 1]