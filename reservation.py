class reservation:
    def __init__(self):
        self.reservationid=''
        self.customerid=''
        self.vehicleid=''
        self.startdate=''
        self.enddate=''
        self.totalcost=''
        self.cstatus=''
    # setter
    def setreservationid(self,reservationid):
        self.reservationid=reservationid
    def setcustomerid(self,customerid):
        self.customerid=customerid
    def setvehicleid(self,vehicleid):
        self.vehicleid=vehicleid
    def setstartdate(self,startdate):
        self.startdate=startdate
    def setenddate(self,enddate):
        self.enddate=enddate
    def settotalcost(self,totalcost):
        self.totalcost=totalcost
    def setstatus(self,cstatus):
        self.cstatus=cstatus
    # getter
    def getreservationid(self):
        return self.reservationid
    def getcustomerid(self):
        return self.customerid
    def getvehicleid(self):
        return self.vehicleid
    def getstartdate(self):
        return self.startdate
    def getenddate(self):
        return self.enddate
    def gettotalcost(self):
        return self.totalcost
    def getstatus(self):
        return self.cstatus
