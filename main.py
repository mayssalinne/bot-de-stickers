from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")  # ou apenas 'TOKEN = "seu_token_aqui"' para testes locais

async def start(update, context):
    await update.message.reply_text("Olá! Bot funcionando!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    app.run_polling()
