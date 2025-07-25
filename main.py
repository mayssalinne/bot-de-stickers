import telegram 
print(f"Versão do python-telegram-bot: {telegram.__version__}")
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")  # ou coloque diretamente: TOKEN = "seu_token_aqui"

# Função do comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Bot está funcionando!")

# Inicializando o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
