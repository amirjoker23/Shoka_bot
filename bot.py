import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, filters, ContextTypes

TOKEN = "7666433350:AAEtnztPRm2s4olljqaOLiSl0Lyr08u9Y-o"

# مراحل گفتگو
(NAME, PHONE, NATIONAL_ID, MARITAL, ADDRESS, BIRTHDAY, JOB, POSTAL, BENEFICIARY_ID, BENEFICIARY_BIRTHDAY) = range(10)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 به بیمه سرمایه‌گذاری شوکا خوش اومدین!\n\nبرای ثبت اطلاعات، لطفا سوالات بعدی رو جواب بدین."
    )
    await update.message.reply_text("👤 لطفا نام و نام خانوادگی خود را وارد کنید:")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("📱 لطفا شماره تماس خود را وارد کنید:")
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("🆔 لطفا کد ملی خود را وارد کنید:")
    return NATIONAL_ID

async def get_national_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['national_id'] = update.message.text
    keyboard = [['متاهل', 'مجرد']]
    await update.message.reply_text(
        "💍 وضعیت تاهل خود را انتخاب کنید:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return MARITAL

async def get_marital(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['marital'] = update.message.text
    await update.message.reply_text("📍 لطفا آدرس محل سکونت خود را وارد کنید:")
    return ADDRESS

async def get_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['address'] = update.message.text
    await update.message.reply_text("📅 لطفا تاریخ تولد خود را وارد کنید (مثال: 1370/01/15):")
    return BIRTHDAY

async def get_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['birthday'] = update.message.text
    await update.message.reply_text("💼 شغل شما چیست؟")
    return JOB

async def get_job(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['job'] = update.message.text
    await update.message.reply_text("🏷️ لطفا کد پستی خود را وارد کنید:")
    return POSTAL

async def get_postal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['postal'] = update.message.text
    await update.message.reply_text("👥 لطفا کد ملی ذینفع در صورت فوت را وارد کنید:")
    return BENEFICIARY_ID

async def get_beneficiary_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['beneficiary_id'] = update.message.text
    await update.message.reply_text("📅 لطفا تاریخ تولد ذینفع را وارد کنید (مثال: 1375/03/22):")
    return BENEFICIARY_BIRTHDAY

async def get_beneficiary_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['beneficiary_birthday'] = update.message.text

    # خلاصه اطلاعات برای ادمین
    summary = "\n".join([f"{key}: {value}" for key, value in context.user_data.items()])
    admin_id = 1571446410  # آیدی عددی خودت رو اینجا گذاشتی

    await context.bot.send_message(chat_id=admin_id, text=f"فرم جدید دریافت شد:\n{summary}")

    await update.message.reply_text("✅ ثبت اطلاعات با موفقیت انجام شد.\nبه زودی لینک پرداخت از طرف شرکت برای شما ارسال می‌شود.")
    return ConversationHandler.END

if name == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
    import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")  # از محیط Render می‌خونه

# مراحل گفتگو
(NAME, PHONE, NATIONAL_ID, MARITAL, ADDRESS, BIRTHDAY, JOB, POSTAL, BENEFICIARY_ID, BENEFICIARY_BIRTHDAY) = range(10)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 به بیمه سرمایه‌گذاری شوکا خوش اومدین!\n\nبرای ثبت اطلاعات، لطفا سوالات بعدی رو جواب بدین."
    )
    await update.message.reply_text("👤 لطفا نام و نام خانوادگی خود را وارد کنید:")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("📱 لطفا شماره تماس خود را وارد کنید:")
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("🆔 لطفا کد ملی خود را وارد کنید:")
    return NATIONAL_ID

async def get_national_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['national_id'] = update.message.text
    keyboard = [['متاهل', 'مجرد']]
    await update.message.reply_text(
        "💍 وضعیت تاهل خود را انتخاب کنید:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return MARITAL

async def get_marital(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['marital'] = update.message.text
    await update.message.reply_text("📍 لطفا آدرس محل سکونت خود را وارد کنید:")
    return ADDRESS

async def get_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['address'] = update.message.text
    await update.message.reply_text("📅 لطفا تاریخ تولد خود را وارد کنید (مثال: 1370/01/15):")
    return BIRTHDAY

async def get_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['birthday'] = update.message.text
    await update.message.reply_text("💼 شغل شما چیست؟")
    return JOB

async def get_job(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['job'] = update.message.text
    await update.message.reply_text("🏷️ لطفا کد پستی خود را وارد کنید:")
    return POSTAL

async def get_postal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['postal'] = update.message.text
    await update.message.reply_text("👥 لطفا کد ملی ذینفع در صورت فوت را وارد کنید:")
    return BENEFICIARY_ID

async def get_beneficiary_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['beneficiary_id'] = update.message.text
    await update.message.reply_text("📅 لطفا تاریخ تولد ذینفع را وارد کنید (مثال: 1375/03/22):")
    return BENEFICIARY_BIRTHDAY

async def get_beneficiary_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['beneficiary_birthday'] = update.message.text

    # خلاصه اطلاعات برای ادمین
    summary = "\n".join([f"{key}: {value}" for key, value in context.user_data.items()])
    admin_id = 1571446410  # آیدی عددی خودت رو اینجا گذاشتی

    await context.bot.send_message(chat_id=admin_id, text=f"فرم جدید دریافت شد:\n{summary}")

    await update.message.reply_text("✅ ثبت اطلاعات با موفقیت انجام شد.\nبه زودی لینک پرداخت از طرف شرکت برای شما ارسال می‌شود.")
    return ConversationHandler.END

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
