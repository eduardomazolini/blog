 O site do [Virt-Manage](https://virt-manager.org/)r mostra que para instalar ele é simples basta digitar:
```
apt-get install virt-manager

```
Mas você precisa digitar a senha para fazer sudo cada vez que abre ao menos que coloque seus usuários no grupo libvirt: 

```
sudo usermod -aG libvirt aluno
sudo usermod -aG libvirt emazolini

```
Se quiser acessar remoto vai precisar de um netcat com opção -U:
sudo apt install netcat-openbsd

Por fim você vai ficar feliz até voltar no outro dia e perceber que sua maquina não sobe mais por um erro de rede.
Pra resolver isso ative a rede default:

$ sudo virsh net-list --all

| Nome    | Estado  | Auto-iniciar | Persistente |
| ------- | ------- | ------------ | ----------- |
| default | inativo | não          | sim         |

$ sudo virsh net-start default
Rede default iniciada

$ sudo virsh net-autostart default
A rede default foi marcada como auto-iniciada

$ sudo virsh net-list --all

| Nome    | Estado | Auto-iniciar | Persistente |
| ------- | ------ | ------------ | ----------- |
| default | ativo  | sim          | sim         |
