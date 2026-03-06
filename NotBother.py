from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8553418621:AAGtJaBVx35AvX1UCTorsuq45_dEJixzaGo"


# Instruction command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "👋 Welcome to the Repeat Bot!\n\n"
        "📌 How to use:\n"
        "/repeat MESSAGE NUMBER\n\n"
        "Example:\n"
        "/repeat hello 5\n\n"
        "The bot will repeat your message the number of times you choose."
    )

    await update.message.reply_text(message)


# Repeat command
async def repeat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ Usage:\n/repeat message number\n\nExample:\n/repeat not an elephant 10"
        )
        return

    try:
        count = int(context.args[-1])   # last word = number
    except ValueError:
        await update.message.reply_text("❌ The last word must be a number.")
        return

    text = " ".join(context.args[:-1])  # message before number

    for i in range(count):
        await update.message.reply_text(text)


app = ApplicationBuilder().token(TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("repeat", repeat))

print("Bot running...")

app.run_polling()