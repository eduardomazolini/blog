---
tags: [linux, rede, voip]
---

Se vc vai usar um servidor com hardware conhecido ligado em um switch de rede conhecido.
POR QUE, depender do protocolo de auto negociação da placa de rede?
Por isso recomendo sempre editar o arquivo que inicia a placa de rede, para desabilitar.
Isso evita muitos problemas, principalmente quando existe voip.
Basta adicionar uma das linhas abaixo:

Para 100Mb Full duplex
```
ETHTOOL_OPTS=”speed 100 duplex full autoneg off”
```

Para 10Mb Halfd duplex
```
ETHTOOL_OPTS=”speed 10 duplex half autoneg off”
```

No meu caso os arquivos ficam em: /etc/sysconfig/network-scripts
O Nome do arquivo da minha 1a. placa de rede é: ifcfg-eth0

Atualização 2026:
Nossa!
Lembrança boa, que a decisão era entre 10Mb e 100Mb. Hoje 100Mb indica defeito no cabo e 1Gb é o padrão. Mas já estamos apontando pra cabos 2.5Gb, eu já tenho um roteador que 1 porta é 2.5Gb.

E linux como Debian não usam mais esse caminho para configurar as interfaces, isso era o padrão RedHat, faz tempo que não uso CentOS.
