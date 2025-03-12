📌 Bot de Geração de Payload para VPN

Bot do Telegram para gerar payloads dinâmicas compatíveis com DTunnel, HTTP Injector e Conecta4G. Ele permite personalizar domínios e alternar entre diversos métodos HTTP para otimizar conexões.


---

✨ Recursos

✅ Gera payloads automáticas para os principais aplicativos de VPN.
✅ Métodos HTTP suportados: GET, POST, CONNECT, OPTIONS, HEAD, HTTP-BUG, DELETE, TRACE, PUT, MOVE, PATCH.
✅ Compatível com DTunnel, HTTP Injector e Conecta4G.
✅ Comando /menu para listar todas as funções do bot.
✅ Fácil instalação no Termux ou VPS.


---

📌 Como Instalar e Executar no Termux

1️⃣ Instalar o Git e Clonar o Repositório

$ pkg update && pkg upgrade -y
$ pkg install git -y
$ git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
$ cd NOME_DO_REPOSITORIO

2️⃣ Instalar Dependências

$ pkg install python -y
$ pip install python-telegram-bot

3️⃣ Configurar o Token do Bot

Abra o arquivo e edite a linha onde está TOKEN = "SEU_TOKEN_AQUI"

$ nano bot_payload.py

Substitua "SEU_TOKEN_AQUI" pelo seu token do Telegram e salve (CTRL + X, Y, Enter).

4️⃣ Executar o Bot

$ python bot_payload.py


---

📌 Como Usar?

📌 No Telegram, envie os seguintes comandos para o bot:

/start → Inicia a configuração para gerar uma payload.

/payload → Gera uma nova payload escolhendo o app e domínios.

/menu → Lista todos os comandos disponíveis.




🔗 Contato e Suporte

📬 Telegram: https://t.me/Reaperslh
📢 Canal: https://t.me/LimitZero
