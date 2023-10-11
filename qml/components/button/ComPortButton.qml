import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


RowLayout {
    id: idRowLayoutComPort 
    property alias idButtonRed: idButtonRed
    property alias idComboBoxPort : idComboBoxPort 
    signal open()

    Image {
        id: idButtonRed
        source: "qrc:/data/icons/red_circle.png"
        asynchronous: true
        Layout.preferredHeight: parent.height
        Layout.preferredWidth: parent.height
        fillMode: Image.PreserveAspectFit 
    }
    ComboBox {
        id: idComboBoxPort
        hoverEnabled: false
        Layout.fillWidth: true
    }
    Button {
        id: idButtonOpenPort
        text: "Open"
        onClicked: {
            idRowLayoutComPort.open()
        }
    }
}



