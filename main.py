import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuração básica de log (pra gente ver o que acontece no Render)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- FUNÇÃO MAIS SIMPLES POSSÍVEL PRA TESTAR ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde ao comando /start com uma mensagem."""
    await update.message.reply_text('FUNCIONOU PORRA! O BOT TA VIVO!')

# --- FUNÇÃO PRINCIPAL ---
def main():
    """Inicia o bot."""
    # Pega o token do ambiente
    token = os.environ.get('TELEGRAM_TOKEN')

    # Cria a aplicação
    application = ApplicationBuilder().token(token).build()

    # Adiciona o handler pro comando /start
    application.add_handler(CommandHandler('start', start))

    # Inicia o bot (polling)
    print("Bot iniciado com sucesso! Aguardando mensagens...")
    application.run_polling()

if __name__ == '__main__':
    main()
