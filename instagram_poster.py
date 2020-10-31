from instabot import Bot
from tokens import getCreds

bot = Bot()


def instagram_post(image_path, video_title, video_link):
    creds = getCreds()
    bot.login(username=creds['username'],
              password=creds['password'])
    caption_text = f'{video_title} {video_link}'
    bot.upload_photo(image_path, caption=caption_text)
