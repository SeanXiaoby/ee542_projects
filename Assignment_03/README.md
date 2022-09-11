# EE542 - Lab03

### ?
---
#### Topics:

- 

#### Author: [Boyang Xiao](https://www.linkedin.com/in/boyang-xiao-40b644225/)

- **USC id**:		3326-7302-74
- **Email**:		<a href="mailto:boyangxi@usc.edu">boyangxi@usc.edu</a>
- **Github**:	[here](https://github.com/SeanXiaoby)

#### Dev Environment:

- **AWS acount:** Free tier
- **Installed VM OS**: [vyOS 1.3](https://aws.amazon.com/marketplace/pp/prodview-o7dahbop7getw?sr=0-1&ref_=beagle&applicationId=AWSMPContessa), [Ubuntu 18.04 LTS](https://aws.amazon.com/marketplace/pp/prodview-pkjqrkcfgcaog?sr=0-1&ref_=beagle&applicationId=AWSMPContessa)

#### [Video Introductions]()

---

### Exploring Bandwidth and Throughput

In this part, we will use iPerf3 tool to test network bandwidth on Linux.

#### TCP throughput

We launch a server on the Server VM using:

```shell
iperf3 -s
```

And we use the command below on the Client machine to start the TCP test:

```shell
iperf3 -c 10.0.2.163 -p 5201
```

The TCP bandwidth test results are below:

```shell
Connecting to host 10.0.2.163, port 5201
[  4] local 10.0.2.86 port 45728 connected to 10.0.2.163 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec   451 MBytes  3.78 Gbits/sec   21   1.60 MBytes
[  4]   1.00-2.00   sec   495 MBytes  4.15 Gbits/sec   12   1.43 MBytes
[  4]   2.00-3.00   sec   502 MBytes  4.21 Gbits/sec    4   2.07 MBytes
[  4]   3.00-4.00   sec   500 MBytes  4.19 Gbits/sec    7   2.37 MBytes
[  4]   4.00-5.00   sec   504 MBytes  4.23 Gbits/sec  122   1.89 MBytes
[  4]   5.00-6.00   sec   504 MBytes  4.23 Gbits/sec   24   1.75 MBytes
[  4]   6.00-7.00   sec   488 MBytes  4.10 Gbits/sec    8   1.48 MBytes
[  4]   7.00-8.00   sec   512 MBytes  4.30 Gbits/sec    7   2.07 MBytes
[  4]   8.00-9.00   sec   490 MBytes  4.11 Gbits/sec   20   1.72 MBytes
[  4]   9.00-10.00  sec   510 MBytes  4.28 Gbits/sec    7   1.74 MBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec  4.84 GBytes  4.16 Gbits/sec  232             sender
[  4]   0.00-10.00  sec  4.83 GBytes  4.15 Gbits/sec                  receiver
```

The bandwidth should be **4.16 Gbits/sec** for TCP.


#### UDP throughput

Then we use the command below to test UDP:

```shell
iperf3 -u -c 10.0.2.163 -p 5201 -b 5000M
```

The results are :

```shell
Connecting to host 10.0.2.163, port 5201
[  4] local 10.0.2.86 port 32931 connected to 10.0.2.163 port 5201
[ ID] Interval           Transfer     Bandwidth       Total Datagrams
[  4]   0.00-1.00   sec   183 MBytes  1.54 Gbits/sec  23486
[  4]   1.00-2.00   sec   186 MBytes  1.56 Gbits/sec  23751
[  4]   2.00-3.00   sec   183 MBytes  1.54 Gbits/sec  23451
[  4]   3.00-4.00   sec   185 MBytes  1.55 Gbits/sec  23682
[  4]   4.00-5.00   sec   180 MBytes  1.51 Gbits/sec  23006
[  4]   5.00-6.00   sec   182 MBytes  1.53 Gbits/sec  23329
[  4]   6.00-7.00   sec   132 MBytes  1.11 Gbits/sec  16940
[  4]   7.00-8.00   sec   134 MBytes  1.13 Gbits/sec  17169
[  4]   8.00-9.00   sec   161 MBytes  1.35 Gbits/sec  20565
[  4]   9.00-10.00  sec   165 MBytes  1.38 Gbits/sec  21105
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
[  4]   0.00-10.00  sec  1.65 GBytes  1.42 Gbits/sec  0.030 ms  953/216481 (0.44%)
[  4] Sent 216481 datagrams
```

The bandwidth should be **1.42 Gbits/sec** for UDP.


