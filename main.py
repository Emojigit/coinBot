from telethon import TelegramClient, functions, types, events, utils
from telethon.errors import *
import logging, config, random

logging.basicConfig(level=config.logging_level,format=config.logging_format)
log = logging.getLogger(__name__)

bot = TelegramClient('coinBot', config.api_id, config.api_hash).start(bot_token=config.bot_token)

choices = ["硬币是反面喵！","硬币是正面喵！"]

@bot.on(events.NewMessage(pattern='/tosscoin'))
async def checkpriv(event):
    await event.respond(random.choice(choices))
    log.info("User {} executed /tosscoin".format(event.sender.id))
    raise events.StopPropagation

log.info("Finished. Starting bot...")
bot.run_until_disconnected()
