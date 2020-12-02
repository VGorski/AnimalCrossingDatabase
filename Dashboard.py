import pymysql as ps
import AnimalCrossingDatabase 
import matplotlib.pyplot as plt
import pandas as pd 
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly import tools
# Connect to the database

conn=ps.connect(host='animal-crossing-catalog-database.caohgd8s4fpc.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='Password123',
                      port=3306, db='animal_crossing_catalog_database', autocommit=True)

pio.templates.default = "plotly_dark"

fig = make_subplots(rows=2, cols=3, specs=[[{"type": "pie"}, {"type": "histogram"},{"type": "scatter"}],[{"type": "bar"},{"type": "scatter"},{"type": "pie"}]])

df=pd.read_sql('SELECT Shadow, COUNT(*) FROM Fish GROUP BY Shadow ORDER BY COUNT(*) DESC', conn)
#fig1=px.pie(df, values=df['COUNT(*)'],names=df['Shadow'],title='Sizes of Different Fish in Animal Crossing',labels={'COUNT(*)':'Amount of Fish'})
fig.add_pie(values=df['COUNT(*)'],name=str(df['Shadow']),legendgroup='Shadow', row=1, col=1)
df1=pd.read_sql('Select Location, COUNT(*) from Fish GROUP BY Location',conn)
#fig2=px.histogram(df1,x=df1['Location'], y=df1['COUNT(*)'], color="Location", title='Location of Different Fish',labels={'COUNT(*)':'Amount of Fish'})
fig.add_bar(x=df1['Location'], y=df1['COUNT(*)'],row=1,col=2)
df2=pd.read_sql('SELECT AnimalName, Availability, Month FROM Availability',conn)
#fig3=px.scatter(df2,x=df2['Availability'],y=df2['AnimalName'], color="Month", title='Availability of Fish and Bugs')
fig.add_scatter(x=df2['Availability'],y=df2['AnimalName'],mode='markers',row=1,col=3)
df3=pd.read_sql('SELECT Location, COUNT(*) FROM Bugs GROUP BY Location;', conn)
#ig4=px.bar(df3, x=df3["Location"], y=df3['COUNT(*)'], color='Location', title='Bugs at Different Locations', labels={'COUNT(*)':'Amount of Bugs'})   
fig.add_bar(x=df3["Location"], y=df3['COUNT(*)'],row=2,col=1)
df4=pd.read_sql('SELECT AnimalName, Availability, Month, Location FROM Availability, Fish WHERE AnimalName = FishName UNION SELECT AnimalName, Availability, Month, Location FROM Availability, Bugs WHERE AnimalName = BugName;', conn)
#fig5=px.scatter(df4,x=df4["Location"],y=df4["Availability"], color="Month")
fig.add_scatter(x=df4["Location"],y=df4["Availability"],mode='markers',row=2,col=2)


fig.update_layout(title_font_family="Old Standard TT",height=1000, width=1800, title_text="Animal Crossing Database Dashboard")


fig.show()



#cur.execute('SELECT FishName, price FROM Fish, order by RAND() LIMIT 10')

#locations=pd.read_sql('SELECT COUNT(FishName), location FROM Fish GROUP BY location',conn)
#availibility=pd.read_sql('SELECT NHJan, NHFeb, NHMar, NHApr, NHMay, NHJun, NHJul, NHAug, NHSep, NHOct, NHNov, NHDec, SHJan, SHFeb, SHMar, SHApr, SHMay, SHJun, SHJul, SHAug, SHSep, SHOct, SHNov, SHDec FROM Fish WHERE != null',conn)



