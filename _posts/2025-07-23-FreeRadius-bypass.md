---
tags: [linux, Mikrotik]
---
Imaginem se um dia der M... você perdeu seu banco de dados, mas precisa acessar seus equipamentos, precisa liberar o mínimo de acesso aos clientes.

Eu ainda não passei por isso mas a alguns dias o MKSolutions deu uma travada quando eu atualizei um Mikrotik ele registra uma conta com data de 1900 e não remove, eu uso NTP em todos os equipamentos mas algo acontece e sempe que atualizo da verão 6 pra 7 o MKSolutions trava.

Bom isso me deixou muito incomodado e fiquei alguns dias batendo cabeça pra pensar quanto tempo eu levo pra levantar um freeradius genérico.

O modo mais rápido que achei foi baixar um conainer docker

```
docker run --name radius -p 1812-1813:1812-1813/udp -d freeradius/freeradius-server:latest -X
```

Agora a primeira limitação é que vc precisa saber o secret se seu nas manda o secret.

```
/etc/freeradius/clients.conf 
```

```
client generico {
		 ipaddr = 0.0.0.0/0
		 proto = *
		 secret = testing123 #ajuste esse valor ou nada vai funcionar
		 require_message_authenticator = no
		 nas_type = other 
}
```

Para autenticar os clientes vc tem 4 protocolos configurados mas pense que são 2 formas:

* PAP onde a senha é enviada em texto claro e vc pode aceitar qualquer senha.
* CHAP/MSCHAP/MSCHAP2 onde a senha não é enviada e vc ainda precisa retornar uma confirmação que vc sabia qual era a senha. Se todos os seus clientes tiverem usuários diferentes mas a mesma senha também não é um problema.

Para acessar o Mikrotik vc pode querer usar ssh e ai fica fácil nem te pede a senha, ou pode insistir em usar o Winbox que usa CHAP. Vc precisa saber qual é a senha.

Eu criei um modulo python3 vc vai olhar e se souber o minimo vai sacar o que deve mudar nele.

O arquivo radiusd.py fica em /etc/freeradius/mods-config/python3/radiusd.py mas só usei uma constante RLM_MODULE_OK o valor dela é 2 numérico se quiser colocar direto e não usar import.

```
#! /usr/bin/env python3
import radiusd

def authorize(p):
	reply = (
			('Mikrotik-Group', 'full'), #libera acesso ao mikrotik
			('Mikrotik-Address-List', 'radiusList'),
			('Mikrotik-Rate-Limit', '440m/880m 0k/0k 0k/0k 0/0 8 60m/60m'),
			('Huawei-Output-Average-Rate', '829440000'),
			('Huawei-Input-Average-Rate', '409600000'),
			('Framed-Pool', 'poolRadius'),
			('Framed-IP-Address', '192.168.100.254'),
			('Mikrotik-Wireless-PSK', '1234568'),
		)

	config = (
			('Cleartext-Password', 'senha_padrao'), # necessario para mschap chap
			('Auth-Type', 'authmod'),
		)

	return (radiusd.RLM_MODULE_OK, reply, config)

def authenticate(p):
	request = dict(p)
	print("*** authenticate ***")
	print(request.get("User-Name", "sem nome"))
	return radiusd.RLM_MODULE_OK
```

Você vai precisar declarar seu modulo:

/etc/freeradius/mods-enabled/python3
```
python3 authmod {
	module = authmod
	python_path = /etc/freeradius/python3
	mod_authorize = authmod
	func_authorize = authorize
	mod_authenticate = authmod
	func_authenticate = authenticate
}
```

E depois de declarar precisa usar então configurar o seu uso no "site".

Aqui temos uma decisão para tomar.

* Se vc tirar # do que esta no arquivo abaixo vc consegue acesso ao mikrotik por ssh sem colocar senha, mas não vai conseguir acessar por winbox nem autenticar clientes pppoe por chap, só vão logar por PAP no PPPoE.
* Sem tirar esse comentário qualquer usuário que usar a "senha_padrao" tem acesso. Ou seja não tem muita vantagem.

/etc/freeradius/sites-enabled/default
```
authorize {
	authmod
}
authenticate {
	# só tire o comentário para acessar por ssh sem senha 
	# Auth-Type mschap {
	#   authmod
	# }
	authmod
}
```

Espero que seja útil para alguém

Se vc não domina muito bem docker vou deixar alguns comandos que usei muito:

Copiar da sua maquina para o container e executar alguns comando dentro dele:

```
docker cp mods-available/python3 radius:/etc/freeradius/mods-available/python3
docker exec radius ln -s /etc/freeradius/mods-available/python3 /etc/freeradius/mods-enabled/python3
docker exec radius mkdir /etc/freeradius/python3
docker cp python3/authmod.py radius:/etc/freeradius/python3/authmod.py
docker cp python3/__init__.py radius:/etc/freeradius/python3/__init__.py
docker exec radius cp /etc/freeradius/mods-config/python3/radiusd.py /etc/freeradius/python3/
docker cp sites-available/default radius:/etc/freeradius/sites-available/default
```

Reiniciar o contaner e olhar o log
```
docker stop radius
docker start radius
docker logs radius
```

Exibir arquivos de configuração sem comentários:

```
docker exec radius grep -vE '^\s*$|^\s*#' /etc/freeradius/clients.conf 
```


Entrar no shell do container:

```
docker exec -it radius bash
```

Testar o login de forma básica
```
radtest edu 123 localhost 0 testing123
```
