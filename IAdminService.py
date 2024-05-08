from abc import ABC,abstractmethod

class IAdminService(ABC):
    @abstractmethod
    def GetAdminById(adminid):
        pass
    @abstractmethod
    def GetAdminByUsername(username):
        pass
    @abstractmethod
    def RegisterAdmin(adminid,firstname,lastname,email,phone,username,password,role,joindate):
        pass
    @abstractmethod
    def UpdateAdmin(adminid,firstname,lastname,email,phone,username,password,role,joindate):
        pass
    @abstractmethod
    def DeleteAdmin(adminid,firstname,lastname,email,phone,username,password,role,joindate):
        pass
