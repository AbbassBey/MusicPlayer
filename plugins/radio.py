from pyrogram import Client, filters
from pyrogram.types import Message
from utils.vc import mp, RADIO
from config import Config
STREAM_URL=Config.STREAM_URL
ADMINS=Config.ADMINS

@Client.on_message(filters.command("radio") & filters.user(ADMINS))
async def radio(client, message: Message):
    if 1 in RADIO:
        await message.reply_text("Lütfen mevcut Radyo Akışını durdurun /stopradio")
        return
    await mp.start_radio()
    await message.reply_text(f"Başlatılan Radyo: <code>{STREAM_URL}</code>")

@Client.on_message(filters.command('stopradio') & filters.user(ADMINS))
async def stop(_, message: Message):
    if 0 in RADIO:
        await message.reply_text("Lütfen Önce Radyoyu başlatın /radio")
        return
    await mp.stop_radio()
    await message.reply_text("Radyo yayını sona erdi.")
