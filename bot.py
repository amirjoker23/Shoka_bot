from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7666433350:AAEtnztPRm2s4olljqaOLiSl0Lyr08u9Y-o"
ADMIN_ID = 1571446410

questions = [
    "👤 نام و نام خانوادگی:",
    "📞 شماره تماس:",
    "🆔 کد ملی:",
    "💍 وضعیت تأهل:",
    "📍 آدرس و تاریخ تولد:",
    "💼 شغل:",
    "📮 کد پستی:",
    "👥 کد ملی ذینفع در صورت فوت:",
    "🎂 تاریخ تولد ذینفع:",
    "📌 طرح مورد نظر:"
]

button_options = {
    3: [["مجرد", "متأهل"]],
    9: [["ماهانه", "سالانه", "یکجا"]],
}

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_data[user_id] = {"step": 0, "answers": []}
    await send_question(update, context, user_id)

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    message = update.message.text.strip()

    if user_id not in user_data:
        await update.message.reply_text("لطفاً اول /start رو بزن.")
        return

    state = user_data[user_id]
    step = state["step"]

    state["answers"].append(message)
    state["step"] += 1

    if state["step"] < len(questions):
        await send_question(update, context, user_id)
    else:
        summary = "\n".join([f"{i+1}. {questions[i]} {ans}" for i, ans in enumerate(state["answers"])])
        
        # برای کاربر
        await update.message.reply_text(
            "✅ اطلاعات شما با موفقیت ثبت شد:\n\n"
            + summary
            + "\n\n🧾 لینک پرداخت به زودی از طرف شرکت برای شما ارسال خواهد شد.",
            reply_markup=ReplyKeyboardRemove()
        )

        # برای ادمین
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"📥 فرم جدید ثبت شد:\n\n{summary}")

        del user_data[user_id]

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE, user_id):
    step = user_data[user_id]["step"]
    question = questions[step]

    if step in button_options:
        reply_markup = ReplyKeyboardMarkup(button_options[step], one_time_keyboard=True, resize_keyboard=True)
    else:
        reply_markup = ReplyKeyboardRemove()

    await context.bot.send_message(chat_id=user_id, text=question, reply_markup=reply_markup)

# اجرا
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

if __name__ == "__main__":
    print("✅ ربات آماده‌ست.")
    app.run_polling()
