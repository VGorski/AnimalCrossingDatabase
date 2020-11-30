import pymysql
import AnimalCrossingDatabase.py
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def make_connection():
    return ps.connect(host='animal-crossing-catalog-database.caohgd8s4fpc.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='Password123',
                      port=3306, autocommit=True)

ppy = AnimalCrossingDatabase.V2Client()
cnx = make_connection()
cur = cnx.cursor()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
def pieChart():
    graph1 = fig.add_subplot(231)
    cur.execute('''SELECT COUNT(size)
                    FROM Fish
                    WHERE size = "large" AND size = "Large w/Fin" AND size = X-Large AND size = "Long" ''')
    largesize = cur.fetchone()[0]

    cur.execute('''SELECT COUNT(size)
                    FROM Fish
                    WHERE size = "Medium"  AND size = "Medium w/Fin" ''')
    mediumsize = cur.fetchone()[0]

    cur.execute('''SELECT COUNT(size)
                    FROM Fish
                    WHERE size = "Small" AND size = "x-small" ''')
    smallsize = cur.fetchone()[0]
    labels = 'Large', 'Medium', 'Small'
    sizes = [large, medium, small]
    explode = (0, 0.1, 0)  # only "explode" the 2nd slice 

    graph1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
               shadow=True, startangle=90)
    graph1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    graph1.set_title('Size of Fish')

#function for horizontal bar graph
def horBarGraph():
    graph2 = fig.add_subplot(232)

    cur.execute('''SELECT FishName, price
    from Fish,
    order by RAND()
    LIMIT 10
    ''')
    fish = cur.fetchall()

    # Horizontal Bar Graph
    graph2.set_title('Prices of Fish by Name')
    graph2.barh([x[1] for x in fish], [y[0] for y in fish], color=('r'))
    graph2.set_xlabel('Names')
    graph2.set_ylabel('Price')

#function for line graph
def lineGraph():
    graph3 = fig.add_subplot(233)
    cur.execute('''select count(FishName), location
    from Fish
    group by location;''')
    location = cur.fetchall()

    # Line graph
    graph3.plot([x[1] for x in growthRate], [y[0] for y in growthRate])
    graph3.set_xlabel('Locations')
    for tick in graph3.get_xticklabels():
        tick.set_rotation(70)
    graph3.set_ylabel('Number of Fish')
    graph3.set_title('Line Graph of Number of Fish in Each Location')



#function for scatterplit
def scatterPlot():
    graph5 = fig.add_subplot(235)
    cur.execute('''select NHJan, NHFeb, NHMar, NHApr, NHMay, NHJun, NHJul, NHAug, NHSep, NHOct, NHNov, NHDec, SHJan, SHFeb, SHMar, SHApr, SHMay, SHJun, SHJul, SHAug, SHSep, SHOct, SHNov, SHDec
    from Fish;''')
    AnimalCrossingDatabase = cur.fetchall()

    # Scatter Graph
    graph5.scatter([x[0] for x in fish], [y[1] for y in fish])
    graph5.set_title('Times of Availible Fish')
    graph5.set_xlabel('not sure')
    graph5.set_ylabel('not sure')

#set the size of window to 16x12 and window title
fig = plt.figure(figsize=(16, 12))
fig.canvas.set_window_title('Animal Crossing Database Dashboard')

#call each chart and display them
pieChart()
horBarGraph()
lineGraph()
scatterPlot()
plt.tight_layout()
plt.show()
