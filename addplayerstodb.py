from pybaseball.lahman import *
import mysql.connector

# connect to mysql db
#db = mysql.connector.connect(user='nick', password='cornbread69',
#                             host='baseballchain.cncamowq5mql.us-west-2.rds.amazonaws.com',
#                             database='mlbplayers')

#mycursor = db.cursor()

people = people()

numplayers = 0

players = []

f = open("players.txt", "w")


for i in range(len(people)):
    if str(people.nameFirst[i]) != 'nan' and str(people.nameLast[i]) != 'nan':
        first = people.nameFirst[i]
        last = people.nameLast[i]
        f.write(first + ' ' + last + '\n')
        numplayers += 1
    else:
        continue



#sql = "INSERT INTO players (first, last) VALUES (%s, %s)"
#mycursor.executemany(sql, players)

#db.commit()

print(numplayers)