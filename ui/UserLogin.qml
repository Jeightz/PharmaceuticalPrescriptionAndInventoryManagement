import QtQuick
import QtQuick.Controls

Rectangle {
    id: userlogin
    width: 700
    height: 500

    Connections {
        target: userlogincontroller
        function onLogin_success(message) {
            console.log("Login success:", message)
            // Handle navigation here
            stackView.push("Dashboard.qml")
        }
        function onLogin_failed(error) {
            console.log("Login failed:", error)
            errorText.text = error
            errorText.visible = true
        }
    }
    Rectangle {
        id: panelloginholder
        x: 0
        y: 0
        width: 356
        height: 500
        color: "#ffffff"

        CustomTextBox {
            id: passwordinput
            x: 72
            y: 200
            placeholderText: "Password"
            isPassword: true
        }

        CustomTextBox {
            id: usernameinput
            x: 72
            y: 120
            placeholderText: "Username"
        }
        CustomButton {
            id: btnlogin
            x: 72
            y: 264
            width: 202
            height: 52
            textplaceholder: "Login"
            onMouseEntered: console.log("Mouse entered")
            onMouseExited: console.log("Mouse exited")
            onMousePressed: console.log("Mouse pressed")
            onMouseReleased: console.log("Mouse released")
            onMouseClicked: {
                var username = usernameinput.textchange;
                var password = passwordinput.textchange;
                userlogincontroller.login(username,password);
            }
        }
    }

    Rectangle {
        id: panelAD
        x: 354
        y: 0
        width: 346
        height: 500
        color: "#4caf50"
        border.color: "#4caf50"

       CustomRectangleImage {
            x: 0
            y: 108
            width: 346
            height: 332
            radius: 10
            imageSource: "pictures/pharmacy.png"
            color: "#4caf50"
            border.color: "#4caf50"
            stretch: true
        }

        Text {
            id: text1
            x: 15
            y: 26
            width: 151
            height: 18
            color: "#ffffff"
            text: "Pharmaceutical Prescription"
            font.family: fontBold
            font.pixelSize: 17
        }

        Text {
            id: text2
            x: 156
            y: 50
            width: 35
            height: 20
            color: "#ffffff"
            text: "and"
            font.pixelSize: 17
            font.family: fontBold
        }
    }

    Text {
        id: text3
        x: 411
        y: 73
        width: 151
        height: 42
        color: "#ffffff"
        text: "Inventory Management"
        font.pixelSize: 17
        font.family: fontBold
    }

}
