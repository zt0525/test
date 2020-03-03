import tabula
import pandas as pd
import re
dfList = tabula.read_pdf('sample_wa_original_Redacted.pdf',pages = 'all',stream = True)
dfColumn = dfList[0]
dfContent = dfList[1]
Col_temp = dfColumn.loc[0].reset_index()
ColList = []
for x in Col_temp.iterrows():
    ColList.append(x[1]['index'] +' ' + x[1][0])
ColList[2] = 'Unit Value'
ColList = ['Fund/Asset'] + ColList
dfContentNew = dfContent.T.reset_index().T.reset_index(drop=True)
dfContentNew.columns = ColList
output = dfContentNew.set_index('Fund/Asset')
output['Number of Units'] = output['Number of Units'].apply(lambda x: re.sub(',','',x))
output['Number of Units']  = pd.to_numeric(output['Number of Units'])

output['Unit Price'] = output['Unit Price'].apply(lambda x: re.sub('p','',x))
output['Unit Price'] = pd.to_numeric(output['Unit Price'])

output['Unit Value'] = output['Unit Value'].apply(lambda x: re.sub('£','',x))
output['Unit Value'] = output['Unit Value'].apply(lambda x: re.sub(',','',x))
output['Unit Value'] = pd.to_numeric(output['Unit Value'])

output['Fund/ Asset %'] = output['Fund/ Asset %'].apply(lambda x: re.sub('%','',x))
output['Fund/ Asset %'] = pd.to_numeric(output['Fund/ Asset %'])



