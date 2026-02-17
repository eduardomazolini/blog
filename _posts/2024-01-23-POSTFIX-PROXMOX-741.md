---
tags: [Proxmox]
---

Como eu configurei meu Proxmox para enviar e-mail

O e-mail de origem é editado em:


> Datacenter -> Options -> Email from address




Editar /etc/postfix/main.cf

> .
> .
> .
> #relayhost =
> .
> .
> .
> #Inserido por Eduardo xx/xx/2024
> relayhost = [smtp-server.example.com]:587
> smtp_use_tls = yes
> smtp_tls_security_level = encrypt
> smtp_tls_note_starttls_offer = yes
> smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
> smtp_sasl_auth_enable = yes
> smtp_sasl_password_maps = hash:/etc/postfix/sasl/sasl_passwd
> smtp_sasl_security_options = noanonymous
> # foi necessario instalar pacote: apt install libsasl2-modules

 

Instalar pacote 

> apt install libsasl2-modules 

 

Editar /etc/postfix/sasl/sasl_passwd

> [smtp-server.example.com]:587 userSMTP:passSMTP




Gerar hash da senha no .db

> postmap /etc/postfix/sasl/sasl_passwd

> chmod 600 /etc/postfix/sasl/sasl_passwd /etc/postfix/sasl/sasl_passwd.db 




Reiniciar postfix

> service postfix restart




Testar

>  echo "Corpo do e-mail" | mail -s "Assunto do e-mail" destino@example.com
