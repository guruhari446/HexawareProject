from abc import ABC,abstractmethod

class IReservationService(ABC):
    @abstractmethod
    def GetReservationById(reservationId):
        pass
    @abstractmethod
    def GetReservationByCustomerId(customerid):
        pass
    @abstractmethod
    def CreateReservation(reservationid,customerid,vehicleid,startdate,enddate,totalcost,cstatus):
        pass
    @abstractmethod
    def UpdateReservation(reservationid,customerid,vehicleid,startdate,enddate,totalcost,cstatus):
        pass
    @abstractmethod
    def CancelReservation(reservationid):
        pass

