import discord
from discord.ext import commands
import platform
token = "Pls write token"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix= "exe!", pm_help = "None " , description="TheBeatles.exe tarafından yazılmıştır.")
        self.bot_version = "1.0.0"
        self.bot_name = "Cobalt"
        self.author = "TheBeatles.exe"
        self.icon= "cobalt.png"
        self.getDevicesOs = platform.system()

        self.load_extension("commands.info")

    async def on_ready(self):
        print("Bot açılıyor...")
        print("Bot : {}".format(self.user.name))
        print("Bot ID : {}".format(self.user.id))
        #print(str(len(set(self.servers()))) + "tane sunucuda aktif")
        print(str(len(set(self.get_all_members()))) + " tane kullanıcıya erişiyor")

    async def on_command_error(self, context, exception):
        if isinstance(exception , discord.ext.commands.errors.CommandNotFound):
            await context.send("Yazdığınız isme uygun bir komut bulamadık! Lütfen komutları doğru ve eksiksiz girdiğinizden emin olun. Tüm komutları görmek için {0.prefix}yardım yardım yazabilirsiniz.".format(context))

bot = Bot()
bot.run(token)