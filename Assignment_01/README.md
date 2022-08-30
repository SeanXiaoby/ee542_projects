# EE542 -- Assignment 01

#### Topics:

- TCP/IP computer networks
- UDP/IP computer networks
- Server-clients emulated networks models based on different protocals
- Client-router-client model based on Linux and VirtualBox virtual machines

#### Author: [Boyang Xiao](https://www.linkedin.com/in/boyang-xiao-40b644225/)

- **USC id**:		3326-7302-74
- **Email**:		<a href="mailto:boyangxi@usc.edu">boyangxi@usc.edu</a>
- **Github**:	[here](https://github.com/)

#### Dev Environment:

- **OS:** [*Ubuntu ver. 16.04*](https://ubuntu.com/16-04)
- **Compiler**: *g++ ver. 5.4.0*

---

### Introduction

In this assignment, the most-widely-used computer networks protocals, TCP/IP & UDP/IP, are introduced and implemeted based on [Linux socket programming](http://www.linuxhowtos.org/C_C++/socket.htm) using [C/C++](https://cplusplus.com/reference/).  A classic model, one server to several clients networks, is emulated under these two types of networks protocals.

Among these two protocals, TCP/IP is well-known for its stability, liability and connection-based characteristics, while UDP/IP is known as a connectionless protocal but convenient & fast. As implemented in this assignment, the server based on TCP/IP can handle multiple connection requests from several different clients and can processively create multiple child processes to send/recv messages with the clients. On the other hand, for the server based on UDP/IP protocal, it can reveive messages from different clients without establishing connections with them ahead and does not require child processes to handle different clients (at least in this assignment senorios).

The models are built on the same machine and the ip address should all be set as *localhost*. Please refer to the instructions in the following sessions carefully to compile and run the programs.

### Assignment Files

- **./README.md:** Introductions and instructions for the whole assignment.
- **./Makefile:** Automatically compile all c/c++ codes.
- **./client.c:** Implementations for clients under TCP/IP protocal.
- **./server.c:** Implementations for the server under TCP/IP protocal.
- **./UDP_client.c:** Implementations for clients under UDP/IP protocal.
- **./UDP_server.c:** Implementations for the server under UDP/IP protocal.

### Compiling Instructions

To compile all the original codes, please open a terminal in the assignment folder and execute the following instructions:

```shell
make all
```

All the codes should be compiled automatically and the following info should be displayed:

```shell
g++ ./server.c -o server
g++ ./client.c -o client
g++ ./UDP_server.c -o udp_server
g++ ./UDP_client.c -o udp_clent
```

### Run Server and Clients

- #### For Server and Clients based on TCP/IP:

To run the server, please excecute the following instructions in the terminal(with an available port number).

```shell
./server <port_num>
```

To run the clients, you can excecute the following instructions in several different terminals. Please use the same port number as the server does and use *localhost* as the ip address if you want to connect the local servers.

```shell
./client <ip_addr> <port_num>
```

Then you can follow the infomation displayed in the terminals to communicate with clients/servers. To close the clients/servers, you can use the following command:

```shell
ctrl + c
```

- #### For Server and Clients based on UDP/IP:

To run the server, please excecute the following instructions in the terminal(with an available port number).

```shell
./udp_server <port_num>
```

To run the clients,please use the same port number as the server does and use *localhost* as the ip address if you want to communicate with the local servers.

```shell
./udp_client <ip_addr> <port_num>
```

Then you can follow the infomation displayed in the terminals to communicate with clients/servers. To close the clients/servers, you can use the following command:

```shell
ctrl + c
```

---

##### Please contact me at  <a href="mailto:boyangxi@usc.edu">boyangxi@usc.edu</a> if you have any concerns and suggestions. Thx!!!


###### Fight  on Trojans! ✌
