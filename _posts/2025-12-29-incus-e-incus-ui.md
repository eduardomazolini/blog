---
---

Pré Instalação do Incus
  
  
    # 1. Criar o diretório de chaves se não existir
    sudo mkdir -p /etc/apt/keyrings/
  
    # 2. Baixar a chave GPG do Zabbly
    sudo curl -fsSL https://pkgs.zabbly.com/key.asc -o /etc/apt/keyrings/zabbly.asc
  
    # 3. Adicionar o repositório específico para o Debian Trixie (13)
    # Vamos apenas criar o arquivo, ainda não daremos 'apt update'
    echo "deb [signed-by=/etc/apt/keyrings/zabbly.asc] https://pkgs.zabbly.com/incus/stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/zabbly-incus.list
  
    # 4. Verificar se o arquivo foi criado corretamente e aponta para 'trixie'
    cat /etc/apt/sources.list.d/zabbly-incus.list
  

Instalação
  
  
    # 1. Atualizar os índices
    sudo apt update
  
    # 2. Instalar o Incus e a Interface Web (Canonical UI)
    # O pacote 'incus' traz o suporte a containers e VMs (via QEMU)
    sudo apt install incus incus-ui-canonical
  

Pós Instalação
  
  
    # 1. Adicionar seu usuário ao grupo do incus-admin
    sudo usermod -aG incus-admin $(whoami)
  
    # 2. Verificar se o serviço está ativo e rodando
    systemctl status incus
  
    # 3. Aplicar a mudança de grupo na sessão atual (evita ter que deslogar)
    newgrp incus-admin
  
    # 4. Testar se o comando básico responde (deve retornar vazio ou erro de init, mas não "command not found")
    incus list
  

Configurar
  
  
    sudo incus admin init
  

Usar os dados salvos da última configuração
  
  
    cat init.yaml | incus admin init --preseed
  

Geração da senha para o cloud-init
  
  
    python3 -c 'import crypt; print(crypt.crypt("suasenha", crypt.mksalt(crypt.METHOD_SHA512)))'
  

Configuração do cloud-init
  
  
    #cloud-config
    # Adicione este bloco fora da seção 'users'
    ssh_pwauth: true  # Permite senha se a chave falhar (opcional)
    package_update: true
    packages:
      - openssh-server
    users:
      - name: emazolini
        groups: sudo
        shell: /bin/bash
        sudo: ALL=(ALL) NOPASSWD:ALL
        lock_passwd: false
        passwd: "$6$7sEVbA2QElMP.e7c$5w.mboIKzN8BnkD.DuBjtHqbm4m9fQUct1ZSELl3g8DjbKDJetD5Jt6RrgHuuUSavQh.oHdzjxr79z39jLNpF1"
        ssh_authorized_keys:
          - ssh-rsa AAAAB3Nza...usuario@notebook
  
