---
---

O pessoal acha que Mikrotik é difícil, pois pode muita coisa.
Então eu limitei bastante o WebFig dele pro pessoal não se perder.
Salve o conteúdo abaixo com extensão .json na pasta skin e atribua a um grupo de usuários.

Como eu digo, essas são coisas que eu não devo esquecer, então talvez seja melhor criar o seu skin, basta acessar o WebFig e clicar no botão "Desing Skin".



{
    Terminal: 0,
    CAPsMAN: 0,
    Wireless: {
        'Wireless (Atheros AR9300)': {
            General: { ARP: 0, 'ARP Timeout': 0 },
            Wireless: { 'WMM Support': 0, 'Station Roaming': 0 },
            'WPS Client': 0,
            'Setup Repeater': 0,
            'Freq. Usage...': 0,
            'Align...': 0,
            'Sniff...': 0,
            'Snooper...': 0
        }
    },
    Interfaces: {
        'Interface List': 0,
        'EoIP Tunnel': 0,
        'IP Tunnel': 0,
        'GRE Tunnel': 0,
        VRRP: 0,
        Bonding: 0,
        LTE: 0
    },
    Bridge: { Settings: 0, Filters: 0, NAT: 0 },
    Switch: 0,
    Mesh: 0,
    IP: {
        ARP: 0,
        Accounting: 0,
        Addresses: {
            Address: { Network: 0 }
        },
        Cloud: 0,
        'DHCP Client': {
            'DHCP Client': {
                Advanced: {
                    'DHCP Options': 0,
                    'Default Route Distance': 0,
                    Script: 0,
                    tab: 0
                },
                Status: { 'CAPS Managers': 0 }
            },
            'DHCP Client Options': 0
        },
        'DHCP Relay': 0,
        'DHCP Server': {
            DHCP: {
                Relay: 0,
                'Bootp Lease Time': 0,
                'Src. Address': 0,
                'Delay Threshold': 0,
                Authoritative: 0,
                'Bootp Support': 0,
                'Lease Script': 0,
                'Add ARP For Leases': 0,
                'Always Broadcast': 0,
                'Use RADIUS': 0
            },
            'DHCP Config': 0,
            'DHCP Setup': 0,
            Networks: {
                Netmask: 0,
                Domain: 0,
                'WINS Servers': 0,
                'NTP Servers': 0,
                'CAPS Managers': 0,
                'Next Server': 0,
                'Boot File Name': 0,
                'DHCP Options': 0,
                'DHCP Option Set': 0
            },
            Options: 0,
            'Option Sets': 0,
            Alerts: 0
        },
        DNS: {
            Settings: {
                'Max UDP Packet Size': 0,
                'Query Server Timeout': 0,
                'Query Total Timeout': 0,
                'Max. Concurrent Queries': 0,
                'Max. Concurrent TCP Sessions': 0,
                'Cache Size': 0,
                'Cache Max TTL': 0
            }
        },
        Firewall: {
            NAT: {
                Action: {
                    Action: { limit: 'masquerade,dst-nat' },
                    Log: 0,
                    'Log Prefix': 0
                },
                General: {
                    'Src. Address': { tab: 'indicado para srcnat/masquerad' },
                    Protocol: { separator: 0, limit: 'tcp,udp' },
                    'Src. Port': 0,
                    'Any. Port': 0,
                    'In. Interface': { order: 3 },
                    'Out. Interface': { order: 2, tab: 'indicado para dstnat/port-forward' },
                    'Packet Mark': 0,
                    'Connection Mark': 0,
                    'Routing Mark': 0,
                    'Routing Table': 0,
                    'Connection Type': 0
                },
                Advanced: {
                    'Src. Address List': 0,
                    'Dst. Address List': 0,
                    'Layer7 Protocol': 0,
                    Content: 0,
                    'Connection Bytes': 0,
                    'Connection Rate': 0,
                    'Per Connection Classifier': 0,
                    'Src. MAC Address': 0,
                    'Out. Bridge Port': 0,
                    'In. Bridge Port': 0,
                    'In. Bridge Port List': 0,
                    'Out. Bridge Port List': 0,
                    'IPsec Policy': 0,
                    'Ingress Priority': 0,
                    Priority: 0,
                    'DSCP (TOS)': 0,
                    'TCP MSS': 0,
                    'Packet Size': 0,
                    Random: 0,
                    'ICMP Options': 0,
                    'IPv4 Options': 0,
                    TTL: 0,
                    tab: 0
                },
                Extra: {
                    'Connection Limit': 0,
                    Limit: 0,
                    'Dst. Limit': 0,
                    Nth: 0,
                    Time: 0,
                    'Src. Address Type': 0,
                    'Dst. Address Type': 0,
                    PSD: 0,
                    Hotspot: 0,
                    'IP Fragment': 0,
                    tab: 0
                }
            },
            Mangle: 0,
            Raw: 0,
            'Service Ports': 0,
            Tracking: 0
        },
        Hotspot: 0,
        IPsec: 0,
        Neighbors: { 'Discovery Interfaces': 0 },
        Packing: 0,
        Routes: { Rules: 0, VRF: 0 },
        Services: 0,
        Settings: 0,
        Socks: 0,
        TFTP: 0,
        'Traffic Flow': 0,
        'Web Proxy': 0
    },
    Routing: 0,
    System: {
        'Auto Upgrade': 0,
        Certificates: 0,
        Clock: 0,
        Console: 0,
        Drivers: 0,
        History: 0,
        LEDs: 0,
        License: 0,
        Logging: 0,
        Ports: 0,
        'Reset Configuration': {
            'Reset Configuration': { 'Do Not Backup': 0, 'Run After Reset': 0 }
        },
        Routerboard: { Settings: 0 },
        'SNTP Client': 0,
        Scheduler: 0,
        Scripts: 0,
        Shutdown: 0,
        'Special Login': 0,
        Users: 0
    },
    Queues: 0,
    Tools: {
        'BTest Server': 0,
        Email: 0,
        'Flood Ping': 0,
        Graphing: 0,
        'MAC Server': 0,
        Netwatch: 0,
        'Packet Sniffer': 0,
        'Ping Speed': 0,
        Profile: 0,
        RoMON: 0,
        SMS: 0,
        Telnet: 0,
        Torch: 0,
        'Traffic Generator': 0,
        'Traffic Monitor': 0
    },
    Files: 0,
    Log: 0,
    Radius: 0,
    'Make Supout.rif': 0,
    Undo: 0,
    Redo: 0,
    WinBox: 0,
    Graphs: 0,
    License: 0,
    Status: {
        Status: {
            '0': { alias: 'Wireless:Wireless (Atheros AR9300):*5:Wireless:Radio Name', tab: 'WLAN' },
            '1': { alias: 'Wireless:Wireless (Atheros AR9300):*5:Wireless:SSID' },
            '2': { alias: 'Wireless:Wireless (Atheros AR9300):*5:Status:Tx/Rx Signal Strength' },
            '3': { alias: 'System:Identity:Identity:Identity', order: 0 },
            '4': { alias: 'Interfaces:Ethernet:*1:running', tab: 'LAN' },
            '5': { alias: 'Interfaces:Ethernet:*1:Status:Auto Negotiation' },
            '6': { alias: 'Interfaces:Ethernet:*1:Status:Rate' },
            '7': { alias: 'Interfaces:Ethernet:*1:Status:Full Duplex' },
            '8': { alias: 'Wireless:Wireless (Atheros AR9300):*5:Status:Tx/Rx CCQ', order: 6 },
            '9': { alias: 'Wireless:Wireless (Atheros AR9300):*5:Status:Signal To Noise', order: 4 },
            '10': { alias: 'Wireless:Wireless (Atheros AR9300):*5:Status:Link Downs', order: 5 },
            '11': { alias: 'Interfaces:Ethernet:*1:Status:Link Downs' }
        }
    }
}




