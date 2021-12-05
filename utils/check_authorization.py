from data import config

def auth(func):
    async def wrapper(message):
        availible = config.ACCESS_GRANTED_TO
        if not (message['from']['username'] in availible):
            return await message.reply("Access Denied. Please speak with an organization that gave you the link to this bot.", reply=False)
        return await func(message)
    return wrapper
