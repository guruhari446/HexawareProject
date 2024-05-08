class vehicle1:
    def __init__(self):
        self.vehicleid=''
        self.model=''
        self.make=''
        self.cyear=''
        self.color=''
        self.registrationnum=''
        self.avaliability=''
        self.dailyrate=''
    #setter
    def setvehicleid(self,vehicleid):
        self.vehicleid=vehicleid
    def setmodel(self,model):
        self.model=model
    def setmake(self,make):
        self.make=make
    def setcyear(self,cyear):
        self.cyear=cyear
    def setcolor(self,color):
        self.color=color
    def setregistrationnum(self,registrationnum):
        self.registrationnum=registrationnum
    def setavaliability(self,avaliability):
        self.avaliability=avaliability
    def setdailyrate(self,dailyrate):
        self.dailyrate=dailyrate
    #getter
    def getvehicleid(self):
        return self.vehicleid
    def getmodel(self):
        return self.model
    def getmake(self):
        return self.make
    def getcyear(self):
        return self.cyear
    def getcolor(self):
        return self.color
    def getregistrationnum(self):
        return self.registrationnum
    def getavaliability(self):
        return self.avaliability
    def getdailyrate(self):
        return self.dailyrate
