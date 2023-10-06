import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Row {
    Image {
        source: "qrc:/data/icons/red_circle.png"
        height: parent.height 
        width: parent.height
        asynchronous: true
        fillMode: Image.PreserveAspectFit 
    }
    ComboBox {
        hoverEnabled: false
        height: parent.height
        width: parent.width / 2
    }
    Button {
        height: parent.height
        width: parent.width / 5
        text: "OK"
        onClicked: {
        }
    }
}



