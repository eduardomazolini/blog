---
tags: [asterisk]
---

Pra quem for usar Elastix tem que instalar os modulos do asterisk:
res_jabber.so
chan_gtalk.so
E também:
wget http://packages.sw.be/iksemel/iksemel-1.3-1.el5.rf.i386.rpm
wget http://centos.oi.com.br/5/os/i386/CentOS/perl-IO-Socket-SSL-1.01-1.fc6.noarch.rpm

# Atualização 2026

O projeto Elastix morreu, Isabel apareceu como alternativa e acho que também morreu.
Google Talk, já mudou de nome para Hangouts e agora Google Chat, foi integrado ao Meeting e infelizmente fechou para o XMPP.
Com as novas propagandas no WhatsApp, acredito que muita gente vai começar a procurar uma alternativa de comunicação por mensagem.
Apesar do [Signal](https://signal.org/) para privacidade e [Telegram](https://telegram.org/) para bots serem as alternativas prontas.
Hospedar o [Matrix](https://matrix.org/) ainda é um problema pq exige muitas sincronizações e muitos dados.
Eu particularmente ainda gostaria que o mundo adotasse o XMPP usando o DNS SRV para busca de federação.