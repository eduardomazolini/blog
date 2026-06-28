---
tags: [dhcp, dns, mikrotik, queue]
---

No Mikrotik, o DHCP Server não adiciona o hostname no DNS, melhor dizendo, o DNS não reconhece a solicitação para publicar um nome.
Bom, eu em casa tenho alguns equipamentos com IP fixo, uns fixos no servidor, outros por amarração de MAC. Seja como for, eu precisei adicionar os hostnames manualmente no DNS.
Hoje precisei acessar um PC sem IP fixo pelo nome DNS, e aí surgiu esse post.
Em uma empresa também surgiu a necessidade de criar uns gráficos de consumo de banda, e a função de gráficos de **queue** me serve perfeitamente, até pela restrição de acesso à informação, já que se pode restringir somente ao target visualizar o gráfico.

Para solucionar isso, o melhor foi usar a opção de script dentro da configuração do DHCP Server, o campo "lease script".
Quando é registrado um novo host, adiciona o hostname com domínio no DNS e cria uma fila.
Quando o registro é removido do lease, remove a entrada do DNS e desativa a fila.
Por que desativar a fila? Para não perder o histórico da máquina. Quando o PC volta com outro IP, só é atualizado o target.
Se mudar o IP do host, vai ter target duplicado? Sim, mas a fila vai estar inativa.
Se o hostname for nulo? Eu checo isso (xx=xx), no caso optei por não fazer nada.

O Script está abaixo:
```
:local custDomain "dhcp.seudominio.com.br";
:local custLease [/ip dhcp-server get value-name=lease-time [/ip dhcp-server find name=$leaseServerName]];

:local custLeaseHost;
:if ([/ip dhcp-server lease find active-address="$leaseActIP"]!="") do={
  :set custLeaseHost [/ip dhcp-server lease get value-name=host-name [/ip dhcp-server lease find active-address="$leaseActIP"]];
} else={
  :set custLeaseHost "";
};
:if ([/ip dhcp-server lease find active-address="$leaseActIP"]!="") do={
  :if ("X".$custLeaseHost."X"!="XX") do={
    :log info message=("DHCP LEASE: ".$leaseServerName." ".$leaseActIP." ".$leaseActMAC." ".$leaseBound." ".$custLeaseHost);
    /ip dns static add address=$leaseActIP name=($custLeaseHost.".".$custDomain) comment="lease" ttl=$custLease;
    :if ([/queue simple find name=($custLeaseHost.".".$custDomain)]="") do={
      /queue simple add name=($custLeaseHost.".".$custDomain) target=$leaseActIP total-max-limit=10M;
    } else={
      /queue simple set [/queue simple find name=($custLeaseHost.".".$custDomain)] target=$leaseActIP;
      /queue simple enable [/queue simple find name=($custLeaseHost.".".$custDomain)];
    }
  } else={
    :log info message=("DHCP LEASE: ".$leaseServerName." ".$leaseActIP." ".$leaseActMAC." ".$leaseBound." "."NULO");
  };
} else={
  /ip dns static remove [/ip dns static find comment="lease" address=$leaseActIP];
  :log info message=("DHCP LEASE: ".$leaseServerName." ".$leaseActIP." ".$leaseActMAC." ".$leaseBound." ");
  /queue simple disable [/queue simple find target=$leaseActIP."/32" disabled=no];
}; 
```