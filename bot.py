import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import yt_dlp

# Token depuis les variables d'environnement (sécurité)
TOKEN = os.getenv("8516224341:AAFqkq4-E9GidEU4azEEfiwab1XZjNm2JDA")

DOWNLOAD_PATH = "downloads"
os.makedirs(DOWNLOAD_PATH, exist_ok=True)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = update.message.text

    await update.message.reply_text("d'environnementéléchargement en cours...")

    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "outtmpl": f"{DOWNLOAD_PATH}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "quiet": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, "rb") as video:
            await update.message.reply_video(video)

        os.remove(filename)

    except Exception as e:
        await update.message.reply_text("Erreur : " + str(e))


def main():

    if not TOKEN:
        print("BOT_TOKEN manquant")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("Bot en ligne...")
    app.run_polling()


if __name__ == "__main__":
    main()
