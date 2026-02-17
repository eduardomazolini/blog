---
---

Algumas vezes precisei criar um site hospedado em minha própria maquina e para isso usei o XAMP de http://www.apachefriends.org/pt_br/xampp.html
Para fazer controle de acesso a pagina sem fazer uma grande integração com LDAP ou AD usei o modulo SSPI (Windows Security Support Provider Interface) que pode ser baixado do sourceforge: http://sourceforge.net/projects/mod-auth-sspi/files/latest/download?source=files
Muito fácil de usar ao baixar o zip vai achar o arquivo my_cfg.txt com exemplo de utilização.
Eu usei para saber o usuário e depois validava dentro do código da pagina assim poderia dar uma mensagem de negação personalizada.
