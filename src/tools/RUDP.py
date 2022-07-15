import socket
import pickle
import sys
import _thread
import threading

import src.services.RTTService as rtt
from src.config.Settings import Settings


class RUDPDatagram:
    timestamp: float
    sequence_no: int
    payload: bytes

    def __init__(self, **kwargs):
        self.payload = kwargs["payload"]
        self.address = kwargs["address"]
        self.sequence_no = kwargs["sequence_no"]
        self.timestamp = kwargs["timestamp"]
        self.BUFFER_SIZE = Settings.BUFFER_SIZE
        


class RUDPServer:
    def __init__(self, port: int, debug: bool = False):
        self.__debug = debug
        self.BUFFER_SIZE = Settings.BUFFER_SIZE

        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.__socket.bind(("0.0.0.0", port))
        except:
            print("Couldn't initialise server", file=sys.stderr)
            sys.exit(1)

    def receive(self):
        message, address = self.__socket.recvfrom(self.BUFFER_SIZE)
        datagram = pickle.loads(message)

        self.__last_seqno = datagram.sequence_no
        self.__last_ts = datagram.timestamp

        return (datagram.payload, address)

    def reply(self, address, payload: bytes):
        datagram = RUDPDatagram(payload=payload, address=address,
                                sequence_no=self.__last_seqno, timestamp=self.__last_ts)
        serialised_datagram = pickle.dumps(datagram)
        self.__socket.sendto(serialised_datagram, address)


class RUDPClient:
    def __init__(self, hostname: str, port: int):
        self.__hostname = hostname
        self.__port = port
        self.__sequence_no = 0
        self.__rtt = rtt.RTTService()
        self.BUFFER_SIZE = Settings.BUFFER_SIZE

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.setblocking(False)
        except:
            print("Couldn't initialise client", file=sys.stderr)
            sys.exit(1)

    def send_recv(self, payload: bytes):
        timestamp = self.__rtt.timestamp()
        datagram = RUDPDatagram(
            address=(self.__hostname, self.__port),
            payload=payload, sequence_no=self.__sequence_no, timestamp=timestamp)
        serialised_datagram = pickle.dumps(datagram)

        self.__rtt.new_packet()

        event = threading.Event()

        def timeout():
            print("timeout")
            if self.__rtt.timeout():
                _thread.interrupt_main()
            else:
                event.set()

        response = None
        attempting_send = True
        while attempting_send:
            event.clear()
            self.socket.sendto(serialised_datagram,
                               (self.__hostname, self.__port))

            timer = threading.Timer(self.__rtt.start(), timeout)
            timer.start()

            datagram = None
            while True:
                try:
                    if event.wait(timeout=0.05):
                        break
                    message = self.socket.recv(self.BUFFER_SIZE)
                    response = pickle.loads(message)
                except BlockingIOError:
                    continue

                if response.sequence_no == self.__sequence_no:
                    attempting_send = False
                    break

        timer.cancel()
        self.__rtt.stop(self.__rtt.timestamp() - response.timestamp)

        return response.payload