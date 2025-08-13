from PySide6.QtCore import QObject, Signal, Slot

class Button(QObject):
    clicked = Signal()
    def __init__(self):
        super().__init__()

    @Slot()
    def click(self):
        print("Login button clicked! (No credentials checked)")
        print("Simulating successful login...")
