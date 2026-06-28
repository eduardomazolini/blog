---
---

Algumas vezes precisei criar um site hospedado em minha própria máquina e para isso usei o XAMPP de http://www.apachefriends.org/pt_br/xampp.html
Para fazer controle de acesso à página sem fazer uma grande integração com LDAP ou AD, usei o módulo SSPI (Windows Security Support Provider Interface) que pode ser baixado do SourceForge: http://sourceforge.net/projects/mod-auth-sspi/files/latest/download?source=files
Muito fácil de usar: ao baixar o zip, vai achar o arquivo my_cfg.txt com exemplo de utilização.
Eu usei para saber o usuário e depois validava dentro do código da página, assim poderia dar uma mensagem de negação personalizada.
