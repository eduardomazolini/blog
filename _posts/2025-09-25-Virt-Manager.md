 O site do [Virt-Manage](https://virt-manager.org/)r mostra que para instalar ele é simples basta digitar:
```
sudo apt install virt-manager

```
Mas você precisa digitar a senha para fazer sudo cada vez que abre ao menos que coloque seus usuários no grupo libvirt: 

```
sudo usermod -aG libvirt aluno
sudo usermod -aG libvirt $USER
```

Se quiser acessar remoto vai precisar de um netcat com opção -U:
```
sudo apt install netcat-openbsd
```

Por fim você vai ficar feliz até voltar no outro dia e perceber que sua maquina não sobe mais por um erro de rede.
Pra resolver isso ative a rede default e marque para inicio automatico:

Liste o estado atual:
```
sudo virsh net-list --all
```
```
| Nome    | Estado  | Auto-iniciar | Persistente |
| ------- | ------- | ------------ | ----------- |
| default | inativo | não          | sim         |
```

Ative a rede se você já tiver reiniciado:
```
sudo virsh net-start default
```

Configure para sempre iniciar:
```
sudo virsh net-autostart default
```

Confrime se a rede default foi marcada para auto-iniciar:
```
sudo virsh net-list --all
```

Agora a saída deve ser algo como:
```
| Nome    | Estado | Auto-iniciar | Persistente |
| ------- | ------ | ------------ | ----------- |
| default | ativo  | sim          | sim         |
```
