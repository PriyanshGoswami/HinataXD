import requests
import config
import random
from Nandha import Nandha, UB
from pyrogram import filters
from pyrogram import enums


@Nandha.on_message(filters.user(config.OWNER_ID) & filters.command("boobs",config.CMDS))
async def boobs(_, message):
    file_id = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    url = "http://media.oboobs.ru/{}"
    await message.reply_photo(url.format(file_id))



@Nandha.on_message(filters.user(config.OWNER_ID) & filters.command("porn",config.CMDS))
async def porn(_, message):
      pron_channel_id = -1001166649999
      chat_id = message.chat.id
      porn_video_ids = []
      async for message in UB.search_messages(pron_channel_id, filter=enums.MessagesFilter.VIDEO, limit=100):
            porn_video_ids.append(message.id)
      random_pron_video = random.choice(porn_video_ids)
      await Nandha.copy_message(
         chat_id,
         pron_channel_id,
         random_pron_video,
         caption=None,
         reply_to_message_id=message.id)
     
