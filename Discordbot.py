import discord
from discord.ext import tasks
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TickersImageSender:
    def __init__(self, dashboard_url, channel_id, bot_token):
        self.dashboard_url = dashboard_url
        self.channel_ids = channel_id
        self.bot_token = bot_token
        self.driver = None

    def open_dashboard(self):
        try:
            # Set up Chrome options to run in headless mode
            # chrome_options = Options()
            # chrome_options.add_argument("--headless")
            # chrome_options.add_argument("--disable-gpu")

            # Initialize WebDriver
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(self.dashboard_url)

        except Exception as e:
            print(f"Error capturing image: {e}")
        # finally:
        #      # To Quit WebDriver
        #     if self.driver:
        #         self.driver.quit()

    def change_ticker_to(self, option_text):
        try:
            # Find the dropdown element
            dropdown = self.driver.find_element(By.XPATH, '//*[@id="ticker-dropdown"]/div')
            # Click on the dropdown to open it
            ActionChains(self.driver).move_to_element(dropdown).click().perform()
            # Find the option within the dropdown
            option = dropdown.find_element(By.XPATH, f'//*[text()="{option_text.upper()}"]')
            # Click on the option to select it
            ActionChains(self.driver).move_to_element(option).click().perform()
        except Exception as e:
            print(f"Error changing dropdown option: {e}")

    def get_channel(self, channel_name):
        try:
            return self.client.get_channel(self.channel_ids[channel_name])
        except Exception as e:
            print(f"Error getting channel {channel_name}: {e}")
            return None

    async def send_img(self, channel_name='spx'):
        channel = self.get_channel(channel_name)
        if channel:
            try:
                self.driver.save_screenshot('screenshot.png')
                with open('screenshot.png', 'rb') as f:
                    await channel.send(file=discord.File(f))
                    print('Screenshot sent')
            except Exception as e:
                print(f"Error sending screenshot to {channel_name}: {e}")
        else:
            print(f'Invalid channel {channel_name} or not text-based.')


    @tasks.loop(minutes=2)
    async def img_sender(self):
        await self.send_img()
        for ticker in channel_ids:
            # Change dropdown option
            self.change_ticker_to(ticker)
            await asyncio.sleep(5)
            await self.send_img(ticker)

    def run(self):
        self.open_dashboard()
        intents = discord.Intents.default()
        intents.guilds = True
        self.client = discord.Client(intents=intents)

        @self.client.event
        async def on_ready():
            print('Bot is ready')
            await asyncio.sleep(10)
            self.img_sender.start()

        self.client.run(self.bot_token)

if __name__ == '__main__':
    dashboard_url = 'https://gav-exposure.onrender.com/'  # Replace with your dashboard URL
    channel_ids = {  'spx' : 1221744071463272489,
                    'tsla': 1221744121539067964,
                    'nvda': 1221744168968392704,
                    'qqq' : 1221744205345329212,
                    'spy' : 1221744246143320074
                     } # Replace with your channel IDs
    bot_token = ''  # Replace with your bot token
    tickers_sender = TickersImageSender(dashboard_url, channel_ids, bot_token)
    tickers_sender.run()
