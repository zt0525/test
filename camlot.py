import camelot
import pandas as pd 
pd.set_option('display.max_colwidth',500)
table = camelot.read_pdf("sample_wa_original_Redacted.pdf")
table.export('foo.csv', f='csv', compress=True)
table[0].parsing_report
data = table[0].df

ListCol = ['Fund/Asset','Number of Units','Unit Price','Unit Value','Fund/Asset %']
newData = data.iloc[2:-1].reset_index(drop = True)
newSeries = newData[0]
dataTemp = newSeries.str.split('\n',expand = True)
dataTemp.columns = ListCol
dataFinal = dataTemp.set_index('Fund/Asset')
dataFinal['Number of Units'] = dataFinal['Number of Units'].apply(lambda x: re.sub(',','',x))
dataFinal['Number of Units']  = pd.to_numeric(dataFinal['Number of Units'] )

dataFinal['Unit Price'] = dataFinal['Unit Price'].apply(lambda x: re.sub('p','',x))
dataFinal['Unit Price'] = pd.to_numeric(dataFinal['Unit Price'])

dataFinal['Unit Value'] = dataFinal['Unit Value'].apply(lambda x: re.sub('£','',x))
dataFinal['Unit Value'] = dataFinal['Unit Value'].apply(lambda x: re.sub(',','',x))
dataFinal['Unit Value'] = pd.to_numeric(dataFinal['Unit Value'])

dataFinal['Fund/Asset %'] = dataFinal['Fund/Asset %'].apply(lambda x: re.sub('%','',x))
dataFinal['Fund/Asset %'] = pd.to_numeric(dataFinal['Fund/Asset %'])
