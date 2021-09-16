#Making Connection 
import mysql.connector
dbase = mysql.connector.connect(host="localhost",user="sahal",passwd="##we145!!!dc",database="movies")
mycursor = dbase.cursor()
#inserting values to the table
query = "Insert into Fmovies(Mname,Actor,Actress,release_year,Director_name) values(%s,%s)"
movies = [("M1","james","clara",1999,"jom"),("M2","kame","mora",2020,"kim"),("M3","sam","syncla",2000,"mukla") ]

mycursor.executemany(query,Fmovies)
#To save the changes from the last executed sql statement
dbase.commit()
