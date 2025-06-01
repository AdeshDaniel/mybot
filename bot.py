from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7688238747:AAFyyAnQxrEijQ8Zzo6UZ1oY8CjmgT2DXDs'
WEB_APP_URL = 'https://mybot-k8ng.onrender.com'  # Replace with your deployed Mini App URL

ADMIN_ID = 5452541589  # Replace with your Telegram user ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Login via Telegram", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome! Click the button below to verify your Telegram account:",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
