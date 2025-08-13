import QtQuick
import QtQuick.Controls

Button {
    id: control
    width: 120
    height: 40

    property color normalColor: "#4CAF50"
    property color hoverColor: "#45a049"
    property color pressedColor: "#2E7D32"
    property color textColor: "white"
    property int borderRadius: 20
    property string textplaceholder: "Text Input"
    property string bordercolor:"black"

   signal mouseEntered()
    signal mouseExited()
    signal mousePressed()
    signal mouseReleased()
    signal mouseClicked()
    signal mouseHovered()
    signal mouseUnhovered()

    contentItem: Text {
        text: control.textplaceholder
        color: textColor
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.pixelSize: 14
        font.bold: true
    }

    background: Rectangle {
        id: bg
        radius: borderRadius
        color: control.normalColor
        border.color: control.bordercolor

    }
// Replace the default mouse handling
    MouseArea {
        anchors.fill: parent
        hoverEnabled: true
        
        onEntered: control.mouseEntered()
        onExited: control.mouseExited()
        onPressed: control.mousePressed()
        onReleased: control.mouseReleased()
        onClicked: control.mouseClicked()
    }
       Component.onCompleted: {
           control.onClicked = undefined
       }
}
