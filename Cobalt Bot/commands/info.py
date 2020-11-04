import discord
from discord.ext import  commands

class infocommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.bot_version = bot.bot_version
        self.bot_name = bot.bot_name
        self.author = bot.author
        self.icon = bot.icon
        self.getDevicesOs = bot.getDevicesOs

        @commands.command()
        async def bilgi(self, mesaj):
            embed = discord.Embed(title="\>", color=0xd00005)
            embed.set_author(name="Cobalt - Bilgilendirme")
            embed.add_field(name="Kütüphane", value="discord.py", inline=True)
            embed.add_field(name="Version", value=self.bot_version, inline=True)
            embed.add_field(name="Yapımcı", value=self.author, inline=True)
            embed.add_field(name="Youtube Kanalım",
                            value="[Tıkla](https://www.youtube.com/channel/UC17PmJKi9wiyLWCuWGIHvMw?view_as=subscriber)",
                            inline=True)
            embed.add_field(name="Discord Davet Linki", value="[Tıkla](https://discord.gg/H6s6nU)", inline=True)
            embed.add_field(name="Emeği Geçenler", value="TheBeatles.exe#9147", inline=True)
            embed.set_footer(icon=self.icon_, text="Cobalt - Bu bir Discord Botu ")
            await  mesaj.send(embed=embed)


def setup(bot):
    bot.add_cog(infocommands(bot))