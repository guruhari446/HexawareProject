#from ICustomerService import *
#from IVehicleService import *
#from IReservationService import *
#from IAdminService import *
from util import DBProperty
import mysql.connector as sql
from exceptions import *
class Implement:
    def open(self):
        try:
            self.conn=sql.connect(host='localhost',database='carrental',user='root',password='guruhari2002#')
            if self.conn.is_connected:
                print('Database is Connected:')
            else:
                print('Not Connected with Database')
            self.stmt=self.conn.cursor()
            return True
        except Exception as e:
            print(f'Rasied DataBaseConnection:{e}')
            return False
    def close(self):
        self.conn.close()
    def GetCustomerById(self,customerId):
        try:
            self.open()
            select_str='''select * from customer where customerId=%s'''
            self.stmt.execute(select_str,(customerId,))
            recods=self.stmt.fetchall()
            print('')
            print('__________________Records In Customers Table__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False
    def GetCustomerByUsername(self,username):
        try :
            self.open()
            select_str = '''select * from customer where username=%s'''
            self.stmt.execute(select_str,(username,))
            recods = self.stmt.fetchall()
            print('')
            print('__________________Records In Customers Table__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f'Raised Invalid Input:{e}')
            return False
    def RegisterCustomer(self,customerid,firstname,lastname,email,phone,address,username,password,registrationdate):
        try:
            self.customerid = int(input('Enter customerid:'))
            self.firstname = input('Enter firstname:')
            self.lastname = input('Enter lastname:')
            self.email = input('Enter email:')
            self.phone = int(input('Enter phone:'))
            self.address = input('Enter address:')
            self.username = input('Enter username:')
            self.password = input('Enter password:')
            self.registerdate = input('Enter registrationdate:')
            print(self.customerid, self.firstname, self.lastname, self.email, self.phone, self.address, self.username,
                  self.password, self.registerdate)

            data = (self.customerid, self.firstname, self.lastname, self.email, self.phone, self.address, self.username,
                    self.password, self.registerdate)

            insert_str = '''insert into customer(customerId,firstName,lastName,email,phone,address,username,password ,registerdate )
                           values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str,(data,))
            self.conn.commit()
            print('Records Inserted Successfully--')
            self.close()
            return True
        except Exception as e:
            print(f'Raised Invalid Input :{e}')
            return False

    def UpdateCustomer(self,customerid,firstname,lastname,email,phone,address,username,password,registrationdate):
        try:
            self.customerid = int(input('Enter customerid:'))
            self.firstname = input('Enter firstname:')
            self.lastname = input('Enter lastname:')
            self.email = input('Enter email:')
            self.phone = int(input('Enter phone:'))
            self.address = input('Enter address:')
            self.username = input('Enter username:')
            self.password = input('Enter password:')
            self.registerdate = input('Enter registrationdate:')
            update_str = 'update customer set firstname =%s,lastname =%s,email = %s,phone = %s,address =%s,username =%s,password = %s,registerdate =%s where customerid=%s'
            self.open()

            data = (self.firstname, self.lastname, self.email, self.phone, self.address, self.username,
                 self.password, self.registerdate, self.customerid)

            self.stmt.executemany(update_str,(data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated successfully...')
            return True
        except Exception as e:
            print(f'Raised Invalid Input ;{e}')
            return False


    def DeleteCustomer(self,customerid):
        try:
            customerid= int(input('enter the customerid to be deleted:'))
            delete_str = 'delete from customer where customerid=%s'
            self.open()
            self.stmt.execute(delete_str,(customerid,))
            self.conn.commit()
            print('Records Deleted Successfully--------')
            return True
        except Exception as e:
            print(f'Raised Invalid Input :{e}')
            return False

    def GetVehicleById(self,vehicleid):
        try:
            self.open()
            select_str = '''select * from vehicle1 where vehicleid=%s '''
            self.stmt.execute(select_str,(vehicleid,))
            recods = self.stmt.fetchall()
            print('')
            print('_______________________Records In Vehicle_______________')
            for i in recods:
                print(i)
            self.close()
            return True
        except (Invalidinputexception,Vehiclenotfoundexception) as e:
            print(str(e))
            return False

    def GetAvailableVehicle(self,vehicleid):
        try:
            self.open()
            select_str = '''select avaliability  from vehicle1 where vehicleid=%s '''
            self.stmt.execute(select_str,(vehicleid,))
            recods = self.stmt.fetchall()
            print('')
            print('_______________________Records In Vehicle_______________')
            for i in recods:
                print(i)
            self.close()
            return True
        except (Invalidinputexception,Vehiclenotfoundexception) as e:
            print(str(e))
            return False

    def AddVehicle(self,vehicleid,model,make,cyear,color,registrationnum,avaliability,dailyrate):
        try:
            self.vehicleid = int(input('Enter the vehicleid:'))
            self.model = input('Enter the model name:')
            self.make = input('Enter the company name:')
            self.cyear = input('Enter the year of manufacture:')
            self.color = input('Enter the color of vehicle:')
            self.registrationnum = int(input('enter the registration Number:'))
            self.avaliability = input('Enter the availability:')
            self.dailyrate = int(input('Enter the dailyrate:'))
            print(self.vehicleid, self.model, self.make, self.cyear, self.color, self.registrationnum, self.avaliability,
              self.dailyrate)

            data = (self.vehicleid, self.model, self.make, self.cyear, self.color, self.registrationnum, self.avaliability,
                 self.dailyrate)
            insert_str = '''insert into vehicle1(vehicleid,model,make,cyear,color,registrationnum,avaliability,dailyrate)
                              values(%s,%s,%s,%s,%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str,(data,))
            self.conn.commit()
            print('Records Inserted Successfully..')
            self.close()
            return True
        except Exception as e:
            print(f'Invalid Input:{e}')
            return False


    def UpdateVehicle(self,vehicleid,model,make,cyear,color,registrationnum,avaliability,dailyrate):
        try:

            self.vehicleid = int(input('Enter the vehicleid:'))
            self.model = input('Enter the model name:')
            self.make = input('Enter the company name:')
            self.cyear = input('Enter the year of manufacture:')
            self.color = input('Enter the color of vehicle:')
            self.registrationnum = int(input('enter the registration Number:'))
            self.avaliability = input('Enter the availability:')
            self.dailyrate = int(input('Enter the dailyrate:'))
            update_str = 'update vehicle1 set model=%s,make=%s,cyear=%s,color=%s,registrationnum=%s,avaliability=%s,dailyrate=%s where vehicleid=%s '
            self.open()
            data = ( self.model, self.make, self.cyear, self.color, self.registrationnum, self.avaliability,
             self.dailyrate,self.vehicleid)
            self.stmt.executemany(update_str,(data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated Successfully..')
            return True
        except (Invalidinputexception,Vehiclenotfoundexception) as e:
            print(str(e))
            return False

    def RemoveVehicle(self,vehicleid):
        try:
            vehicleid = int(input('Enter the vehicleid to remove:'))
            delete_str = 'delete from vehicle1 where vehicleid=%s'
            self.open()
            self.stmt.execute(delete_str,(vehicleid,))
            self.conn.commit()
            print('Records Deleted Successfully... ')
            return True
        except (Invalidinputexception,Vehiclenotfound) as e:
            print(str(e))
            return False

    def GetReservationById(self,reservationid):
        try:
            self.open()
            select_str = '''select * from reservation where reservationid=%s'''
            self.stmt.execute(select_str,(reservationid,))
            recods = self.stmt.fetchall()
            print('')
            print('___________Records in reservation table________________ ')
            for i in recods:
                print(i)
            self.close()
            return True
        except (Invalidinputexception,Reservationexception) as e:
            print(str(e))
            return False

    def GetReservationByCustomerid(self,customerid):
        try:
            self.open()
            select_str = '''select * from reservation where customerid=%s'''
            self.stmt.execute(select_str,(customerid,))
            recods = self.stmt.fetchall()
            print('')
            print('___________Records in reservation table________________ ')
            for i in recods:
                print(i)
            self.close()
            return True
        except (Invalidinputexception,Reservationexception) as e:
            print(str(e))
            return False

    def CreateReservation(self,reservationid,customerid,vehicleid,startdate,enddate,totalcost,cstatus):
        try:
            self.reservationid = int(input('Enter the reservationid:'))
            self.customerid = int(input('Enter the customerid:'))
            self.vehicleid = int(input('Enter the vehicleid:'))
            self.startdate = input('Enter the start date:')
            self.enddate = input('Enter the End date:')
            self.totalcost = input('Enter the Totalcost')
            self.cstatus = input('Enter the status:')
            print(self.reservationid, self.customerid, self.vehicleid, self.startdate, self.enddate, self.totalcost,
                  self.cstatus)

            data = (self.reservationid, self.customerid, self.vehicleid, self.startdate, self.enddate, self.totalcost,
                     self.cstatus)
            insert_str = '''insert into reservation(reservationid,customerid,vehicleid,startdate,enddate,totalcost,cstatus)
                            values(%s,%s,%s,%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str, (data,))
            self.conn.commit()
            print('Records Inserted Successfully...')
            self.close()
            return True
        except (Invalidinputexception, Reservationexception) as e:
            print(str(e))
            return False

    def UpdateReservation(self,reservationid,customerid,vehicleid,startdate,enddate,totalcost,cstatus):
        try:

            self.reservationid = int(input('Enter the reservationid:'))
            self.customerid = int(input('Enter the customerid:'))
            self.vehicleid = int(input('Enter the vehicleid:'))
            self.startdate = input('Enter the start date:')
            self.enddate = input('Enter the End date:')
            self.totalcost = input('Enter the Totalcost:')
            self.cstatus = input('Enter the status:')
            update_str = 'update reservation set customerid=%s,vehicleid=%s,startdate=%s,enddate=%s,totalcost=%s,cstatus=%s where reservationid=%s'
            self.open()
            data = (self.customerid, self.vehicleid, self.startdate, self.enddate, self.totalcost,
                 self.cstatus,self.reservationid)
            self.stmt.executemany(update_str, (data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated Successfully....')
            return True
        except (Invalidinputexception, Reservationexception) as e:
            print(str(e))
            return False

    def CancelReservation(self,reservationid):
        try:
            reservationid= int(input('Enter the reservationid:'))
            delete_str = 'delete from reservation where reservationid=%s'
            self.open()
            self.stmt.execute(delete_str,(reservationid,))
            self.conn.commit()
            print('Records deleted Successfully....')
            return True
        except (Invalidinputexception, Reservationexception) as e:
            print(str(e))
            return False

    def GetAdminById(self,adminid):
       try:
           self.open()
           select_str = '''select * from admin where adminid=%s'''
           self.stmt.execute(select_str,(adminid,))
           recods = self.stmt.fetchall()
           for i in recods:
               print(i)
           self.close()
           return True
       except Exception as e:
           print(f'Raised AdminNotFound:{e}')
           return False

    def GetAdminByUsername(self,username):
        try:
            self.open()
            select_str = '''select * from admin where username=%s'''
            self.stmt.execute(select_str,(username,))
            recods = self.stmt.fetchall()
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f'Raised AdminNotFound:{e}')
            return False

    def RegisterAdmin(self,adminid,firstname,lastname,email,phone,username,apassword,role,joindate):
        try:
            self.adminid = int(input('Enter Adminid:'))
            self.firstname = input('Enter the firstname of admin:')
            self.lastname = input('Enter the lastname of admin:')
            self.email = input('Enter the email:')
            self.phone = input('Enter the phonenumber:')
            self.username = input('Enter the username:')
            self.apassword = input('Enter the password :')
            self.role = input('Enter the role of admin:')
            self.joindate = input('Enter the joindate:')
            print(self.adminid, self.firstname, self.lastname, self.email, self.phone, self.username, self.apassword,
              self.role, self.joindate)
            data = (self.adminid, self.firstname, self.lastname, self.email, self.phone, self.username, self.apassword,
                 self.role, self.joindate)
            insert_str = '''insert into admin(adminid,firstname,lastname,email,phone,username,apassword,role,joindate)
                               values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str,(data,))
            self.conn.commit()
            print('Records Inserted Successfully-----------')
            self.close()
            return True
        except Exception as e:
            print(f'Invalid Input:{e}')
            return False


    def UpdateAdmin(self,adminid,firstname,lastname,email,phone,username,apassword,role,joindate):
        try:

            self.adminid = int(input('Enter Adminid:'))
            self.firstname = input('Enter the firstname of admin:')
            self.lastname = input('Enter the lastname of admin:')
            self.email = input('Enter the email:')
            self.phone = input('Enter the phonenumber:')
            self.username = input('Enter the username:')
            self.apassword = input('Enter the password :')
            self.role = input('Enter the role of admin:')
            self.joindate = input('Enter the joindate:')
            update_str = 'update admin set firstname=%s,lastname=%s,email=%s,phone=%s,username=%s,apassword=%s,role=%s,joindate=%s where adminid=%s'
            self.open()
            data = ( self.firstname, self.lastname, self.email, self.phone, self.username, self.apassword,
                     self.role, self.joindate,self.adminid)
            self.stmt.executemany(update_str, (data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated  Successfully...')
            return True
        except Exception as e:
            print(f'Raised AdminNotFound:{e}')
            return False

    def DeleteAdmin(self,adminid):
        try:
            adminid = input('Enter the adminid:')
            delete_str = 'delete from admin where adminid=%s'
            self.open()
            self.stmt.execute(delete_str,(adminid,))
            self.conn.commit()
            print('Records Deleted Successfully....')
            return True
        except (AdminnotfoundExpection,AuthenicationException) as e:
            print(str(e))
            return False











