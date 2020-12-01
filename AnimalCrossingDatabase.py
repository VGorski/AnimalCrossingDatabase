import pymysql as ps

# authors: Victoria Gorski and Julia Wilkinson
# database name: animal-crossing-catalog-database
# username: admin
# password: Password123

# Connect to the database
def make_connection():
    return ps.connect(host='animal-crossing-catalog-database.caohgd8s4fpc.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='Password123',
                      port=3306, autocommit=True)

# Set up the database
def setupDatabase(data):

    # Create the database
    data.execute('DROP DATABASE IF EXISTS animal_crossing_catalog_database');
    data.execute('CREATE DATABASE animal_crossing_catalog_database');
    data.execute('USE animal_crossing_catalog_database');

    # Drop any of the previously existing tables
    data.execute('DROP TABLE IF EXISTS Fish');
    data.execute('DROP TABLE IF EXISTS Bugs');
    data.execute('DROP TABLE IF EXISTS Availability');

    # Create each of the tables
    # Create the Fish table
    data.execute(
        '''CREATE TABLE Fish (
        FishName VARCHAR(30) NOT NULL PRIMARY KEY,
        Location VARCHAR(30) NOT NULL,
        Weather VARCHAR(20),
        Shadow VARCHAR(20),
        NorthernHemisphereJanuary VARCHAR(20) NOT NULL,
        NorthernHemisphereFeburary VARCHAR(20) NOT NULL,
        NorthernHemisphereMarch VARCHAR(20) NOT NULL,
        NorthernHemisphereApril VARCHAR(20) NOT NULL,
        NorthernHemisphereMay VARCHAR(20) NOT NULL,
        NorthernHemisphereJune VARCHAR(20) NOT NULL,
        NorthernHemisphereJuly VARCHAR(20) NOT NULL,
        NorthernHemisphereAugust VARCHAR(20) NOT NULL,
        NorthernHemisphereSeptember VARCHAR(20) NOT NULL,
        NorthernHemisphereOctober VARCHAR(20) NOT NULL,
        NorthernHemisphereNovember VARCHAR(20) NOT NULL,
        NorthernHemisphereDecember VARCHAR(20) NOT NULL,
        SouthernHemisphereJanuary VARCHAR(20) NOT NULL,
        SouthernHemisphereFeburary VARCHAR(20) NOT NULL,
        SouthernHemisphereMarch VARCHAR(20) NOT NULL,
        SouthernHemisphereApril VARCHAR(20) NOT NULL,
        SouthernHemisphereMay VARCHAR(20) NOT NULL,
        SouthernHemisphereJune VARCHAR(20) NOT NULL,
        SouthernHemisphereJuly VARCHAR(20) NOT NULL,
        SouthernHemisphereAugust VARCHAR(20) NOT NULL,
        SouthernHemisphereSeptember VARCHAR(20) NOT NULL,
        SouthernHemisphereOctober VARCHAR(20) NOT NULL,
        SouthernHemisphereNovember VARCHAR(20) NOT NULL,
        SouthernHemisphereDecember VARCHAR(20) NOT NULL,
        ColorOne VARCHAR(20) NOT NULL,
        ColorTwo VARCHAR(20),
        SellPrice VARCHAR(10) NOT NULL,
        Size VARCHAR(20) NOT NULL);''')
    
    # Create the Bug table
    data.execute(
        '''CREATE TABLE Bugs (
        BugName VARCHAR(30) NOT NULL PRIMARY KEY,
        Location VARCHAR(30) NOT NULL,
        Weather VARCHAR(20),
        NorthernHemisphereJanuary VARCHAR(20) NOT NULL,
        NorthernHemisphereFeburary VARCHAR(20) NOT NULL,
        NorthernHemisphereMarch VARCHAR(20) NOT NULL,
        NorthernHemisphereApril VARCHAR(20) NOT NULL,
        NorthernHemisphereMay VARCHAR(20) NOT NULL,
        NorthernHemisphereJune VARCHAR(20) NOT NULL,
        NorthernHemisphereJuly VARCHAR(20) NOT NULL,
        NorthernHemisphereAugust VARCHAR(20) NOT NULL,
        NorthernHemisphereSeptember VARCHAR(20) NOT NULL,
        NorthernHemisphereOctober VARCHAR(20) NOT NULL,
        NorthernHemisphereNovember VARCHAR(20) NOT NULL,
        NorthernHemisphereDecember VARCHAR(20) NOT NULL,
        SouthernHemisphereJanuary VARCHAR(20) NOT NULL,
        SouthernHemisphereFeburary VARCHAR(20) NOT NULL,
        SouthernHemisphereMarch VARCHAR(20) NOT NULL,
        SouthernHemisphereApril VARCHAR(20) NOT NULL,
        SouthernHemisphereMay VARCHAR(20) NOT NULL,
        SouthernHemisphereJune VARCHAR(20) NOT NULL,
        SouthernHemisphereJuly VARCHAR(20) NOT NULL,
        SouthernHemisphereAugust VARCHAR(20) NOT NULL,
        SouthernHemisphereSeptember VARCHAR(20) NOT NULL,
        SouthernHemisphereOctober VARCHAR(20) NOT NULL,
        SouthernHemisphereNovember VARCHAR(20) NOT NULL,
        SouthernHemisphereDecember VARCHAR(20) NOT NULL,
        ColorOne VARCHAR(20) NOT NULL,
        ColorTwo VARCHAR(20),
        SellPrice VARCHAR(10) NOT NULL);''')

    # Create the join table
    # Create the Availability table
    data.execute(
        '''CREATE TABLE Availability (
        AnimalName VARCHAR(30) NOT NULL,
        Month VARCHAR(30) NOT NULL,
        Hemisphere VARCHAR(30) NOT NULL,
        Availability VARCHAR(30) NOT NULL,
        PRIMARY KEY(AnimalName, Month, Hemisphere));''')
 
