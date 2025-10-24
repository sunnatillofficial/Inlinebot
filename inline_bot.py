from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 O'zingizning tokeningizni shu joyga yozing
TOKEN = "8126626814:AAFfPsP-8tk7DPQG4gI9yJIbk_Zx6qH4KJw"

# /start buyrug'i bosilganda tugma chiqadi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎥 Videoni ko‘rish", callback_data="video")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Quyidagi tugmani bosing 👇", reply_markup=reply_markup)

# Tugma bosilganda ishlaydigan funksiya
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "video":
        video_url = "https://t.me/game_esence/368"
        await query.message.reply_video(video_url, caption="🎥 Mana siz so‘ragan video!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("✅ Bot ishga tushdi...")
app.run_polling()