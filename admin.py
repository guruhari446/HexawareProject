class admin:
    def __init__(self):
        self.adminid=''
        self.firstname=''
        self.lastname=''
        self.email=''
        self.phone=''
        self.username=''
        self.password=''
        self.role=''
        self.joindate=''
    # setter

    def setadminid(self,adminid):
        self.adminid=adminid
    def setfirstname(self,firstname):
        self.firstname=firstname
    def setlastname(self,lastname):
        self.lastname=lastname
    def setemail(self,email):
        self.email=email
    def setphone(self,phone):
        self.phone=phone
    def setusername(self,username):
        self.username=username
    def setpassword(self,password):
        self.password=password
    def setrole(self,role):
        self.role=role
    def setjoindate(self,joindate):
        self.joindate=joindate
    #getter
    def getadminid(self):
        return self.adminid
    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
    def getemail(self):
        return self.email
    def getphone(self):
        return self.phone
    def getusername(self):
        return self.username
    def getpassword(self):
        return self.password
    def getrole(self):
        return self.role
    def getjoindate(self):
        return self.joindate