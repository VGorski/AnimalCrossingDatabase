import pymysql as ps
import AnimalCrossingDatabase 
import matplotlib.pyplot as plt
import pandas as pd 
import plotly.express as px

# Connect to the database
def make_connection():
    return ps.connect(host='animal-crossing-catalog-database.caohgd8s4fpc.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='Password123',
                      port=3306, autocommit=True)

def setupDatabase(cur):
    cur.execute('USE animal_crossing_catalog_database')
    cur.execute('SELECT size, COUNT(*) FROM Fish GROUP BY size ORDER BY COUNT(*) DESC')
    sizes=cur.fetchall()
    fig1=px.pie(values=sizes['COUNT(*)'],names=sizes['size'],title='Sizes of Different Fish in Animal Crossing')
    with open('p_graph.html', 'a') as f:
        f.write(fig1.tohtml(full_html=False, include_plotlyjs='cdn'))




#cur.execute('SELECT FishName, price FROM Fish, order by RAND() LIMIT 10')

#locations=pd.read_sql('SELECT COUNT(FishName), location FROM Fish GROUP BY location',conn)
#availibility=pd.read_sql('SELECT NHJan, NHFeb, NHMar, NHApr, NHMay, NHJun, NHJul, NHAug, NHSep, NHOct, NHNov, NHDec, SHJan, SHFeb, SHMar, SHApr, SHMay, SHJun, SHJul, SHAug, SHSep, SHOct, SHNov, SHDec FROM Fish WHERE != null',conn)



connection = make_connection()
cur = connection.cursor()
setupDatabase(cur)
