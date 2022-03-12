import datetime
import socket
import cv2
import numpy
from PIL import Image
import io
from multiprocessing import Process, Queue
import threading
from SelfieSegMNV2 import SelfieSegMNV2

HOST = ""  # Standard loopback interface address (localhost)
PORT = 12345  # Port to listen on (non-privileged ports are > 1023)
ACK = bytearray([0x96])
frames = Queue()
is_connected = False

def starttime():
    return datetime.datetime.now()

def endtime(stime=0, show=False):
    etime = datetime.datetime.now() - stime
    if show:
        print("Elpased(ms): " + str(int(etime.total_seconds() * 1000)))
    return int(etime.total_seconds()*1000)

#"""
def cam_server_proc():
    global is_connected

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)

        print("Server Listening ", PORT)
        is_connected = True

        while is_connected:
            conn, addr = s.accept()
            print(f"Connected by {addr}")

            while is_connected:
                chunks = []
                # print("Request Capture!!")
                conn.send(ACK)
                while is_connected:
                    data = conn.recv(1024)
                    if data:
                        # print("Received", len(data))
                        chunks += list(data)
                        # print("Last(2) = %02x %02x" % (int(chunks[-2]), int(chunks[-1])))
                        if chunks[-1] == 0xD9 and chunks[-2] == 0xFF:
                            #print("Received EOF (%d)" % len(chunks))

                            # """
                            stream = io.BytesIO(bytes(chunks))
                            img = Image.open(stream)
                            img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
                            frames.put(img)
                            """
                            cv2.imshow("Captured", img)
                            if cv2.waitKey(1) == 27:
                                conn.close()
                                cv2.destroyAllWindows()
                                is_connected = False
                                exit()
                                break
                            #"""
                            break

                    # conn.sendall(data)

#process = Process(target=cam_server_proc, args=())
process = threading.Thread(target=cam_server_proc, args=())
process.start()
#"""

width = 320
height = 240
seg = SelfieSegMNV2(width, height)

# Load and resize the background image
bgd = cv2.imread('./images/background.jpeg')
bgd = cv2.resize(bgd, (width, height))

stime = starttime()
count = 0
while cv2.waitKey(1) != 27:
    if not frames.empty():
        elapsed = endtime(stime) / 1000
        count += 1
        img = frames.get(True)

        # f = open("./captures/%d.jpeg" % count, "wb")
        # f.write(bytes(chunks))
        # f.close()

        # TODO: Segmentation
        # Get segmentation mask
        mask = seg.seg(img)
        # Merge with background
        fg = cv2.bitwise_or(img, img, mask=mask)
        bg = cv2.bitwise_or(bgd, bgd, mask=~mask)
        img = cv2.bitwise_or(fg, bg)

        # Show image
        cv2.putText(img, "FPS %0.2f" % (count / elapsed), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, 2)
        cv2.imshow("Captured", img)

is_connected = False
cv2.destroyAllWindows()
