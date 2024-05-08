from abc import ABC,abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def GetCustomerById(customerId):
        pass
    @abstractmethod
    def GetCustomerByUsername(username):
        pass
    @abstractmethod
    def RegisterCustomer(customerid,firstname,lastname,email,phone,address,username,password,registrationdate):
        pass
    @abstractmethod
    def UpdateCustomer(customerid,firstname,lastname,email,phone,address,username,password,registrationdate):
        pass
    @abstractmethod
    def DeleteCustomer(customerid):
        pass
        