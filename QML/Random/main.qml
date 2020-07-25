import QtQuick 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.0

Window {
    id: root
    width: 640
    height: 480
    visible: true
    title: "Random"

    RowLayout {
        Button {
            text: "Give me a number!"
            onClicked: numbergenerator.giveNumber();
        }

        Text {
            id: numberLabel
            text: "no number"
        }
    }
    
    Connections {
        target: numbergenerator
        onNextNumber: numberLabel.text = giveNumber
    }
}
