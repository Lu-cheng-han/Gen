from PySide6.QtCore import QObject, Signal, Slot, Property, qDebug, Qt, QDir, qDebug, QFile,QTimer,QIODevice,QIODeviceBase
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
from PySide6.QtQml import QmlElement, QmlSingleton

class SerialPortParam:

    def __init__(self, port_name, baud_rate, data_bits = None) -> None:
        self.port_name = port_name
        self.baud_rate = baud_rate
        self.data_bits = data_bits


class SerialWorker(QSerialPort):

    opened = Signal(bool)
    response = Signal(str)
    error_occurred = Signal(QObject)
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @Slot()
    def open(self, param: SerialPortParam):
        if super().isOpen():
            super().close()

        port_name = param.port_name
        baud_rate = param.baud_rate
        self.setPortName(port_name)
        self.setBaudRate(baud_rate)

        if param.data_bits != None:
            data_bits = param['data_bits']
            self.setDataBits(data_bits)

        result = super().open(QIODeviceBase.OpenModeFlag.ReadWrite)

        if result:
            self.opened.emit(result)
            print(f'{port_name} open successful')
        else:
            print(f'{port_name} open fail')

        return result

    @Slot()
    def close(self):
        if super().isOpen():
            super().close()
        