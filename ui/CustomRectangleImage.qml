import QtQuick

Rectangle {
    id: root
    property alias imageSource: img.source
    property alias fillMode: img.fillMode
    property alias radius: root.radius

    // Default to cropping to fill
    property bool stretch: false
    property bool fit: false

    onStretchChanged: {
        if (stretch) img.fillMode = Image.Stretch
    }
    onFitChanged: {
        if (fit) img.fillMode = Image.PreserveAspectFit
    }

    Image {
        id: img
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop // Default
    }
}
