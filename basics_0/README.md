# Network - Basics

This project introduces the fundamental concepts of computer networking. It covers the OSI model, different network types (LAN vs. WAN), IP addressing, Transport Layer protocols (TCP vs. UDP), and basic network troubleshooting tools like `ping` and `netstat`.

## 📚 Resources
* [OSI model](https://en.wikipedia.org/wiki/OSI_model)
* [Different types of network](https://www.geeksforgeeks.org/types-of-computer-networks/)
* LAN network
* WAN network
* Internet
* [MAC address](https://en.wikipedia.org/wiki/MAC_address)
* What is an IP address
* Private and public address
* IPv4 and IPv6
* Localhost
* [TCP and UDP](https://www.geeksforgeeks.org/differences-between-tcp-and-udp/)
* [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
* [What is ping /ICMP](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)
* [Positional parameters](https://wiki.bash-hackers.org/scripting/posparams)

**man or help:**
* `netstat`
* `ping`

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to **explain to anyone**, **without the help of Google**:

### OSI Model
* What it is
* How many layers it has
* How it is organized

### Networks
* What is a **LAN** (Typical usage, Typical geographical size)
* What is a **WAN** (Typical usage, Typical geographical size)
* What is the **Internet**

### Addressing
* What is an **IP address**
* What are the 2 types of IP address
* What is `localhost`
* What is a **subnet**
* Why **IPv6** was created

### TCP/UDP
* What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
* What is the main difference between **TCP** and **UDP**
* What is a **port**
* Memorize **SSH**, **HTTP** and **HTTPS** port numbers

### Troubleshooting
* What tool/protocol is often used to check if a device is connected to a network

---

## ⚙️ Requirements

### Bash Script Files
* **Allowed editors:** `vi`, `vim`, `emacs`
* **Environment:** All your Bash script files will be interpreted on **Ubuntu 22.04**.
* **File Ending:** All your files should end with a new line.
* **Shebang:** The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
* **Comments:** The second line of all your Bash scripts should be a comment explaining what is the script doing.
* **Executable:** All your Bash script files must be executable.
* **Linting:** Your Bash script must pass `shellcheck` without any error.
* **README:** A `README.md` file, at the root of the folder of the project, is mandatory.

### Answer Files
For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer.

**Example:**
*Question: What is the most important position in a software company?*
1. Project manager
2. Backend developer
3. System administrator


📂 Tasks
0. OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

Questions:

What is the OSI model?

Set of specifications that network hardware manufacturers must respect

The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology

The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

Alphabetically

From the lowest to the highest level

Randomly

File: 0-OSI_model

1. Types of network
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

What type of network a computer in local is connected to?

Internet

WAN

LAN

What type of network could connect an office in one building to another office in a building a few streets away?

Internet

WAN

LAN

What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

Internet

WAN

LAN

File: 1-types_of_network

2. MAC and IP address
Questions:

What is a MAC address?

The name of a network interface

The unique identifier of a network interface

A network interface

What is an IP address?

Is to devices connected to a network what postal address is to houses

The unique identifier of a network interface

Is a number that network devices use to connect to networks

File: 2-MAC_and_IP_address

3. UDP and TCP
Let’s fill the empty parts in the drawing above.

Questions:

Which statement is correct for the TCP box:

It is a protocol that is transferring data in a slow way but surely

It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the UDP box:

It is a protocol that is transferring data in a slow way but surely

It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the TCP worker:

Have you received boxes x, y, z?

May I increase the rate at which I am sending you boxes?

File: 3-UDP_and_TCP

4. TCP and UDP ports
While the full list of ports should not be memorized, it is important to know the most used ports:

22 for SSH

80 for HTTP

443 for HTTPS

Write a Bash script that displays listening ports:

That only shows listening sockets

That shows the PID and name of the program to which each socket belongs

File: 4-TCP_and_UDP_ports

5. Is the host on the network
The Internet Control Message Protocol (ICMP) is used by network devices to check if other network devices are available on the network. The command ping uses ICMP.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

Accepts a string as an argument

Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed

Ping the IP 5 times

File: 5-is_the_host_on_the_network

