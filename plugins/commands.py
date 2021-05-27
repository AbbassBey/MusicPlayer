from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "Merhaba, [{}](tg://user?id={})\n\n Ben gruplarda ve kanallarda müzik ve radio açabilirim 24*7"
HELP = """**Komutlar**:

**/play**  Sesli yanıtla play/queue veya oynatma listesini göster
**/player**  Geçerli parçanın geçerli çalma süresini göster
**/help** Komutlar için yardımı göster
**/playlist** Çalma listesini gösterir.

**Admin komutları**:
**/skip** [n] ...  sıradaki şarkıya geçer n >= 2
**/join**  Mevcut grubun sesli sohbetine katılın
**/leave**  Mevcut sesli sohbetten ayrıl
**/vc**  Hangi VC'nin katıldığını kontrol edin
**/stop**  Müziği durdurur
**/radio** Radioyu başlatır
**/stopradio** Radio durdurur
**/replay**  Baştan başlatır şarkıyı
**/clean** Kullanılmayan RAW PCM dosyalarını kaldırın
**/pause** Oynatmayı duraklat
**/resume** Oynamaya devam et
**/mute**  VC kullanıcı botunu sessize alın
**/unmute**  VC kullanıcı robotunun sesini açın
**/restart** Botu yeniden başlatır
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('Güncelleme kanalı', url='https://t.me/zevzekcalardestek'),
        InlineKeyboardButton('Ses botu hesabı', url='https://t.me/zevzekcalarasistan'),
        InlineKeyboardButton('Güncelleme grubu', url='https://t.me/zevzekcalardestekgrup'),
    ],
    [
        InlineKeyboardButton('Sahip', url='https://t.me/abbassbey'),
        InlineKeyboardButton('Sahip Biografisi', url='https://t.me/biolinki'),
        InlineKeyboardButton('Sahip Kanalları', url='https://t.me/kanaltoplist'),
    ],
    [
        InlineKeyboardButton('Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
