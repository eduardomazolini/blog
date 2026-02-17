---
---

Hoje ter servidores pra cada necessidade já e claramente perda de recursos.
Então qual a solução? Contratar da núvem ou virtualizar localmente (On-Premises).
Passar pra nuvem realmente é uma alternativa, precisa ser feita uma avaliação financeira.
Se pagar por mês, em 24x já vale o custo do PC simples desligado, sim só o Servidor simples desligado.
Tem que por na conta:
- energia elétrica
- ar-condicionado,
- profissional de DevOps,
- rack,
- espaço do rack no aluguel do imóvel.
- depreciação

Depende de quantos serviços simples já vale um servidor profissional de R$5mil, R$15mil, R$130mil. Mas comprar agora ou financiar.

Virtualização tem varias opções e formas, temos as **VMs** e os **Containers**.
Para ambas as formas temos opções de fazer em nossos desktops, em cima do Sistema Operacional existente seja Windows 10, Linux Desktop ou MacOS, mas isso não serve pra por em produção.

VM no Desktop temos Oracle VirtualBox, VMware Play(só pra rodar), VMWare Workstation, VMWare Fusion.
Container no Desktop temos Docker CE, Minikube (kubernetes), Canonical Microk8s.

Pra virtualizar precisamos de softwares de virtualização (Hypervisor) em um Sistema Operacional que consuma o minimo.

Abaixo algumas opções para VM:
- **KVM**
- Proxmox VE
- oVirt
- VMWare EXSi
- Microsoft Hyper-V
- Citrix **Xen** Server
- Citrix Hypervisor 8.0
- XenServer 7.1 LTSR
- XenServer 7.0
- XenServer 7.6 Free Edition
- XPC-NG
- Xen Orchestra (Free - U$77 - U$550) (Free, minha escolha)

Abaixo algumas opções para Container:
- CoreOS
- Tectonic
- Integrado ao Xen Orchestra Unified Appliance (XOA)
- RedHat Openshift
- RancherOS
- Rancher (Minha escolha)

Existem outras distribuições do Kubernets

Tanto para VM como Containers existem os **Orquestradores**  e existem as interfaces gráficas web (**Web GUI** , site pra gerenciar) que são produtos adicionais opcionais.

Para containers tem o mais simples **Swarm**  e observei movimento de uma padronização em cima do **Kubernets**.
Todas Web GUI que encontrei já tem algum recurso para orquestração dos contêineres.

Algumas Web GUI para conteiners
-  [Portainer](https://www.portainer.io/products-services/portainer-community-edition/)
- [Shipyard](https://shipyard-project.com/automated-deployment/)
- [Rancher](https://rancher.com/products/rancher)
- [Kubernets Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard)

Eu tenho só alguns PC simples, assim que der vou comprar meu servidor, mas já preciso juntar algumas coisinhas nos PCs que tenho.

Eu não preciso de orquestradores pra VMs, uma Web GUI básica já me resolve, pode ser as que vem junto.
Uma opção livre que promete unir os diferentes hypervisors é o OpenStack.
Não achei um linux pronto com OpenStack e um Hypervisor, aceito sugestões.

Eu preciso de orquestração de containters, com certeza não necessito de tudo que o kubernets oferece, Swarm já me atende uso ele em desenvolvimento.

Então eu escolhi o xcp-ng com xoa livre.
Não consegui ativar o pluging do xoa pra gerenciar conteiners no CoreOS.
Então optei pelo Rancher no RancherOS.
