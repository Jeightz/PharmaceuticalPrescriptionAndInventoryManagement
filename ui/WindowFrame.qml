
    import QtQuick
    import QtQuick.Window
    Window {
        id: mainWindow
        width: mainScreen.width
        height: mainScreen.height
        
        FontLoader {

            id: lemonMilkBold
            source: "fonts/LEMONMILK-Bold.otf"


        }
        
        readonly property string fontBold: lemonMilkBold.status === FontLoader.Ready ? lemonMilkBold.name : "Arial"

        visible: true
        title: "UntitledProject"

        flags: Qt.Window | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint
        minimumWidth: mainScreen.width
        minimumHeight: mainScreen.height
        maximumWidth: mainScreen.width
        maximumHeight: mainScreen.height


        UserLogin{
            id: mainScreen
            anchors.fill: parent
            Component.onCompleted: console.log("UserLogin component loaded")
           
        }
            
        
    }
