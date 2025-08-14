from PySide6.QtCore import QObject, Signal, Slot
from .userlogin_Model import checkDataInputed as check
from .userlogin_DAO import UserLoginDAO as DAO  
class UserLoginController(QObject):
    login_success = Signal(str)
    login_failed = Signal(str)
      
    def __init__(self):
        super().__init__()
        self._username = ""
        self._password = ""


    @Slot()
    def login(self,username,password):
        self._username = username
        self._password = password
        
        if not self._authenticate():
            self.login_failed.emit("Invalid Inputed Username and Password.")
            return
        login = DAO.login_authentication(self._username, self._password)
        
        if login is True:
            print("successfull")

        
    def _authenticate(self):
        check.checkDataInputed(self._username, self._password)