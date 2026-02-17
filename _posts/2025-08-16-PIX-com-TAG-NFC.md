
Fazer um pix parece muito fácil não é?
1. Destravar o celular com Biometria
2. Tem que achar o app do banco
3. Logar no app com senha do app
4. Ir na área de pix
5. Escolher pagar pix com QR-Code
6. Mirar a câmera no QR-Code
7. Aguardar o foco da câmera funcionar
8. Fazer alguns passos de confirmação
9. Digitar sua senha de pagamento

Nesse processo você digitou no meio da rua 2 senhas do seu banco.

Eu prefiro pagar com débito:
1. Destravar o celular com Biometria
2. Encostar o celular

Mas se der para fazer PIX por aproximação?
1. Destravar o celular com Biometria
2. Encostar o celular
3. Digitar o valor
4. Confirmar com Biometria

Não é tão fácil como débito, mas dá para pagar dando algum benefício para o vendedor.
Primeiro compre uma TAG adesiva ou um cartão NFC.
Baixe o app NFC Tool: <https://play.google.com/store/apps/details?id=com.wakdev.wdnfc>
Usando o app do seu banco crie um pagamento PIX com ou sem valor, com identificação se preferir. Copie o PIX "PIX Copia e Cola".
No site <https://www.urlencoder.org/pt/> você pode codificar o seu PIX no formato "URL Encoder". Isso vai remover espaços e substituir por "%20" e modificar algum caráter especial se existir.
Agora, no NFC Tool, você vai gravar no cartão uma URL Personalizada. Digite:

pix://localhost?qr=
Cole seu PIX codificado, vai ficar algo assim:
pix://localhost?qr=00020126650014br.gov.bcb.pix01.....B9rp6304E416
Escolha gravar no cartão e pronto.
Proteja seu cartão com senha para nenhum engraçadinho trocar o PIX do seu cartão e direcionar seus pagamentos para ele.

FONTE: https://www.bcb.gov.br/content/estabilidadefinanceira/pix/especificacoes_pix_aproximacao_android.pdf