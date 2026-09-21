from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8984541039:AAE6Jiw56qTDTvyv3H_0QVvLwnEMU6PFOpY"


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠 ስለ አፓርታማ", callback_data="apartment")],
        [InlineKeyboardButton("💰 ዋጋ", callback_data="price")],
        [InlineKeyboardButton("📍 አድራሻ", callback_data="location")],
        [InlineKeyboardButton("📞 አግኙን", callback_data="contact")],
    ])


def apartment_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏢 የአፓርታማ አይነቶች", callback_data="types")],
        [InlineKeyboardButton("📐 ስፋት", callback_data="size")],
        [InlineKeyboardButton("🔙 ወደ Main Menu", callback_data="home")],
    ])


def types_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1 Bedroom", callback_data="one")],
        [InlineKeyboardButton("2 Bedroom", callback_data="two")],
        [InlineKeyboardButton("3 Bedroom", callback_data="three")],
        [InlineKeyboardButton("🔙 ተመለስ", callback_data="apartment")],
    ])


def bedroom_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 ወደ አፓርታማ", callback_data="types")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="home")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 እንኳን ደህና መጣህ!\n\n"
        "ምን መረጃ ትፈልጋለህ?",
        reply_markup=main_menu()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "home":
        await query.edit_message_text(
            "👋 ዋናው Menu\n\nምን መረጃ ትፈልጋለህ?",
            reply_markup=main_menu()
        )

    elif query.data == "apartment":
        await query.edit_message_text(
            "🏠 ስለ አፓርታማ\n\n"
            "ከታች ያለውን ይምረጡ፦",
            reply_markup=apartment_menu()
        )

    elif query.data == "types":
        await query.edit_message_text(
            "🏢 የሚገኙ የአፓርታማ አይነቶች፦",
            reply_markup=types_menu()
        )

    elif query.data == "one":
        await query.edit_message_text(
            "🏠 1 Bedroom\n\n"
            "የ1 Bedroom ዝርዝር መረጃ እዚህ ይገባል።",
            reply_markup=bedroom_menu()
        )

    elif query.data == "two":
        await query.edit_message_text(
            "🏠 2 Bedroom\n\n"
            "የ2 Bedroom ዝርዝር መረጃ እዚህ ይገባል።",
            reply_markup=bedroom_menu()
        )

    elif query.data == "three":
        await query.edit_message_text(
            "🏠 3 Bedroom\n\n"
            "የ3 Bedroom ዝርዝር መረጃ እዚህ ይገባል።",
            reply_markup=bedroom_menu()
        )

    elif query.data == "size":
        await query.edit_message_text(
            "📐 ስፋት\n\n"
            "የአፓርታማዎቹ ስፋት እዚህ ይገባል።",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 ተመለስ", callback_data="apartment")],
                [InlineKeyboardButton("🏠 Main Menu", callback_data="home")],
            ])
        )

    elif query.data == "price":
        await query.edit_message_text(
            "💰 ዋጋ\n\n"
            "የአፓርታማው ዋጋ በአይነትና በስፋት ይለያያል።",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Main Menu", callback_data="home")]
            ])
        )

    elif query.data == "location":
        await query.edit_message_text(
            "📍 አድራሻ\n\n"
            "ለቡ መብራት።",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Main Menu", callback_data="home")]
            ])
        )

    elif query.data == "contact":
        await query.edit_message_text(
            "📞 አግኙን\n\n"
            "ስልክ፦ 0969170039\n"
            "Telegram፦ @Ab2169",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Main Menu", callback_data="home")]
            ])
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
