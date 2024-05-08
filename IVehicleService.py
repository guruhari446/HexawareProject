from abc import ABC,abstractmethod

class IVehicleService(ABC):
    @abstractmethod
    def GetVehicleById(vehicleid):
        pass
    @abstractmethod
    def GetAvaliabileVehicle(self):
        pass
    @abstractmethod
    def AddVehicle(vehicleid,model,make,cyear,color,registrationnum,avaliability,dailyrate):
        pass
    @abstractmethod
    def UpdateVehicle(vehicleid,model,make,cyear,color,registrationnum,avaliability,dailyrate):
        pass
    @abstractmethod
    def RemoveVehicle(vehicleid):
        pass