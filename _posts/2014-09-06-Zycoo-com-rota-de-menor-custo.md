---
---

O PABX Zycoo especialmente o ZX20 possui um shell (ash) muito limitado.
Então para fazer a consulta tive que fazer todo o AGI.

O que eu fiz está no GitHub:
https://github.com/eduardomazolini/Zycoo-TeleIn

O arquivo extension_general.conf que não é alterado automaticamente portanto é um bom ponto para efetuar alterações.
Na macro macro-trunkdial-failover faço o seguinte:
 \- verifico se a rota a primeira rota (variável ARG1) é o meu tronco MAGICO.
 \- ajusto o telefone para colocar o DDD sem o 0
 \- Aciono o TeleIn.agi.
 \- Substituo a variável Substituo o ARG1 usando a variavél Operadora, retornada pela AGI, que propositadamente é igual as constantes de troncos criadas pelo Zycoo.

Bom proveito!

