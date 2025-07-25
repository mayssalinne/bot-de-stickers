from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("7956634632:AAFijJtLbal-wJxZ8eb4m9u1a69hvBat1Tc")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá, eu sou seu bot de stickers! Use /newpack para começar 👑")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
