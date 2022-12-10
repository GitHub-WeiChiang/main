NetworkPlanningAndManagementStudyGuide
=====
協定
---
| 縮寫 | 英文 | 中文 | 層級 |
| --- | --- | --- | --- |
| DNS | Domain Name System | 網域名稱服務協定 | L5 |
| DHCP | Dynamic Host Configuration Protocol | 動態主機 IP 配置協定 | L5 |
| HTTP | HyperText Transfer Protocol | 超文字傳輸協定 | L5 |
| SMTP | Simple Mail Transfer Protocol | 簡易郵件傳輸協定 | L5 |
| POP | Post Office Protocol | 郵件接收協定 | L5 |
| Telnet | Telnet | 遠端登入協定 | L5 |
| SSH | Secure Shell | 遠端登入協定 | L5 |
| FTP | File Transfer Protocol | 檔案傳輸協定 | L5 |
| TFTP | Trivial File Transfer Protocol | 簡單檔案傳輸協定 | L5 |
| TCP | Transmission Control Protocol | 傳輸控制協定 | L4 |
| UDP | User Datagram Protocol | 使用者資料報協定 | L4 |
| IPv4 | Internet Protocol version 4 | 網際網路通訊協定第四版 | L3 |
| IPv6 | Internet Protocol version 6 | 網際網路通訊協定第六版 | L3 |
| IPX | Internetwork Packet Exchange | 網際網路封包交換協定 | L3 |
| CLNP | Connectionless Network Protocol | 無連接網路協定 | L3 |
| Ethernet protocol | Ethernet protocol | 乙太網路協定 | L2 |
| ICMP | Internet Control Message Protocol | 網際網路控制訊息協定 | L3 |
| ARP | Address Resolution Protocol | 位址解析協定 | L3 |
| GARP | Gratuitous Address Resolution Protocol | 無回報位址解析協定 | L3 |
| RARP | Reverse Address Resolution Protocol | 逆位址解析協定 | L3 |
| CDP | Cisco Discovery Protocol | 思科發現協定 | L2 |
| LLDP | Link Layer Discovery Protocol | 鏈路層發現協定 | L2 |
| Routing Protocol | Routing Protocol | 路由協定 | L3 |
| IGP | Interior Gateway Protocol | 內部閘道協定 | L3 |
| EGP | Exterior Gateway Protocol | 外部閘道協定 | L3 |
| RIP | Routing Information Protocol | 路由資訊協定 | L3 |
| EIGRP | Enhanced Interior Gateway Routing Protocol | 增強型內部閘道路由協定 | L3 |
| OSPF | Open Shortest Path First | 開放式最短路徑優先 | L3 |
| IS - IS | Intermediate System To Intermediate System | 中間系統到中間系統 | L2 |
| BGP | Border Gateway Protocol | 邊界閘道協定 | L5 |
| IGMP | Internet Group Management Protocol | 網際網路組管理協定 | L3 |
| NDP | Neighbor Discovery Protocol | 鄰居發現協議 | L3 |
| DTP | Dynamic Trunk Protocol | 動態中繼協定 | L2 |
| VTP | VLAN Trunking Protocol | 虛擬區域網絡中繼協定 | L2 |
| STP | Spanning Tree Protocol | 生成樹協定 | L2 |
| PAgP | Port Aggregation Protocol | 連線埠聚集協定 | L2 |
| LACP | Link Aggregation Control Protocol | 鏈路聚合控制協議 | L2 |
| FHRP | First Hop Redundancy Protocol | 第一跳冗餘協定 | L3 |
| HSRP | Hot Standby Router Protocol | 熱備份路由器協定 | L3 |
| VRRP | Virtual Router Redundancy Protocol | 虛擬路由器冗餘協定 | L3 |
| GLBP | Gateway Load Balancing Protocol | 閘道負載平衡協定 | L3 |
| ATM | Asynchronous Transfer Mode | 非同步傳輸模式 | L2 |
| Frame Relay | Frame Relay | 訊框中繼 | L2 |
| HDLC | High Level Data Link Control | 高級數據鏈路控制 | L2 |
| PPP | Point To Point Protocol | 對等協定 | L2 |
| PAP | Password Authentication Protocol | 通行碼鑑別協定 | L2 |
| CHAP | Challenge Handshake Authentication Protocol | 詢問握手認證協議 | L2 |
| MLPPP | Multilink PPP | 多鏈路對等協定 | L3 |
| PPPoE | Point-to-Point Protocol over Ethernet | 乙太網路對等協定 | L2 |
| ISAKMP | Internet Security Association And Key Management Protocol | 網際網路安全關聯鑰匙管理協定 | L4 |
| NHRP | Next Hop Resolution Protocol | 下一跳解析協定 | L2 |
| NTP | Network Time Protocol | 網路時間協定 | L5 |
| SNMP | Simple Network Management Protocol | 簡單網路管理協定 | L5 |
| RSVP | Resource Reservation Protocol | 資源預留協定 | L4 |
| CAPWAP | Control And Provisioning Of Wireless Access Points | 無線接入點的控制和配置協議 | L3 |
| CHARGEN | Character Generator Protocol | 字元產生器協定 | L4 |
| EAP | Extensible Authentication Protocol | 可擴展身份驗證協議 | L4 |
<br />

