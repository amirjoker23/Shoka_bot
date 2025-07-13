from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# توکن رباتت رو بذار اینجا
TOKEN = "7666433350:AAEtnztPRm2s4olljqaOLiSl0Lyr08u9Y-o"
# آی‌دی عددی تلگرام شما (ادمین)
ADMIN_ID = 1571446410

# لیست سؤالات فرم
questions = [
    "👤 نام و نام خانوادگی:",
    "📞 شماره تماس:",
    "🆔 کد ملی:",
    "💍 وضعیت تأهل (مجرد / متأهل):",
    "📍 آدرس و تاریخ تولد:",
    "💼 شغل:",
    "📮 کد پستی:",
    "👥 کد ملی ذینفع در صورت فوت:",
    "🎂 تاریخ تولد ذینفع:",
    "📌 طرح مورد نظر (ماهانه / سالانه / یکجا):",
    "💳 نحوه پرداخت (کارت به کارت / درگاه / حضوری):"
]

# ذخیره وضعیت هر کاربر
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_data[user_id] = {"step": 0, "answers": []}
    await update.message.reply_text("سلام 😊 به فرم مشاوره بیمه سرمایه‌گذاری شوکا خوش اومدی.\nلطفاً به سؤال‌ها یکی‌یکی پاسخ بده.\n\n" + questions[0])

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    message = update.message.text.strip()

    if user_id not in user_data:
        await update.message.reply_text("لطفاً اول /start رو بزن.")
        return

    state = user_data[user_id]
    step = state["step"]
    if step < len(questions):
        state["answers"].append(message)
        state["step"] += 1

    if state["step"] < len(questions):
        await update.message.reply_text(questions[state["step"]])
    else:
        summary = "\n".join([f"{i+1}. {questions[i]} {ans}" for i, ans in enumerate(state["answers"])])
        
        # پیام برای کاربر
        await update.message.reply_text("✅ اطلاعات شما با موفقیت ثبت شد:\n\n" + summary + "\n\nممنون! به‌زودی با شما تماس می‌گیریم ☎️")

        # پیام برای ادمین
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"📥 فرم جدید ثبت شد:\n\n{summary}")

        # حذف وضعیت کاربر
        del user_data[user_id]

# تنظیمات ربات
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

if __name__ == "__main__":
    print("🤖 ربات در حال اجراست...")
    app.run_polling()