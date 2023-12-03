import time
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
from config import *


class Sender:
    def __init__(self):
        self.file = 'output/images.txt'

    def send_webhook(self, img_url):
        webhook = DiscordWebhook(url=discordWebhook)
        embed = DiscordEmbed()
        embed.set_title(embedTitle)
        embed.set_image(url=img_url)
        embed.set_footer(text=embedFooter)
        embed.set_color(hex(embedColor)[2:])
        webhook.add_embed(embed)
        response = webhook.execute()
        if response.status_code == 200:
            print("\033[92mSuccessfully sent webhook.\033[0m")

    def get_img(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
        return random.choice(lines).strip()

    def run(self):
        while True:
            img_url = self.get_img()
            self.send_webhook(img_url)
            time.sleep(10)
