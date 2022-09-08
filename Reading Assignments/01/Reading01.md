{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Paper Reading\
\
## Main idea\
\
- The design philosophy of the complex networks structures.\
- DIscuss some main features and goals of Internet designing\
- Elaborate some key techniques/concepts in the Internet designing\
\
## Goals for DPRPA Internet protocals\
\
- The fundamental goal: To develop an effective technique for multiplexed utilization of the interconnected networks\
- More detailed goals:\
  - Internet communications' suvivability\
  - Can support multiple types of service\
  - Must accommodate a variety of networks\
  - Other...\
\
## Goal #1: Survivalbilty in face of Loss\
\
- The on-going conversation status is protected\
- "Fate-sharing" model: Gather the conversation status info at the endpoint of the net.\
- Advantages of Fate-sharing over replications:\
  - Protect any number of failures\
  - Easier to engineer\
\
## Goal #2: Types of service\
\
- Bi-directional reliable delivery of data using TCP\
- Real-time delivery of digitized speech with less delay amd latency\
\
## Goal #3 Varieties of Networks\
\
- The Internet is able to incorporate a wide variety of network technologies:\
  - Long haul nets\
  - LAN\
  - Broadcast satellite nets\
- Method: The Internet makes a minimum set of assumptions about the function which the net will provide.\
\
## Architecture and Implementation\
\
- "Realization": A particular set of networks, gateways and hosts connected together.\
- Implementation engineerings:\
  - Give guidance to the designer of a realization for different types of service.\
  - Explore the service which a realization can deliver under a variety of loadings.\
- Higher level implementations: Performance\
\
## Datagrams\
\
- Datagram is a fundamental architectural feature for Internet.\
- Why datagrams are important:\
  - Eliminate the need for connection state within intermediate nodes\
  - Provides a basic building block which can tolerate a variety of types of service.\
  - Represent a minimum network service assumptions.\
\
## Transmission Control Protocal (TCP)\
\
- One important feature: Regulation of the delivery of bytes instead of packets.\
  - To permit the insertion of control information into sequence space of the bytes.\
  - To permit TCP packet to be broken into smaller packets\
  - To permit a number of smaller packets to be gathered to form a larger packet for retransmission.\
- End-Of-Letter flag (EOL): now vanished\
\
## Further work and Conclusions\
\
- From a overall perspective, the Internet architecture is very successful in itself and in s series of similar architectures it spawned.\
- Some further goals designers should access:\
  - Resource management and accounting must be done on each packet separately\
- Next generation of architecture\
  - No assumptions on any particular type of service when identify a sequence of packets\
  - "Soft state": guarantee the survivability& flexibility when doing a better job of resource management and accounting.\
}