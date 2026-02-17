---
---

Vou anotar aqui o que achei sobre o assunto até que esse texto vire um bom artigo.

cli:
```
wlanconfig ath1 create wlandev wifi0 wlanmode ap
iwpriv ath1 ap_bridge 0
iwconfig ath1 key off open
brctl addif br0 ath1
iwconfig ath1 essid INTERA_03A
ip link set ath1 up
```
1) Add a new 'bridge' port (use the next port number in line, eg 'port.4' and next device number in line, eg 'ath1'):


bridge.1.port.4.devname=ath1
bridge.1.port.4.prio=20
bridge.1.port.4.status=enabled

2) Add in the 'ebtables' options (incrementing the .2. number as applicable and using the added device number):

ebtables.sys.eap.2.status=enabled
ebtables.sys.eap.2.devname=ath1
ebtables.sys.arpnat.2.status=enabled
ebtables.sys.arpnat.2.devname=ath1

3) Add in the 'netconf' port (incrementing the .4. number as applicable and using the added device number):

netconf.4.up=enabled
netconf.4.status=enabled
netconf.4.role=bridge_port
netconf.4.promisc=enabled
netconf.4.netmask=255.255.255.0
netconf.4.mtu=1500
netconf.4.ip=0.0.0.0
netconf.4.hwaddr.status=disabled
netconf.4.hwaddr.mac=
netconf.4.devname=ath1
netconf.4.autoip.status=disabled
netconf.4.allmulti=enabled

4) Create the next 'virtual' radio device using the added device number and the next virtual number, eg virtual.1.:

radio.1.virtual.1.status=enabled
radio.1.virtual.1.devname=ath1
radio.1.virtual.1.mode=master

5) Create the next 'wireless' section using the device number and specify the new SSID:

wireless.2.wmm=enabled
wireless.2.wds.status=disabled
wireless.2.status=enabled
wireless.2.ssid=NEWSSID <= CHANGE TO ACTUAL SSID OF VIRTUAL AP
wireless.2.l2_isolation=enabled <= CHANGE TO 'disabled' IF NO ISOLATION IS REQUIRED
wireless.2.hide_ssid=disabled
wireless.2.autowds=disabled
wireless.2.authmode=1
wireless.2.ap=
wireless.2.addmtikie=enabled
wireless.2.devname=ath1

6) If no security is needed; you're done here; save config file and upload to device.

7) If security is required; add the following config appending the section number:

aaa.2.br.devname=br0
aaa.2.devname=ath1<= CHANGE TO ACTUAL DEVICE OF VIRTUAL AP
aaa.2.driver=madwifi
aaa.2.radius.auth.1.status=disabled
aaa.2.ssid=NEWSSID<= CHANGE TO ACTUAL SSID OF VIRTUAL AP
aaa.2.status=enabled
aaa.2.wpa.1.pairwise=TKIP CCMP
aaa.2.wpa.key.1.mgmt=WPA-PSK
aaa.2.wpa.psk=PASSWORD<= CHANGE TO REQUIRED PASSWORD OF VIRTUAL AP
aaa.2.wpa.mode=2

fonte: [Fórum UBNT](https://community.ubnt.com/t5/airOS-Software-Configuration/Multiple-SSIDs-Virtual-APs/m-p/1098419#M38785) / [Binary Heartbeat](http://www.binaryheartbeat.net/2015/09/ubiquiti-airos-56-virtual-ssid-step-by.html)
