---
---

Eu uso warp-cli em um container docker pra criar as conexões e com os comando abaixo da pra printar os valores dos JSON dos arquivos de configuração.

Lembre de não remover ou desconectar por linha de comando ou esses valores vão se tonar inválidos. 

echo $(jq -r .secret_key < /var/lib/cloudflare-warp/reg.json)
echo $(jq -r .public_key < /var/lib/cloudflare-warp/conf.json) 
echo $(jq -r '.endpoints[0].v4' /var/lib/cloudflare-warp/conf.json) 
echo $(jq -r .interface.v4 < /var/lib/cloudflare-warp/conf.json)/12

fonte: <https://github.com/AnimMouse/wgcf-connector/blob/main/wgcf-connector.sh>



