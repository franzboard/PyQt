import QtQuick 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.0
import QtQuick.Controls.Material 2.0


ApplicationWindow {
    id: page
    width: 600
    height: 300
    visible: true
    title: "Raspberry Dashboard"

    ListModel {
        id: outputModel
        ListElement {devicetext: "LED 18"; deviceindex: "0"}
        ListElement {devicetext: "LED 23"; deviceindex: "1"}
        ListElement {devicetext: "LED 24"; deviceindex: "2"}
        ListElement {devicetext: "LED 25"; deviceindex: "3"}
    }

    ListModel {
        id: inputModel
        ListElement {devicetext: "BUTTON 22"; devcolor: "black"}
        ListElement {devicetext: "BUTTON 27"; devcolor: "black"}
        ListElement {devicetext: "BUTTON 17"; devcolor: "black"}
    }
    GridLayout {
        anchors.margins: 20
        anchors.fill: parent
        rows: 3
        columns: 2

        // CPU Temperature
        Text {color: "white"; text: "CPU Temperature:"; font.pointSize: 16}
        Text {id: temperature; color: "white"; text: "00"; font.pointSize: 16; Layout.alignment: Qt.AlignHCenter}

        // Outputs
        Text {color: "white"; text: "Outputs:"; font.pointSize: 16}
        Component {
            id: outputDelegate
            Button {
                text: devicetext
                highlighted: true
                Material.accent: Material.Blue
                onClicked: Material.accent = con.toggleLed(deviceindex)? Material.Red : Material.Blue
            }
        }

        RowLayout {
            ListView {
                width: 400
                height: 50
                spacing: 20
                orientation: ListView.Horizontal
                model: outputModel
                delegate: outputDelegate
            }
        }

        // inputs
        Text {color: "white"; text: "Inputs:"; font.pointSize: 16}
        Component {
            id: inputDelegate
            ColumnLayout {
                Text {color: "white"; text: devicetext ;horizontalAlignment: Text.AlignHCenter}
                Rectangle {
                    height:20
                    width:20
                    radius: 10
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    border.color: "gray"
                    border.width: 1
                    color: devcolor
                }
            }
        }

        RowLayout {
            ListView {
                width: 400
                height: 50
                spacing: 20
                orientation: ListView.Horizontal
                model: inputModel
                delegate: inputDelegate
            }
        }

    }
    Timer {
        interval: 300 // ms
        repeat: true
        running:true
        onTriggered: {
            temperature.text = con.getTemperature()
            inputModel.setProperty(0, "devcolor", con.readButton(0)? "red" : "black")
            inputModel.setProperty(1, "devcolor", con.readButton(1)? "red" : "black")
            inputModel.setProperty(2, "devcolor", con.readButton(2)? "red" : "black")
        }
    }
}
