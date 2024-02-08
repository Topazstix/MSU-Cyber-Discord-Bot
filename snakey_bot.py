import discord
import dotenv
import os

dotenv.load_dotenv()

class SnakeyBot(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')
        
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

intents = discord.Intents.default()
intents.message_content = True
client = SnakeyBot(intents=intents)
client.run(os.getenv('CLIENT_TOKEN'))