import config

from Nandha import Nandha

from Nandha.help.rulesdb import *

from Nandha.help.admin import is_admin

from pyrogram import filters


@Nandha.on_message(filters.command("setrules"))
async def setrules(_, message):
   chat_id = message.chat.id
   user_id = message.from_user.id
   reply = message.reply_to_message
   if (await is_admin(chat_id,user_id)) == False:
        return await message.reply("`Admins Only!`")
   else:
        if reply and (reply.text or reply.caption):
            RULES = reply.text or reply.caption
        elif not reply and len(message.text.split()) <2:
            return await message.reply("`reply to text message or give text to set rules!`")
        elif not reply and len(message.text.split()) >1:
             RULES = message.text.replace(message.text.split()[0], "")
        if chat_id in rules_chat():
                 update_rules(chat_id,RULES)
                 await message.reply("`Group Rules already set so I have updated the Rules Successfully!`")
        else:
                 add_rules(chat_id,RULES)
                 await message.reply("`Group Rules set Successfully!`")
             
              
             
            