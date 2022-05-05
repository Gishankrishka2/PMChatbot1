#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os

from pyrogram import Client, filters
from presets import Presets

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

@Client.on_message(filters.private & filters.command(["start"]))
async def force_sub(bot, msg):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, msg.from_user.id)
            if user.status == "kicked out":
                await msg.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            await msg.reply_text text= 
                text="**❌ Access Denied ❌**\n🌷You Must Join My Update Channel...🌷\n♻️Join it & Try Again.♻️",
                reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒', url='https://t.me/{force_subchannel}'),
                 InlineKeyboardButton('◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』', url='https://t.me/{OWNER}')
                 ]]
                )
            )    
            return 
    
@Client.on_message(filters.command(commands=['start'])) 
  async def StartMsg(_,m): 
  await client.send_sticker(m.chat.id, sticker='CAADAgADaRsAAsOUWUpHrmf5mZp3EgI')
    
@Client.on_message(filters.private & filters.command(['start', 'help']))
async def help_me(bot, message):
    if message.from_user.id == Config.ADMIN:
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    await bot.send_message(
        chat_id=message.chat.id,
        text=Presets.WELCOME_TEXT.format(info.first_name)
    )
    await bot.send_message(
        chat_id=Config.ADMIN,
        text=Presets.USER_DETAILS.format(
            info.first_name,
            info.last_name,
            info.id, info.username,
            info.is_scam,
            info.is_restricted,
            info.status,
            info.dc_id
        )
    )