# Insert data into its respective tables
def insertData(data):
    
    # Insert data into the Fish table
    with open("data/rf_fish.csv", 'r') as r1:
        # Extra line for the headers
        next(r1)
        for line in r1:
            # Split the data
            line = line.split(',')
            # Get the name of the fish
            Name = line.__getitem__(1)
            # Get the location of the fish
            Where = line.__getitem__(3)
            #
            Shadow = line.__getitem__(4)
            # Get if fish appears in a certain weather condition
            Rain = line.__getitem__(7)
            # Get if the fish appears in January in the northern hemisphere
            NHJan = line.__getitem__(8)
            # Get if the fish appears in Feburary in the northern hemisphere 
            NHFeb = line.__getitem__(9)
            # Get if the fish appears in March in the northern hemisphere 
            NHMar = line.__getitem__(10)
            # Get if the fish appears in April in the northern hemisphere 
            NHApr = line.__getitem__(11)
            # Get if the fish appears in May in the northern hemisphere
            NHMay = line.__getitem__(12)
            # Get if the fish appears in June in the northern hemisphere 
            NHJun = line.__getitem__(13)
            # Get if the fish appears in July in the northern hemisphere 
            NHJul = line.__getitem__(14)
            # Get if the fish appears in August in the northern hemisphere 
            NHAug = line.__getitem__(15)
            # Get if the fish appears in September in the northern hemisphere 
            NHSep = line.__getitem__(16)
            # Get if the fish appears in October in the northern hemisphere 
            NHOct = line.__getitem__(17)
            # Get if the fish appears in November in the northern hemisphere 
            NHNov = line.__getitem__(18)
            # Get if the fish appears in December in the northern hemisphere 
            NHDec = line.__getitem__(19)
            # Get if the fish appears in January in the southern hemisphere 
            SHJan = line.__getitem__(20)
            # Get if the fish appears in Feburary in the southern hemisphere 
            SHFeb = line.__getitem__(21)
            # Get if the fish appears in March in the southern hemisphere 
            SHMar = line.__getitem__(22)
            # Get if the fish appears in April in the southern hemisphere 
            SHApr = line.__getitem__(23)
            # Get if the fish appears in May in the southern hemisphere 
            SHMay = line.__getitem__(24)
            # Get if the fish appears in June in the southern hemisphere 
            SHJun = line.__getitem__(25)
            # Get if the fish appears in July in the southern hemisphere 
            SHJul = line.__getitem__(26)
            # Get if the fish appears in August in the southern hemisphere 
            SHAug = line.__getitem__(27)
            # Get if the fish appears in September in the southern hemisphere 
            SHSep = line.__getitem__(28)
            # Get if the fish appears in October in the southern hemisphere 
            SHOct = line.__getitem__(29)
            # Get if the fish appears in November in the southern hemisphere 
            SHNov = line.__getitem__(30)
            # Get if the fish appears in December in the southern hemisphere 
            SHDec = line.__getitem__(31)
            # Get the primary color of the fish
            ColorOne = line.__getitem__(32)
            # Get the secondary color of the fish
            ColorTwo = line.__getitem__(33)
            # Get the selling price of the fish
            Sell = line.__getitem__(2)
            # Get the size of the fish 
            Size = line.__getitem__(34) 

            # Allow the data to go from the .csv file to the database
            data.execute(
                'INSERT IGNORE INTO Fish(FishName, Location, Shadow, Weather, NorthernHemisphereJanuary, NorthernHemisphereFeburary, NorthernHemisphereMarch, NorthernHemisphereApril, NorthernHemisphereMay, NorthernHemisphereJune, NorthernHemisphereJuly, NorthernHemisphereAugust, NorthernHemisphereSeptember, NorthernHemisphereOctober, NorthernHemisphereNovember, NorthernHemisphereDecember, SouthernHemisphereJanuary, SouthernHemisphereFeburary, SouthernHemisphereMarch, SouthernHemisphereApril, SouthernHemisphereMay, SouthernHemisphereJune, SouthernHemisphereJuly, SouthernHemisphereAugust, SouthernHemisphereSeptember, SouthernHemisphereOctober, SouthernHemisphereNovember, SouthernHemisphereDecember,ColorOne, ColorTwo, SellPrice, Size) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (Name, Where, Shadow, Rain, NHJan, NHFeb, NHMar, NHApr, NHMay, NHJun, NHJul, NHAug, NHSep, NHOct, NHNov, NHDec, SHJan, SHFeb, SHMar, SHApr, SHMay, SHJun, SHJul, SHAug, SHSep, SHOct, SHNov, SHDec, ColorOne, ColorTwo, Sell, Size))

    # Insert data into the Bugs table
    with open("data/rf_insects.csv", 'r') as r1:
        # Extra line for the headers
        next(r1)
        for line in r1:
            # Split the data
            line = line.split(',')
            # Get the name of the bug
            Name = line.__getitem__(1)
            # Get the location of the bug
            Where = line.__getitem__(3)
            # Get if bug appears in a certain weather condition
            Weather = line.__getitem__(4)
            # Get if the bug appears in January in the northern hemisphere
            NHJan = line.__getitem__(7)
            # Get if the bug appears in Feburary in the northern hemisphere
            NHFeb = line.__getitem__(8)
            # Get if the bug appears in March in the northern hemisphere
            NHMar = line.__getitem__(9)
            # Get if the bug appears in April in the northern hemisphere
            NHApr = line.__getitem__(10)
            # Get if the bug appears in May in the northern hemisphere
            NHMay = line.__getitem__(11)
            # Get if the bug appears in June in the northern hemisphere
            NHJun = line.__getitem__(12)
            # Get if the bug appears in July in the northern hemisphere
            NHJul = line.__getitem__(13)
            # Get if the bug appears in August in the northern hemisphere
            NHAug = line.__getitem__(14)
            # Get if the bug appears in September in the northern hemisphere
            NHSep = line.__getitem__(15)
            # Get if the bug appears in October in the northern hemisphere
            NHOct = line.__getitem__(16)
            # Get if the bug appears in November in the northern hemisphere
            NHNov = line.__getitem__(17)
            # Get if the bug appears in December in the northern hemisphere
            NHDec = line.__getitem__(18)
            # Get if the bug appears in January in the southern hemisphere
            SHJan = line.__getitem__(19)
            # Get if the bug appears in Feburary in the southern hemisphere
            SHFeb = line.__getitem__(20)
            # Get if the bug appears in March in the southern hemisphere
            SHMar = line.__getitem__(21)
            # Get if the bug appears in April in the southern hemisphere
            SHApr = line.__getitem__(22)
            # Get if the bug appears in May in the southern hemisphere
            SHMay = line.__getitem__(23)
            # Get if the bug appears in June in the southern hemisphere
            SHJun = line.__getitem__(24)
            # Get if the bug appears in July in the southern hemisphere
            SHJul = line.__getitem__(25)
            # Get if the bug appears in August in the southern hemisphere
            SHAug = line.__getitem__(26)
            # Get if the bug appears in September in the southern hemisphere
            SHSep = line.__getitem__(27)
            # Get if the bug appears in October in the southern hemisphere
            SHOct = line.__getitem__(28)
            # Get if the bug appears in November in the southern hemisphere
            SHNov = line.__getitem__(29)
            # Get if the bug appears in December in the southern hemisphere
            SHDec = line.__getitem__(30)
            # Get the primary color of the bug
            ColorOne = line.__getitem__(31)
            # Get the secondary color of the bug
            ColorTwo = line.__getitem__(32)
            # Get the selling price of the fish
            Sell = line.__getitem__(2)

            # Allow the data to go from the .csv file to the database
            data.execute(
                'INSERT IGNORE INTO Bugs(BugName, Location, Weather, NorthernHemisphereJanuary, NorthernHemisphereFeburary, NorthernHemisphereMarch, NorthernHemisphereApril, NorthernHemisphereMay, NorthernHemisphereJune, NorthernHemisphereJuly, NorthernHemisphereAugust, NorthernHemisphereSeptember, NorthernHemisphereOctober, NorthernHemisphereNovember, NorthernHemisphereDecember, SouthernHemisphereJanuary, SouthernHemisphereFeburary, SouthernHemisphereMarch, SouthernHemisphereApril, SouthernHemisphereMay, SouthernHemisphereJune, SouthernHemisphereJuly, SouthernHemisphereAugust, SouthernHemisphereSeptember, SouthernHemisphereOctober, SouthernHemisphereNovember, SouthernHemisphereDecember, ColorOne, ColorTwo, SellPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (Name, Where, Weather, NHJan, NHFeb, NHMar, NHApr, NHMay, NHJun, NHJul, NHAug, NHSep, NHOct, NHNov, NHDec, SHJan, SHFeb, SHMar, SHApr, SHMay, SHJun, SHJul, SHAug, SHSep, SHOct, SHNov, SHDec, ColorOne, ColorTwo, Sell))

    # Insert data into the Availability table
    with open("data/rf_fish_and_insects.csv", 'r') as r1:
        # Extra line for the headers
        next(r1)
        for line in r1:
            # Split the data by commas
            line = line.split(',')
            # Get the name of the animal
            AnimalName = line.__getitem__(0)
            # Get the name of the month
            Month = line.__getitem__(1)
            # Get the hemisphere
            Hemisphere = line.__getitem__(2)
            # Get when the fish is available 
            Availability = line.__getitem__(3)
                    
            # Allow the data to go from the .csv file to the database
            data.execute(
                'INSERT IGNORE INTO Availability(AnimalName, Month, Hemisphere, Availability) VALUES (%s, %s, %s, %s)',
                (AnimalName, Month, Hemisphere, Availability))

            
# Make the connection to the database
connection = make_connection()
data = connection.cursor()
setupDatabase(data)
# Insert the data into the database
insertData(data)
# Close the database connection
data.close()
connection.commit()
# Make sure all the data is saved
connection.close()


