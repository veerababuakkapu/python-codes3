"""import pandas as pd
df = pd.DataFrame()
print(df)"""

import pandas as pd
data = {'Country': ['Belgium','India','Brazil'],
'Capital':['Brussels','New Delhi','Brasilla'],
'population':[11190346,1303171035,207847528]}
df = pd.DataFrame(data,columns=['Country', 'Capital','population'])
print(df)
