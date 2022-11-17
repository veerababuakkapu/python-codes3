import pandas as pd
#lst = ['Geeks','for','Geeks','is','portal','for','geeks']
#df = pd.DataFrame(lst)
#print(df)

#data = {'Name':['tom','nick','krish','jack'],'Age':[20,21,22,23]}
#df = pd.DataFrame(data)
#data = pd.read_csv(r'C:\pythoncode\Giants.csv')
#df = pd.DataFrame(data, columns=['CEO','Established'])
#print(df)

import pandas as pd
data1 = pd.read_excel(r'C:\pythoncode\Companies.xlsx')
df = pd.DataFrame(data1, columns=['CEO'])
print(df)
