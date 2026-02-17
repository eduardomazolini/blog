---
---

## Instação do podman

O Docker poderia ser usado mas vou dar preferencia para o podman. Com isso podemos levantar as 2 aplicações de forma mais isolada do sistema base.

IMPORTANTE! Portainer não sobe o stack tem que ser por linha de comando. Docker da problema parece que estamos vivendo uma migração do modo OCI de trabalhar para o CDI. Não sei entedi certo.
  
  
    sudo apt update
    sudo apt-get -y install podman podman-compose
    sudo systemctl enable --now podman.socket

## Para usar placa NVIDIA alguns passos são necessários

Infelizmente isso tem que ser feito na maquina base do docker. Se ela for virtual os Drivers também devem ser instalados no Host também.

### instalação básica do drives da NVIDIA
  
  
    sudo apt update
    sudo apt install nvidia-driver linux-headers-$(uname -r)

### Instalar nvidia container toolkit

Fonte: <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation>
  
```
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
        | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
    curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
        | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
        | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    sudo apt-get update
  
  
    export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.17.8-1
        sudo apt-get install -y \
          nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
          nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
          libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
          libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```
### Instalar e ativar o Container Device Interface (CDI)

Fontes:

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html
https://docs.docker.com/reference/cli/docker/container/run/#cdi-devices
https://docs.docker.com/build/building/cdi/
https://docs.docker.com/reference/cli/docker/container/run/#gpus
https://docs.docker.com/compose/how-tos/gpu-support/
  
```
    sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```

#### Testando o container

Fonte: <https://docs.podman.io/en/v4.6.0/markdown/options/security-opt.html>

Esse é o modo CDI
  
```
    podman run --rm \
        --device nvidia.com/gpu=0 \
        --security-opt=label=disable \
        ubuntu nvidia-smi -L
  
  
    services:
      test:
        image: docker.io/nvidia/cuda:12.3.1-base-ubuntu20.04
    	runtime: nvidia
        command: nvidia-smi
        devices:
          - nvidia.com/gpu=all
```  

Esse é o modo nvidia-container-toolkit
  
```
    podman run --rm \
        --gpus=all \
        ubuntu nvidia-smi -L
  
  
    services:
      test:
        image: docker.io/nvidia/cuda:12.3.1-base-ubuntu20.04
    	runtime: nvidia
        command: nvidia-smi
        deploy:
          resources:
            reservations:
              devices:
                - driver: nvidia
                  count: 1
                  capabilities: [gpu]
```  

## Instalar Ollama
  
```
    podman run -d -v ollama:/root/.ollama \
        --gpus=all \
        --security-opt=label=disable \
        -p 11434:11434 \
        --name ollama \
        --security-opt=label=disable \
        ollama/ollama
  
  
    podman run -d -v ollama:/root/.ollama \
        --device nvidia.com/gpu=0 \
        --security-opt=label=disable \
        -p 11434:11434 \
        --restart always \
        --name ollama \
        docker.io/ollama/ollama
```

## Instalar Open WebUI
  
  
```
    podman run -d -v open-webui:/app/backend/data \
        -p 3000:8080 \
        -e OLLAMA_BASE_URL=http://ollama:11434 \
        --name open-webui \
        --restart always \
        ghcr.io/open-webui/open-webui:main
```

## Docker Compose
  
```
    version: '3.8'
  
    services:
      ollama:
        # O serviço principal Ollama para rodar modelos de linguagem
        image: docker.io/ollama/ollama
        container_name: ollama
        # Removemos a opção --restart=always do comando original, mas 
        # é altamente recomendado mantê-la para produção.
        # restart: always 
      
        # Mapeamento de portas para que o Ollama seja acessível fora do Podman
        # Você usará esta porta para acessar a interface da web (via proxy interno)
        # ou para rodar modelos diretamente.
        ports:
          - "11434:11434"
        
        # Configuração de recursos de GPU
        deploy:
          resources:
            reservations:
              devices:
                # Especifica a GPU a ser usada (dispositivo 0 neste caso)
                - driver: nvidia
                  device_ids: ['0']
                  capabilities: [gpu]
                
        # Desabilita o rótulo de segurança (necessário para rodar o Ollama com GPU em certos setups Linux)
        security_opt:
          - label=disable
        
        # Mapeia o volume para persistir os modelos baixados e as configurações
        volumes:
          - ollama_data:/root/.ollama
        
      open-webui:
        # A interface de usuário baseada na web para interagir com o Ollama
        image: ghcr.io/open-webui/open-webui:main
        container_name: open-webui
        restart: always 
      
        # Mapeamento de portas para acessar a interface web no host (porta 3000)
        ports:
          - "3000:8080" # Host:3000 -> Container:8080
        
        # Variável de ambiente para que o Open WebUI saiba onde encontrar o Ollama.
        # Usamos o nome do serviço 'ollama' + a porta interna (11434)
        environment:
          - OLLAMA_BASE_URL=http://ollama:11434
        
        # Volume para persistir os dados do usuário, sessões e configurações do Open WebUI
        volumes:
          - open_webui_data:/app/backend/data
  
    # Definição dos volumes nomeados
    volumes:
      ollama_data:
        driver: local
      open_webui_data:
        driver: local
  
    networks:
      default:
        enable_ipv6: true
```
