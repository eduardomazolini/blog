---
---

Isso é algo que já sabíamos na pratica esta comentado em alguns lugares mas faltava para convencer algumas pessoas um comentário de um grande fabricante de equipamento de Voz.
  
    Segue um documento da AVAYA sobre o tema:
  
    
  
    http://downloads.avaya.com/css/P8/documents/100016254
  
    
  
    
  
    Multipath routing
  
    Many routing protocols, such as OSPF, install multiple routes for a particular destination into a
  
    routing table. Many routers attempt to load-balance across the two paths. There are two
  
    methods for load balancing across multiple paths. The first method is per-packet load
  
    balancing, where each packet is serviced round-robin fashion across the two links. The second
  
    method is per-flow load balancing, where all packets in an identified "flow" (source and
  
    destination addresses and ports) take the same path. IP Telephony does not operate well over
  
    per-packet load-balanced paths. This type of setup often leads to "choppy" quality voice. Avaya
  
    recommends that in situations with multiple active paths, per-flow load balancing is preferable to
  
    per-packet load balancing. On Cisco routers, the command for this is "ip route-cache," applied
  
    per interface.
  
    
  
    
  
