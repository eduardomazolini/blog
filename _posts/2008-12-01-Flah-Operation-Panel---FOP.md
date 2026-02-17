---
tags: [asterisk, Flash Operation Panel, FOP]
---

```
version 0.29 released:

This version fixes the "red/green flashing problem" that is experienced by using the latest Flash Player from Adobe.

So, if you have some machines that work ok, and some that have problems, then you will need to update FOP to this version, or install an older version of the flash player on the affected machines, but I do not recommend that since Adobe patched a security issue in the last version, so you should be updating all of your flash players together with FOP.

If you use FreePBX (that is, trixbox, elastix or some other distribution that includes it) you have to replace only op_server.pl and operator_panel.swf and then add one line to op_server.cfg:

use_amportal_conf=1

just below the [general] section.

All those files are inside /var/www/html/panel. And finally issue a "killall op_server.pl" at the linux console to restart the panel.
```

Fonte: [http://www.asternic.org/](http://www.asternic.org/)


Tradução livre: 
```
Se vc já tem um FOP instalado mas esta piscando depois que vc atualizou seu flash.
Execute os 2 passos:

1) Copie os arquivos abaixo da nova versão 0.29 para o diretório "/var/www/html/panel"


  * op_server.pl
  * operator_panel.swf



2) Edite o arquivo "op_server.cfg" que também esta nesse diretório, coloque a seguinte linha logo abaixo da linha que esta escrito [general].

  * use_amportal_conf=1
```

## Atualização 2026

O FOP foi só até a versão 0.30, o site original não existe mais. Agora a versão existente é grátis para um certo número de ramais, mas não livre.
