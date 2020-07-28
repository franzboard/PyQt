import QtQuick 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.0
import QtQuick.Controls.Material 2.0


ApplicationWindow {
    id: page
    width: 500
    height: 300
    visible: true
    title: "OneTwoThree"


    GridLayout {
        anchors.margins: 20
        anchors.fill: parent
        rows: 2
        columns: 1

        // Time display
        Text {id: timedisplay; color: "white"; text: "00:00:000"; font.pointSize: 36; Layout.alignment: Qt.AlignHCenter}

        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            spacing: 20
            Button {
                text: "START"
                highlighted: true
                Material.accent: Material.Blue
                onClicked: {

                    stopwatch.start()
                }
            }
            Button {
                text: "STOP"
                highlighted: true
                Material.accent: Material.Blue
                onClicked: {

                    stopwatch.stop()
                }
            }

        }
    }
    Connections {
        target: stopwatch
        onNewTime: timedisplay.text = displayTime;
    }

}
