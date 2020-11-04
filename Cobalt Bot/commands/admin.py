import  discord
from discord.ext import commands
import time

class adminkomut(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def yenile(self, mesaj, value: str):
        dizin = "commands."


        try:
            if(mesaj,author,guild_permission, administrator):
                self.bot.unload_extension(dizin + value)
                self.bot.load_extension(dizin + value)
                await mesaj.send(value + "Dosyası yenilendi !")
            else:
                await  mesaj.send("Bunu Değiştemezsin!!!")
        except ImportError as e:
            print(e)

    @commands.command(aliases= ["clear"])
    async def temizle(self, mesaj, sayi : int):
        min = 0
        max = 100

        if(mesaj.author,guild_permissions,administrator):
            if(sayi >min and sayi <= max):
                kanal = mesaj.channel
                message = await  kanal.history(limit=sayi).flatten()
                mesaj2 = await mesaj.send("{ } adet mesaj buldum...".format(sayi))
                time.sleep(1)
                await mesaj2.send("{ } adet mesaj buldum...".format(sayi))
                time.sleep(0.5)
                await  kanal.delete_messages(message)
                await mesaj2.edit(content = "while_check_mark: {} adet mesaj silindi...".format(sayi))
                time.sleep(0.5)
                message = await kanal.history(limit=1).flatten()
                await kanal.delete_messages(message)
            else:
                await mesaj.send(":x: En fazla { } mesaj silebilirim".format(max))
        else:
            await mesaj.send(":x: Bu komutu kullanamazsın :x:")

    @commands.command()
    async def rol(self, mesaj,member:discord.Member):
        pass
        def setup(bot):
            bot.add_cog(adminkomut(bot))