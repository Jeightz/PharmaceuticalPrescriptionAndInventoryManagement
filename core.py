from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from userlogin.userlogin_controller import UserLoginController 
def core():

    app = QApplication([])
    engine = QQmlApplicationEngine()
    controller = UserLoginController()
    engine.rootContext().setContextProperty("userlogincontroller", controller)
    engine.load("PharmaceuticalPrescriptionAndInventoryManagement/ui/WindowFrame.qml")

    if not engine.rootObjects():
        print("ERROR: Failed to load QML file!")    
        return -1
        
    app.exec()

if __name__ == "__main__":
    core()