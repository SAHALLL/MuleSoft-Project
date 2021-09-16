#Making Connection 
import mysql.connector
dbase = mysql.connector.connect(host="localhost",user="sahal",passwd="##we145!!!dc")
mycursor = dbase.cursor()
#Creating Database named "movies"
mycursor.execute("Create database movies")
