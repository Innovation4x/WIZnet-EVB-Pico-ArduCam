# CamReceiver.py code file explanation:
Datetime is imported to work with dates as date objects. Imported socket module provides
access to the BSD socket interface. the socket() function returns a socket object whose
methods implement the various socket system calls. OpenCV is a huge open-source library
for computer vision, machine learning, and image processing and it is imported in our
project. NumPy is imported and it offers comprehensive mathematical functions and also
used for handling the arrays. The imported Image module provides a class with the same
name which is used to represent a PIL image. The io module provides Python&#39;s main facilities
for dealing with various types of I/O. There are three main types of I/O: text I/O, binary I/O
and raw I/O. The multiprocessing module uses Process and queue APIs which do not have
analogs in the threading module. In multiprocessing, processes are spawned by creating a
Process object and then calling its start() method. Process follows the API of threading. And
also Queue is used for python threads, treading is imported for supporting this
multiprocessing.

In CamReceiver class has 6 methods. And the methods used in our work are __init__,
cam_server_proc, start, stop, get and empty. And explanation for each of the methods are as
follows.
__init__ (self, width=320, height=240) method:
The __init__ method is similar to constructors. Constructors are used to initializing the
method’s state. Like methods, a constructor contains a collection of statements (i.e.
instructions) that are executed at the time of method creation. It runs as soon as an method of a
class is instantiated. Class methods must have an extra first parameter in the method
definition. And all the values are provided by the python when its defined. The used
parameters for the method is width, height, HOST, PORT, ACK, frames and two flags
is_connected and process. Width is defined with value equal to 320 and height equal to 240.

# Method cam_server_proc(self):
In the method cam_server_proc(self), self represents the instance of the class. By using the
“self” we can access the attributes and methods of the class in python. In line 25 global
is_connected, is_connected() returns True when the connection is available, False otherwise.
socket.socket() creates a socket method that supports the context manager type, so you can use
it in a with statement. The arguments passed to socket() are constants used to specify the
address family and socket type. AF_INET is the Internet address family for IPv4.
SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport
messages in the network. From the socket libraries some of the API’s are used to set the IP
address and port and other protocols using the values defined for setting up to receive the
streamed image. The s.bind() method is used to associate the socket with a specific network
interface and port number. The values passed to s.bind() depend on the address family of the
socket. In this example, we are using socket.AF_INET (IPv4). So it expects a two-tuple:
(host, port). The IP address 127.0.0.1 is the standard IPv4 address for the loopback interface,
so only processes on the host will be able to connect to the server. port represents the TCP
port number to accept connections on from clients. It should be an integer from 1 to 65535, as
0 is reserved. Some systems may require superuser privileges if the port number is less than
1024. When everything is completed with the setup it starts to listen using the socket and
is_connected flag is used for indicating it.
Note: Host can be a hostname, IP address, or empty string. If an IP address is used, host
should be an IPv4-formatted address string.
When it is connected s.accept() function in line 36 returns a socket descriptor that is
connected to your TCP server. In this case, it returns a tuple of objects. The first parameter,
conn, is a socket object that you can use to send data to and receive data from the client that
is connected. The second parameter, addr, contains address information about the client that
is connected (e.g., IP address and remote part). And printf prints the address its connected.
When it connected chunks array is created and conn.send() sends an acknowledgement i.e
send ACK values. Data variable is created to receive the values using the conn.recv(1024),
this will read at most 1024 bytes, blocking if no data is waiting to be read. If something is
present in data, it is updated in chunks as a list values. In line 49 and we are checking the last
two vales to see the End of the frame. The index value of -1 gives the last element, and -2
gives the second last element of an array. Checking if the last array value is 0xD9 and second
last element is 0xFF we will end that array and view that values as images using next set of
codes.
From line 52 to 56 the code is used for storing the values of the image as a raw image values.
Stream variable is used to store the value as byte, it is obtained by converting the chunks to
bytes using io.bytes() method. Cv2.cvtColor is used for converting the values into numpy
array with BGR image values. Io and cv2 libraries are used for getting the proper image with
each received chunks of data as a frames. Four functions are defined for executing the camera
receive protocols, these are for starting, stopping, getting frames of images and lastly empty
is used to empty the frames which are not used in our work and can be called.
# Methods start (), stop (), get () and empty ():
Start method starts the thread’s activity. It must be called at most once per thread method. It
arranges for the object’s run () method to be invoked in a separate thread of control. This
method will raise a RuntimeError if called more than once on the same thread method. The
self. process turns your string into a list of characters, passing them to the processLine
function. The start() method creates and starts the thread on line 60. The thread executes the cam_server_proc() method.
This function continuously runs a while loop that reads a frame from the video stream and
stores it in the class instance’s frame attribute, as long as the stopped flag isn’t set.
Stop method stops the thread’s activity. is_connected flag is set False to stop the connection
and its defined on line 65. Get method is defined to get and return the camera vales as a frames
when cam is started it is defined in in lines 68 and 69. Empty is used to check the values of
the received frames is empty, and it is defined in line 71 and 72.

