import mysql.connector as sql
from DBProperty import *
class DBConnectivity:
    @staticmethod
    def makeconnection():
        l=DBProperty.getparameter()
        print(l)

DBConnectivity.makeconnection()

