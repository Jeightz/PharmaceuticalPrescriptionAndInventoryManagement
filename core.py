from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from userlogin.model.Button import Button
def core():

    app = QApplication([])
    engine = QQmlApplicationEngine()
    button = Button() 
    engine.rootContext().setContextProperty("loginButton", button)
    engine.load("PharmaceuticalPrescriptionAndInventoryManagement/ui/WindowFrame.qml")

    if not engine.rootObjects():
        print("ERROR: Failed to load QML file!")
        return -1
        
    app.exec()

if __name__ == "__main__":
    core()