/*!
    \qmltype CustomTextBox
    /*!
        \qmltype CustomTextBox
    */
    // Note: Each line below has a short, simple comment on the right side to explain it.  // (Helps you read each line.)

    import QtQuick           // (Brings in basic building blocks for the UI.)
    import QtQuick.Controls  // (Brings in ready-made controls like TextInput and CheckBox.)

    Rectangle { id: root                         // (This is the outer box that holds everything.)
        width: 202                               // (How wide the box is.)
        height: 45                               // (How tall the box is.)
        radius: 10                               // (Rounded corners size.)
        border.color: txtInput.activeFocus ? "green" : "black"  // (Green border when typing, otherwise black.)
        border.width: 1                          // (Thickness of the border.)
        color: "#d3d3d3"                         // (Background color of the box.)

        property string placeholderText: "Text Input"  // (Gray hint text when empty.)
        property bool isPassword: false                // (If true, show dots instead of characters.)
        property color normalBorderColor: "black"      // (Normal border color.)
        property color focusedBorderColor: "green"     // (Border color when focused.)
        property color hoverBorderColor: "blue"        // (Border color when mouse is over.)
        property color pressedBorderColor: "darkblue"  // (Border color while clicking.)
        property string textchange : ""                // (Holds current text as a string.)
        signal clicked()                               // (Sends a message when clicked.)
        signal pressed()                               // (Sends a message when pressed down.)
        signal released()                              // (Sends a message when released.)
        signal entered()                               // (Sends a message when mouse enters.)
        signal exited()                                // (Sends a message when mouse leaves.)
        signal customtextChanged(string text)          // (Sends new text when it changes.)
        signal focusChanged(bool focused)              // (Sends true/false when focus changes.)
        signal returnPressed()                         // (Sends a message when Enter is pressed.)

        Text { id: placeholder                         // (This shows the placeholder hint.)
            anchors.fill: parent                       // (Fill the whole box so text is centered.)
            anchors.margins: 8                         // (Space between text and the box edge.)
            text: root.placeholderText                 // (Use the placeholderText property.)
            color: "gray"                              // (Make the hint gray.)
            font.pixelSize: 12                         // (Text size.)
            verticalAlignment: Text.AlignVCenter       // (Center the text vertically.)
            visible: txtInput.text === ""              // (Only show when the input is empty.)
            elide: Text.ElideRight                     // (Cut off and add ... if too long.)
        }

        Flickable { id: flick                          // (Allows scrolling the text if it's too long.)
            anchors.fill: parent
            anchors.margins: 8
            anchors.rightMargin: root.isPassword ? 30 : 8  // (Make room for the visibility checkbox when password.)
            clip: true                                // (Hide anything outside the area.)
            contentWidth: txtInput.contentWidth      // (How wide the content inside is.)
            contentHeight: height                    // (Content height set to the box height.)
            interactive: false                       // (User can't scroll by dragging; it's just for clipping.)

            function ensureVisible(r) {               // (Make sure the cursor is visible by changing contentX.)
                if (contentX >= r.x)
                    contentX = r.x;
                else if (contentX+width <= r.x+r.width)
                    contentX = r.x+r.width-width;
            }

            TextInput { id: txtInput                   // (This is the actual place you type.)
                width: Math.max(flick.width, contentWidth)  // (Width grows with content.)
                height: flick.height                   // (Same height as the flickable area.)
                color: "black"                         // (Typed text color.)
                font.pixelSize: 12                     // (Text size.)
                verticalAlignment: TextInput.AlignVCenter // (Center text vertically.)
                echoMode: root.isPassword ? TextInput.Password : TextInput.Normal // (Hide text if password.)
                selectByMouse: true                    // (Allow selecting text with mouse.)

                onTextChanged: {                       // (When the text changes run this.)
                    root.textchange = text;            // (Store the current text in our property.)
                    root.customtextChanged(text);     // (Emit a signal saying the text changed.)
                    flick.contentX = Math.max(0, contentWidth - flick.width) // (Scroll to end if needed.)
                }
                onCursorRectangleChanged: flick.ensureVisible(cursorRectangle) // (Keep the cursor visible.)
                onActiveFocusChanged: {                // (When the input gains/loses focus.)
                    root.focusChanged(activeFocus)     // (Emit focusChanged with true/false.)
                    if (activeFocus) {
                        flick.contentX = Math.max(0, contentWidth - flick.width) // (Scroll to show end when focused.)
                    }
                }
                onAccepted: root.returnPressed()       // (Emit returnPressed when Enter is hit.)
            }
        }

        CheckBox { id: visibilityCheckbox             // (Small box to show/hide password.)
            anchors {
                right: parent.right                   // (Put it at the right edge of the box.)
                verticalCenter: parent.verticalCenter // (Center it vertically.)
                rightMargin: 8                        // (Small gap from the edge.)
            }
            width: 20                                 // (Size of the checkbox.)
            height: 20
            visible: root.isPassword && txtInput.text.length > 0  // (Show only for password with text.)
            indicator: Rectangle {                     // (Custom look for the checkbox indicator.)
                implicitWidth: 16
                implicitHeight: 16
                border.color: visibilityCheckbox.down ? "green" : "black" // (Green border when pressed.)
                border.width: 1
                radius: 3
                Rectangle {                             // (Inner rectangle that shows checked state.)
                    visible: visibilityCheckbox.checked
                    color: "green"
                    border.color: "black"
                    radius: 20
                    anchors.margins: 3
                    anchors.fill: parent
                }
            }
            ToolTip.visible: hovered                    // (Show tooltip when hovering.)
            ToolTip.text: checked ? "Hide password" : "Show password" // (Tooltip text toggles.)

            onCheckedChanged: {                        // (When checkbox changes do this.)
                txtInput.echoMode = checked ? TextInput.Normal : TextInput.Password // (Toggle echo mode.)
            }
        }

        MouseArea { id: mouseArea                      // (Area that detects mouse clicks and hover.)
            anchors.fill: parent
            hoverEnabled: true                         // (We want mouse enter/exit events.)
            onClicked: {
                root.clicked()                         // (Emit clicked signal.)
                txtInput.forceActiveFocus()            // (Focus the text input so the user can type.)
            }
            onPressed: root.pressed()                  // (Emit pressed when mouse button down.)
            onReleased: root.released()                // (Emit released when mouse button up.)
            onEntered: root.entered()                  // (Emit entered when mouse comes in.)
            onExited: root.exited()                    // (Emit exited when mouse leaves.)
        }

        states: [                                      // (Visual states to change border color.)
            State {
                name: "HOVERED"
                when: mouseArea.containsMouse && !mouseArea.pressed // (When mouse is over but not pressing.)
                PropertyChanges { target: root; border.color: root.hoverBorderColor } // (Use hover color.)
            },
            State {
                name: "PRESSED"
                when: mouseArea.pressed               // (When mouse button is down inside.)
                PropertyChanges { target: root; border.color: root.pressedBorderColor } // (Use pressed color.)
            }
        ]

        transitions: Transition {                      // (Make color changes animate smoothly.)
            ColorAnimation { duration: 150 }           // (Animation takes 150 milliseconds.)
        }
    }  // End of Rectangle (the whole custom text box)  // (This closes the big box.)

