from PySide6.QtCore import Signal, Slot, QObject, QTimer, Qt, qDebug, qCritical, QCoreApplication
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from queue import Queue
class SerialPortParam:

    port_name: str #ex: COM1
    baud_rate: int #ex: 115200 、9600
    data_bits: QSerialPort.DataBits


class SerialPortWorker(QSerialPort):

    opened = Signal(bool)
    response = Signal(str)


    def __init__(self) -> None:
        super().__init__()
        self.init_queue()
            
    def init_queue(self):
        self.queue = Queue()
        self.request_map = {}
    
    def put_queue(self, request):
        self.queue.put(request)

    def open(self, param : 'SerialPortParam'):
        if self.isOpen():
            self.close()

        self.setPortName(param.port_name)
        self.setBaudRate(param.baud_rate)

        if param.get('data_bits'):
            self.setDataBits(param.data_bits)
        
        if self.open(QSerialPort.ReadWrite):
            qDebug(f"{param.port_name} open sucessful")
        else:
            qDebug(f'{param.port_name} open failed')


        


