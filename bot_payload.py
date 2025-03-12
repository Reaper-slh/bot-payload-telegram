import random
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Configuração do log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Estados da conversa
ESCOLHENDO_APP, ESPERANDO_DOMINIOS = range(2)

# Token do Bot (SUBSTITUA PELO SEU)
TOKEN = "SEU_TOKEN_AQUI"

# Lista de métodos HTTP disponíveis para rotação (adicionados novos métodos)
metodos = [
    "GET", "POST", "CONNECT", "OPTIONS", "HEAD",
    "HTTP-BUG", "DELETE", "TRACE", "PUT", "MOVE", "PATCH"
]

# Lista de User-Agents para simular diferentes dispositivos
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 10)"
]

# Formata a payload para o app escolhido
def gerar_payload(dominios, app):
    metodo_atual = random.choice(metodos)
    dominio_atual = random.choice(dominios)
    user_agent_atual = random.choice(user_agents)

    if app == "DTunnel":
        payload = f"""{metodo_atual} http://{dominio_atual}/ HTTP/1.1\r\nHost: {dominio_atual}\r\nUser-Agent: {user_agent_atual}\r\nConnection: Keep-Alive\r\n\r\n"""
    
    elif app == "HTTP Injector":
        payload = f"""{metodo_atual} http://{dominio_atual}/ HTTP/1.1[crlf]Host: {dominio_atual}[crlf]User-Agent: {user_agent_atual}[crlf]Connection: Keep-Alive[crlf][crlf]"""
    
    elif app == "Conecta4G":
        payload = f"""{metodo_atual} http://{dominio_atual}/ HTTP/1.1\nHost: {dominio_atual}\nUser-Agent: {user_agent_atual}\nConnection: Keep-Alive\n\n"""
    
    else:
        payload = "❌ Aplicativo não suportado!"
    
    return payload

# Comando /start
def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [["DTunnel", "HTTP Injector", "Conecta4G"]]
    update.message.reply_text(
        "Olá! Escolha para qual aplicativo deseja gerar a payload:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return ESCOLHENDO_APP

# Escolher aplicativo
def escolher_app(update: Update, context: CallbackContext) -> int:
    app_escolhido = update.message.text
    context.user_data["app"] = app_escolhido
    
    update.message.reply_text(f"Você escolheu: {app_escolhido}\nAgora, envie os domínios separados por espaço.")
    return ESPERANDO_DOMINIOS

# Receber domínios e gerar a payload
def receber_dominios(update: Update, context: CallbackContext) -> int:
    dominios = update.message.text.split()
    app_escolhido = context.user_data.get("app", "")

    if not dominios:
        update.message.reply_text("Por favor, envie pelo menos um domínio válido.")
        return ESPERANDO_DOMINIOS

    payload = gerar_payload(dominios, app_escolhido)
    update.message.reply_text(f"🔹 Sua Payload para *{app_escolhido}* 🔹\n\n```{payload}```", parse_mode="Markdown")

    return ConversationHandler.END

# Comando /menu
def menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📌 *Comandos disponíveis:*\n\n"
        "✅ /payload - Gerar payload para DTunnel, HTTP Injector ou Conecta4G\n"
        "✅ /menu - Exibir esta lista de comandos\n"
        "✅ /start - Iniciar a configuração de uma nova payload\n",
        parse_mode="Markdown"
    )

# Configuração do bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Adiciona o comando /menu
    dp.add_handler(CommandHandler("menu", menu))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("payload", start)],
        states={
            ESCOLHENDO_APP: [MessageHandler(Filters.text & ~Filters.command, escolher_app)],
            ESPERANDO_DOMINIOS: [MessageHandler(Filters.text & ~Filters.command, receber_dominios)]
        },
        fallbacks=[]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
