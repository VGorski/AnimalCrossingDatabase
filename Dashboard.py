import pymysql as ps
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages")
import pandas as pd 
import plotly.express as px

conn=ps.connect(host='animal-crossing-catalog-database.caohgd8s4fpc.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='Password123',
                      port=3306, autocommit=True)
sizes=pd.read_sql('SELECT size, COUNT(*) FROM Fish GROUP BY size',conn)
fishprice=pd.read_sql('SELECT FishName, price FROM Fish, order by RAND() LIMIT 10',conn)
locations=pd.read_sql('SELECT COUNT(FishName), location FROM Fish GROUP BY location',conn)
availibility=pd.read_sql('SELECT NHJan, NHFeb, NHMar, NHApr, NHMay, NHJun, NHJul, NHAug, NHSep, NHOct, NHNov, NHDec, SHJan, SHFeb, SHMar, SHApr, SHMay, SHJun, SHJul, SHAug, SHSep, SHOct, SHNov, SHDec FROM Fish WHERE != null',conn)

fig1=px.pie(values=sizes['COUNT(*)'],names=sizes['size'],title='Sizes of Different Fish in Animal Crossing')

with open('p_graph.html', 'a') as f:
    f.write(fig1.tohtml(full_html=False, include_plotlyjs='cdn'))
