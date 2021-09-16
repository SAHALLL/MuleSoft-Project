#Making Connection 
import mysql.connector
dbase = mysql.connector.connect(host="localhost",user="sahal",passwd="##we145!!!dc",database="movies")
mycursor = dbase.cursor()
#Creating table for the database
mycursor.execute("Create table Fmovies(Mname varchar(30),Actor varchar(20),Actress varchar(20),release_year int(4),Director_name varchar(20))")