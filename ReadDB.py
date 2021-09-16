#Making Connection 
import mysql.connector
dbase = mysql.connector.connect(host="localhost",user="sahal",passwd="##we145!!!dc",database="movies")
mycursor = dbase.cursor()
#Fecthing and printing the values
mycursor.execute("Select * from Fmovies")
end = mycursor.fetchall()
for row in end:
	print(rows)