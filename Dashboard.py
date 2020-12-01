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
df1=pd.read_sql('Select Location, COUNT(*) from Fish GROUP BY Location',conn)
fig2=px.histogram(df1,x=df1['Location'], y=df1['COUNT(*)'], color="Location", title='Location of Different Fish', )
df2=pd.read_sql('SELECT AnimalName, Availability FROM Availability',conn)
fig3=px.scatter(df2,x=df2['Availability'],y=df2['AnimalName'], title='Availability of Fish and Bugs')
df3=pd.read_sql('SELECT Location, Weather, BugName FROM Bugs;', conn)
fig4=px.scatter(df3, x=df3["BugName"], y=df3["Location"], color="Weather", hover_name="Location")    
df4=pd.read_sql('SELECT AnimalName, Availability, Month, Location FROM Availability, Fish WHERE AnimalName = FishName UNION SELECT AnimalName, Availability, Month, Location FROM Availability, Bugs WHERE AnimalName = BugName;', conn)
fig5=px.scatter(df4,x=df4["Location"],y=df4["Availability"], color="Month")
with open('p_graph.html', 'a') as f:
    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig4.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig5.to_html(full_html=False, include_plotlyjs='cdn'))

fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()


#cur.execute('SELECT FishName, price FROM Fish, order by RAND() LIMIT 10')

#locations=pd.read_sql('SELECT COUNT(FishName), location FROM Fish GROUP BY location',conn)
#availibility=pd.read_sql('SELECT NHJan, NHFeb, NHMar, NHApr, NHMay, NHJun, NHJul, NHAug, NHSep, NHOct, NHNov, NHDec, SHJan, SHFeb, SHMar, SHApr, SHMay, SHJun, SHJul, SHAug, SHSep, SHOct, SHNov, SHDec FROM Fish WHERE != null',conn)




