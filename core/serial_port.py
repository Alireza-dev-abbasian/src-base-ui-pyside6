from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort

class SerialPort:
    
    def get_serial_ports_info():
        ports = QSerialPortInfo.availablePorts()
        port_list = [
            {'name': port.portName(), 'description': port.description()}for port in ports
        ]
        return port_list
    
    def connect_to_serial_port(port_name, baud_rate=QSerialPort.BaudRate.Baud115200, 
                                data_bits=QSerialPort.DataBits.Data8, parity=QSerialPort.Parity.NoParity,
                                stop_bits=QSerialPort.StopBits.OneStop, flow_control=QSerialPort.FlowControl.NoFlowControl):
        
        serial_port = QSerialPort(port_name)
        message = ''

        try:
            if not serial_port.isOpen():
                serial_port.setPortName(port_name)
                serial_port.setBaudRate(baud_rate)
                serial_port.setDataBits(data_bits)
                serial_port.setParity(parity)
                serial_port.setStopBits(stop_bits)
                serial_port.setFlowControl(flow_control)

                if not serial_port.open(QSerialPort.ReadWrite):
                    raise Exception(f"Failed to open {port_name}")
                else:
                    message = f"Connected to {port_name}"
                    return True, message
                
            else:
                message = f"Serial port {port_name} is already open."
                return True, message
                        
        except Exception as e:
            message = f"Serial Port Error: {e}"
            return False, message