![image](https://gitlab.com/ChiangWei/main/-/raw/master/ComputerNetwork/Internet%20Protocol.png)
<br />

* ### EMS (Element Management System，網元管理系統)，是管理特定類型的一個或多個電信 NE (Network Element，網路單元) 的系統。
* ### NMS (Network Management System，網路管理系統)，也稱為綜合網管系統，可以同時對多種專業網進行管理，也可以同時管理由多個廠家設備構成的電信網路。
* ### API vs. SNMP vs. CLI
    * ### There are a variety of ways to communicate, configure, and manage network devices. The first way of managing network equipment is through the console. The console is a command-line environment that network admins connect to through a remote connection. Though SSH is commonly used today, that remote connection can be made through the Telnet or SSH protocols.
    * ### SNMP is another way to communicate with network devices. SNMP is more universal than console commands. SNMP has a limited ability to perform configurations, though, and is commonly used to collect metrics for networks instead. These metrics are collected and displayed by management information bases.
    * ### Finally, network engineers can also use APIs. Again, APIs are specific to each vendor, though common languages like OpenConfig attempt to make those APIs more universal. Network admins can create a much more automated, scalable, and robust network by using vendor APIs.
* ### Whats The Difference Between A Port And An Interface ?
    * ### The port is where you plug in the physical cable connector. The interface is what you configure in the Cisco IOS, therefore is the software representation of the physical port.
* ### "ip default-gateway" vs. "ip default-network"
    * ### "ip default-gateway" is to be used in L2 devices.
    * ### "ip default-network" would be used in L3 devices, but works slightly different from the usual static default route configured with "ip route 0.0.0.0 0.0.0.0 <next_hop>". Let's say you configure "ip default-network 172.31.0.0". Then, if the device already knows a route for 172.31.0.0, this route will be flagged as a default route candidate. "ip default-network" command is classful.
* ### The difference between VLANs and VLAN interfaces.
    * ### A VLAN itself is not an interface. It is a division of the broadcast domain within an Ethernet segment.
    * ### To initiate a VLAN in a network switch, this command can be used: "(config)#vlan 10".
    * ### A VLAN interface is a logical interface that represents a VLAN in all Layer 3 activities the unit may participate in.
    * ### A VLAN interface has an IP address that is used for any management operations, or as an IP next-hop for routes.
    ```
    (config)#Interface vlan 10
    (config-vlan-10)#ip address 10.10.10.1 255.255.255.0
    (config-vlan-10)#no shutdown
    ```
<br />

Reference
=====
* ### 網路規劃與管理實務 - 協助考取國際網管證照, 3e