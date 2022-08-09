from telethon import TelegramClient, utils, events
import logging, config, random

logging.basicConfig(level=config.logging_level,format=config.logging_format)
log = logging.getLogger(__name__)

bot = TelegramClient('coinBot', config.api_id, config.api_hash).start(bot_token=config.bot_token)

choices = {
    "en":["It's tail!","It's head!"],
    "zh-hans":["硬币是反面喵！","硬币是正面喵！"],
    "zh-hant":["硬幣是反面喵！","硬幣是正面喵！"],
}

@bot.on(events.NewMessage(pattern='/tosscoin'))
async def checkpriv(event):
    user_lang = event.sender.lang_code
    if event.sender.lang_code == None: user_lang = "en"
    lang_choices = choices[user_lang] if user_lang in choices else choices["en"]
    await event.respond(random.choice(lang_choices))
    log.info("User {} (lang \"{}\") executed /tosscoin".format(event.sender.id,event.sender.lang_code))
    raise events.StopPropagation

log.info("Finished. Starting bot...")
bot.run_until_disconnected()
