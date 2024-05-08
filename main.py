from dao.Implement import Implement
class main:
    def __init__(self):
        self.use=Implement()
    def run(self):
        while True:
            print("CarConnect Application Menu")
            print("1.GetCustomerById")
            print("2.GetCustomerByUsername")
            print("3.RegisterCustomer")
            print("4.UpdateCustomer")
            print("5.DeleteCustomer")
            print("6.GetVehicleById")
            print("7.GetAvailableVehicles")
            print("8.AddVehicle")
            print("9.UpdateVehicle")
            print("10.RemoveVehicle")
            print("11.GetReservationById")
            print("12.GetReservationsByCustomerId")
            print("13.CreateReservation")
            print("14.UpdateReservation")
            print("15.CancelReservation")
            print("16.GetAdminById")
            print("17.RegisterAdmin")
            print("18.UpdateAdmin")
            print("19.DeleteAdmin")
            print("20.GetAdminByUsername")
            choice=int(input("Enter Your Purpose choice(1-20):"))
            if(choice ==1):
               customerId=int(input('Enter the customerid:'))
               if self.use.GetCustomerById(customerId): #1.GetCustomerById
                   print("Customer is displayed successfully")
               else:
                   print("Error occured")
            elif(choice ==2):
               username=input('Enter the username:')
               if self.use.GetCustomerByUsername(username):     #GetCustomerByUsername
                   print("Customer is displayed successfully")
               else:
                   print("Error occured")
            elif(choice ==3):
                customerid=''
                firstname=''
                lastname=''
                email=''
                phone=''
                address=''
                username=''
                password=''
                registrationdate=''

                if self.use.RegisterCustomer(customerid, firstname, lastname, email, phone, address, username, password, registrationdate):       #RegisterCustomer
                   print("Registered successfully")
                else:
                    print("Error Occured")
            elif(choice ==4):
                customerid = ''
                firstname = ''
                lastname = ''
                email = ''
                phone = ''
                address = ''
                username = ''
                password = ''
                registrationdate=''

                if self.use.UpdateCustomer(customerid,firstname,lastname,email,phone,address,username,password,registrationdate):
                    print("Updated Successfully")
                else:
                    print("Error Occured")
            elif(choice ==5):
                customerid = ''
                if self.use.DeleteCustomer(customerid):
                    print("Deleted successfully")
                else:
                    print("Error occured")
            elif(choice ==6):
                vehicleid=int(input('Enter the vehicleid:'))
                if self.use.GetVehicleById(vehicleid):
                    print("Vehicle is displayed successfully")
                else:
                    print("Error Occured")
            elif(choice ==7):
                vehicleid=int(input('Enter the vehicleid:'))
                if self.use.GetAvailableVehicle(vehicleid):
                    print("Availability is Displayed")
                else:
                    print("Error Occured")
            elif(choice == 8):
                vehicleid = ''
                model = ''
                make = ''
                cyear = ''
                color = ''
                registrationnum = ''
                avaliability =''
                dailyrate =''

                if self.use.AddVehicle(vehicleid,model,make,cyear,color,registrationnum,avaliability,dailyrate):
                    print("Vehicle row is added")
                else:
                    print("Error Occured")
            elif(choice ==9):
                vehicleid = ''
                model = ''
                make = ''
                cyear = ''
                color = ''
                registrationnum = ''
                avaliability = ''
                dailyrate = ''

                if self.use.UpdateVehicle(vehicleid, model, make, cyear, color, registrationnum, avaliability, dailyrate):
                    print("Updated successfully")
                else:
                    print("Error Occured")
            elif(choice ==10):
                vehicleid =''
                if self.use.RemoveVehicle(vehicleid):
                    print("Vehicle Row is deleted")
                else:
                    print("Error Occured")
            elif(choice ==11):
                reservationid=int(input('Enter the Reservation Id:'))
                if self.use.GetReservationById(reservationid):
                    print("Reservation is successfully displayed")
                else:
                    print("Error Ocured")
            elif(choice ==12):
                customerid=int(input('Enter the customer id:'))
                if self.use.GetReservationByCustomerid(customerid):
                    print("Reservation is Successfully displayed")
                else:
                    print("Error Occured")
            elif(choice ==13):
                reservationid = ''
                customerid = ''
                vehicleid = ''
                startdate = ''
                enddate = ''
                totalcost = ''
                cstatus = ''

                if self.use.CreateReservation(reservationid,customerid,vehicleid,startdate,enddate,totalcost,cstatus):
                    print("Reservation is successfully")
                else:
                    print("Error Occured")
            elif(choice ==14):
                reservationid = ''
                customerid = ''
                vehicleid = ''
                startdate = ''
                enddate =''
                totalcost = ''
                cstatus = ''

                if self.use.UpdateReservation(reservationid,customerid,vehicleid,startdate,enddate,totalcost,cstatus):
                    print("Reservation is updated")
                else:
                    print("Error Occured")
            elif(choice ==15):
               reservationid = ''
               if self.use.CancelReservation(reservationid):
                    print("Reservation is Cancelled")
               else:
                    print("Error Occured")
            elif(choice ==16):
                adminid=int(input('Enter the adminid:'))
                if self.use.GetAdminById(adminid):
                    print("Admin is displayed successfully")
                else:
                    print("Error Occured")
            elif(choice ==17):
                adminid = ''
                firstname = ''
                lastname = ''
                email = ''
                phone = ''
                username = ''
                apassword = ''
                role = ''
                joindate = ''

                if self.use.RegisterAdmin(adminid,firstname,lastname,email,phone,username,apassword,role,joindate):
                    print("Admin Registered successfully")
                else:
                    print("Error Occured")
            elif(choice ==18):
                adminid = ''
                firstname = ''
                lastname = ''
                email = ''
                phone = ''
                username = ''
                apassword = ''
                role = ''
                joindate = ''

                if self.use.UpdateAdmin(adminid,firstname,lastname,email,phone,username,apassword,role,joindate):
                    print("Admin updated successfully")
                else:
                    print("Error Occured")
            elif(choice ==19):
                adminid=''
                if self.use.DeleteAdmin(adminid):
                    print("Deleted Admin successfully")
                else:
                    print("Error Occured")

            elif(choice ==20):
                username=input('Enter the Username:')
                if self.use.GetAdminByUsername(username):
                    print("Admin is displayed successfully")
                else:
                    print("Error Occured")

            else:
                print("Invalid choice.Please Try Later")

obj1=main()
obj1.run()


