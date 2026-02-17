---
---

A área de segurança de uma empresa me avisou sobre uma vulnerabilidade no PHP do Elastix.
Vulnerabilidade:

PHP imap_mail_compose() Stack Buffer Overflow Vulnerability 
CVE-2007-1825 
CVSS 8.0

Consegui fazer a atualização segue a dica de como ocorreu:
1)      Crie um repo para um centos completo e coloque uma instrução para não atualizar para 5.3 eu queria instalar 5.2

	exclude = php*5.3* (Fonte: http://en.ispdoc.com/index.php/Updating_PHP_in_CentOS_Linux)
    vi /etc/yum.repos.d/RedHat.repo

	[REDHAT1]
    name=RedHat1
    baseurl=http://repo.webtatic.com/yum/centos/5/i386/
	exclude=kernel*
    exclude=redhat-logos
    exclude = php*5.3*
    enabled=1
  
2)      Acerte as opções de proxy se necessário 

	vi /etc/yum/pluginconf.d/fastestmirror.conf

	proxy=http://192.168.0.2:80
    proxy_username=dominiocomifem\-br\\usuario
    proxy_password=XXXXXX
    declare -x http_proxy="http://dominiocomifem\-br\\usuario:xxxxxxx@192.168.0.2:80"
  
3)      Atualize e baixe também o pacote php-process (Fonte: http://www.elastix.org/component/kunena/31/39393/)

	yum install php php-process –nogpgcheck

## Atualização para 2026

Olhando hoje para esse post vejo a importância das empresas rodarem simulações de ataques internos e terem uma equipe focada em segurança.
Isso na época me levou um aprendizado de como proceder pra arrumar um problema, mas também me moldou a olhar para os problemas de segurança e a preocupação em manter firewalls internos e atualizações dos sistemas independente de eu precisar de uma nova facilidade, mas sim pq sei que melhorias de segurança vão sempre ser implantadas.