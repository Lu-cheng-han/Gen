from PySide6.QtCore import QObject, Signal, Slot, Property, qDebug, Qt, QDir, qDebug, QFile,QTimer,QIODevice
from PySide6.QtSerialPort import QSerialPortInfo
from PySide6.QtQml import QmlElement, QmlSingleton


QML_IMPORT_NAME = 'system'
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
@QmlSingleton
class PortController(QObject):

    result = False
    _port=[]

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_available_port)
        self.timer.start(500)

        
    @Slot(result=list)
    def get_port(self):
        return self._port
    port_list_changed = Signal()
    port_list = Property(list, get_port, notify = port_list_changed)
    
    @Slot(result=list)
    def get_available_port(self):
        available_ports = QSerialPortInfo.availablePorts()
        for port in available_ports:
            if port.portName() not in self._port:
                self._port.append(port.portName())
                self.port_list_changed.emit()
        