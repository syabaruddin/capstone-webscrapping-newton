from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/history/IDR/USD/T')

url_get.content[1:777]

soup = BeautifulSoup(url_get.content,"html.parser")
print(type(soup))

table = soup.find('table',attrs={'class':'table table-striped table-hover table-hover-solid-row table-simple history-data'})
print(table.prettify()[1:500])

tr = table.find_all('tr')
tr[0:135]

#insert the scrapping process here
temp = [] 

for i in range(0,12):
    row = table.find_all('tr')[i]

    #get date
    date = row.find_all('td')[0].text
    date = date.strip()
    
    #get weekday 
    weekday = row.find_all('td')[1].text
    weekday = weekday.strip()
    
    #get IDRtoUSD 
    IDRtoUSD = row.find_all('td')[2].text
    IDRtoUSD = IDRtoUSD.strip()
    
    #get remarks
    remarks = row.find_all('td')[3].text
    remarks = remarks.strip()
               
    temp.append((date,weekday,IDRtoUSD,remarks))
    
for i in range(14,36):
    row = table.find_all('tr')[i]

    #get date
    date = row.find_all('td')[0].text
    date = date.strip()
    
    #get weekday 
    weekday = row.find_all('td')[1].text
    weekday = weekday.strip()
    
    #get IDRtoUSD 
    IDRtoUSD = row.find_all('td')[2].text
    IDRtoUSD = IDRtoUSD.strip()
    
    #get remarks
    remarks = row.find_all('td')[3].text
    remarks = remarks.strip()
               
    temp.append((date,weekday,IDRtoUSD,remarks))
    
for i in range(38,len(tr)):
    row = table.find_all('tr')[i]

    #get date
    date = row.find_all('td')[0].text
    date = date.strip()
    
    #get weekday 
    weekday = row.find_all('td')[1].text
    weekday = weekday.strip()
    
    #get IDRtoUSD 
    IDRtoUSD = row.find_all('td')[2].text
    IDRtoUSD = IDRtoUSD.strip()
    
    #get remarks
    remarks = row.find_all('td')[3].text
    remarks = remarks.strip()
    
    temp.append((date,weekday,IDRtoUSD,remarks))
    
temp 

temp = temp[::-1]
temp

#change into dataframe
df = pd.DataFrame(temp,columns = ('date','weekday','IDRtoUSD','remarks'))


#insert data wrangling here

#clean the IDRtoUSD, replace the "," and "IDR" and change it to float data type
df['IDRtoUSD']=df['IDRtoUSD'].replace(",","",regex=True).replace("IDR","",regex=True)
df['IDRtoUSD']=df['IDRtoUSD'].astype('float64')

#change date data type from object to datetime data type
df['date']=df['date'].astype('datetime64')

#change weekday data type from object to categorical data type
df['weekday']=df['weekday'].astype('category')


exchange = df.loc[:,['date','IDRtoUSD']].set_index('date')
exchange

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'USD {exchange["IDRtoUSD"].mean()}'

	# generate plot
	ax = exchange.plot(figsize = (20,9))
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]


	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)
