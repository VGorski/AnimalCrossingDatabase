import pymysql as ps
import AnimalCrossingDatabase 
import matplotlib.pyplot as plt
import pandas as pd 
import plotly.express as px

# Connect to the database
conn=ps.connect(host='animal-crossing-catalog-database.caohgd8s4fpc.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='Password123',
                      port=3306, db='animal_crossing_catalog_database', autocommit=True)

df=pd.read_sql('SELECT Shadow, COUNT(*) FROM Fish GROUP BY Shadow ORDER BY COUNT(*) DESC', conn)
fig1=px.pie(df, values=df['COUNT(*)'],names=df['Shadow'],title='Sizes of Different Fish in Animal Crossing')
with open('p_graph.html', 'a') as f:
    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))

fig1.show()


#cur.execute('SELECT FishName, price FROM Fish, order by RAND() LIMIT 10')

#locations=pd.read_sql('SELECT COUNT(FishName), location FROM Fish GROUP BY location',conn)
#availibility=pd.read_sql('SELECT NHJan, NHFeb, NHMar, NHApr, NHMay, NHJun, NHJul, NHAug, NHSep, NHOct, NHNov, NHDec, SHJan, SHFeb, SHMar, SHApr, SHMay, SHJun, SHJul, SHAug, SHSep, SHOct, SHNov, SHDec FROM Fish WHERE != null',conn)




