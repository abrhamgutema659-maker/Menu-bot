import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get("PORT", "10000"))
WEBHOOK_URL = os.environ["WEBHOOK_URL"]


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏢 ስለ አፓርታማ", callback_data="apartment")],
        [InlineKeyboardButton("💰 ዋጋ", callback_data="price")],
        [InlineKeyboardButton("📍 አድራሻ", callback_data="location")],
        [InlineKeyboardButton("📞 አግኙን", callback_data="contact")],
    ])


def apartment_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏢 የአፓርታማ አይነቶች", callback_data="types")],
        [InlineKeyboardButton("📐 መጠን", callback_data="size")],
        [InlineKeyboardButton("⬅️ Main Menu", callback_data="home")],
    ])


def types_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1 Bedroom", callback_data="one")],
        [InlineKeyboardButton("2 Bedroom", callback_data="two")],
        [InlineKeyboardButton("3 Bedroom", callback_data="three")],
        [InlineKeyboardButton("⬅️ ተመለስ", callback_data="apartment")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 እንኳን ወደ አፓርታማችን በደህና መጡ!\n\n"
        "ከታች ያለውን ምናሌ ይምረጡ።",
        reply_markup=main_menu()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "home":
        await query.edit_message_text(
            "🏠 Main Menu",
            reply_markup=main_menu()
        )

    elif query.data == "apartment":
        await query.edit_message_text(
            "🏢 ስለ አፓርታማው ምን ማወቅ ይፈልጋሉ?",
            reply_markup=apartment_menu()
        )

    elif query.data == "types":
        await query.edit_message_text(
            "🏢 የአፓርታማ አይነት ይምረጡ።",
            reply_markup=types_menu()
        )

    elif query.data == "one":
        await query.edit_message_text(
            "🏠 1 Bedroom Apartment\n\n"
            "ስለዚህ አይነት አፓርታማ ተጨማሪ መረጃ በቅርቡ ይጨመራል።",
            reply_markup=types_menu()
        )

    elif query.data == "two":
        await query.edit_message_text(
            "🏠 2 Bedroom Apartment\n\n"
            "ስለዚህ አይነት አፓርታማ ተጨማሪ መረጃ በቅርቡ ይጨመራል።",
            reply_markup=types_menu()
        )

    elif query.data == "three":
        await query.edit_message_text(
            "🏠 3 Bedroom Apartment\n\n"
            "ስለዚህ አይነት አፓርታማ ተጨማሪ መረጃ በቅርቡ ይጨመራል።",
            reply_markup=types_menu()
        )

    elif query.data == "size":
        await query.edit_message_text(
            "📐 የአፓርታማው መጠን\n\n"
            "የተለያዩ የካሬ ሜትር አማራጮች አሉ።",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ ተመለስ", callback_data="apartment")],
                [InlineKeyboardButton("🏠 Main Menu", callback_data="home")]
            ])
        )

    elif query.data == "price":
        await query.edit_message_text(
            "💰 ዋጋ\n\n"
            "ስለ ዋጋ ለማወቅ እባክዎ ያግኙን።",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📞 አግኙን", callback_data="contact")],
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
            "📱 0969170039\n"
            "💬 Telegram: @Ab2169",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Main Menu", callback_data="home")]
            ])
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot is running with webhook...")

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="telegram",
        webhook_url=WEBHOOK_URL
    )


if __name__ == "__main__":
    main()
