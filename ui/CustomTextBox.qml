import QtQuick
import QtQuick.Controls

Rectangle {
    id: root
    width: 202
    height: 45
    radius: 10
    border.color: txtInput.activeFocus ? "green" : "black"
    border.width: 1
    color: "#d3d3d3"

    property string placeholderText: "Text Input"
    property bool isPassword: false
    property color normalBorderColor: "black"
    property color focusedBorderColor: "green"
    property color hoverBorderColor: "blue"
    property color pressedBorderColor: "darkblue"
    property string textchange : ""
    signal clicked()
    signal pressed()
    signal released()
    signal entered()
    signal exited()
    signal customtextChanged(string text)
    signal focusChanged(bool focused)
    signal returnPressed()

    Text {
        id: placeholder
        anchors.fill: parent
        anchors.margins: 8
        text: root.placeholderText
        color: "gray"
        font.pixelSize: 12
        verticalAlignment: Text.AlignVCenter
        visible: txtInput.text === ""
        elide: Text.ElideRight
    }

    Flickable {
        id: flick
        anchors.fill: parent
        anchors.margins: 8
        anchors.rightMargin: root.isPassword ? 30 : 8
        clip: true
        contentWidth: txtInput.contentWidth
        contentHeight: height
        interactive: false  // Disable user scrolling, just for clipping

        function ensureVisible(r) {
            if (contentX >= r.x)
                contentX = r.x;
            else if (contentX+width <= r.x+r.width)
                contentX = r.x+r.width-width;
        }

        TextInput {
            id: txtInput
            width: Math.max(flick.width, contentWidth)
            height: flick.height
            color: "black"
            font.pixelSize: 12
            verticalAlignment: TextInput.AlignVCenter
            echoMode: root.isPassword ? TextInput.Password : TextInput.Normal
            selectByMouse: true

            onTextChanged: {
                root.textchange = text;
                root.customtextChanged(text);
                flick.contentX = Math.max(0, contentWidth - flick.width)
            }
            onCursorRectangleChanged: flick.ensureVisible(cursorRectangle)
            onActiveFocusChanged: {
                root.focusChanged(activeFocus)
                if (activeFocus) {
                    flick.contentX = Math.max(0, contentWidth - flick.width)
                }
            }
            onAccepted: root.returnPressed()
        }
    }

    CheckBox {
        id: visibilityCheckbox
        anchors {
            right: parent.right
            verticalCenter: parent.verticalCenter
            rightMargin: 8
        }
        width: 20
        height: 20
        visible: root.isPassword && txtInput.text.length > 0
        indicator: Rectangle {
            implicitWidth: 16
            implicitHeight: 16
            border.color: visibilityCheckbox.down ? "green" : "black"
            border.width: 1
            radius: 3
            Rectangle {
                visible: visibilityCheckbox.checked
                color: "green"
                border.color: "black"
                radius: 20
                anchors.margins: 3
                anchors.fill: parent
            }
        }
        ToolTip.visible: hovered
        ToolTip.text: checked ? "Hide password" : "Show password"
        
        onCheckedChanged: {
            txtInput.echoMode = checked ? TextInput.Normal : TextInput.Password
        }
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true
        onClicked: {
            root.clicked()
            txtInput.forceActiveFocus()
        }
        onPressed: root.pressed()
        onReleased: root.released()
        onEntered: root.entered()
        onExited: root.exited()
    }

    states: [
        State {
            name: "HOVERED"
            when: mouseArea.containsMouse && !mouseArea.pressed
            PropertyChanges { target: root; border.color: root.hoverBorderColor }
        },
        State {
            name: "PRESSED"
            when: mouseArea.pressed
            PropertyChanges { target: root; border.color: root.pressedBorderColor }
        }
    ]

    transitions: Transition {
        ColorAnimation { duration: 150 }
    }
}