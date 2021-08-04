# SOLARISPLAnet~ENV
# family-def=SOLARIS
# environment=Python39; discord.py
# REQUIREMENTS.TXT

import discord
from discord.ext import commands, tasks, loops

bot = commands.Bot(command_prefix = "m!")

### EVENEMENTS ###

msg_dump_channel = 872577182973718628

@bot.event
async def on_message(message: discord.Message):
    channel = bot.get_channel(msg_dump_channel)
    embed = discord.Embed(title=" ", description=message.content, color=0xFDFDFD)
    embed.set_author(name="#" + channel.name + "    ←    " + message.author.name + "#" + message.author.discriminator)
    if message.guild is None and not message.author.bot:
        await channel.send(embed=embed)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print("Le bot est en ligne")
    channel = bot.get_channel(867652127027232798)
    await channel.send("Je suis en ligne")

### COMMANDES D'ADMINISTRATION ###
  
@bot.command()
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre).flatten()
    for message in messages:
        await message.delete()
    channel = bot.get_channel(867652127027232798)
    await channel.send(f"{nombre} messages ont été supprimés")
  
@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.User, *, reason="Aucune raison n'a été fournie pour cet avertissement."):
    embed = discord.Embed(title="**Avertissement**",
                          description="Un modérateur ou administrateur a averti un membre", color=0xD9534F)
    embed.set_author(name="@System", url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://images.emojiterra.com/twitter/v13.0/512px/26a0.png")
    embed.add_field(name="Membre averti", value=user.name + "#" + str(user.discriminator))
    embed.add_field(name="Raison", value=reason, inline=False)
    embed.add_field(name="Invoker", value=ctx.author.name + "#" + str(ctx.author.discriminator), inline=False)
    embed.set_footer(text="Qui cherche trouve, retiens la lecon !")
    await ctx.send(embed=embed)
    await ctx.message.delete()
    
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, reason="Aucune raison n'a été fournie pour ce kick."):
    await ctx.guild.kick(user, reason=reason)
    embed = discord.Embed(title="**← Utilisateur expulsé**",
                          description="Un modérateur ou administrateur à mis un coup de kick")
    embed.set_author(name=ctx.author.name, url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://iconape.com/wp-content/png_logo_vector/exit-logo.png")
    embed.add_field(name="Membre expulsé", value=user.name)
    embed.add_field(name="Raison", value=reason, inline=False)
    embed.add_field(name="Invoker", value=ctx.author.name, inline=False)
    embed.set_footer(text=random.choice(list6))
    await ctx.send(embed=embed)
    await ctx.message.delete()
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été fournie pour ce ban."):
    await ctx.guild.ban(user, reason=reason)
    embed = discord.Embed(title="**← Coup de marteau**",
                          description="Un modérateur ou administrateur à tapé le marteau sur la table !",
                          color=0xff0000)
    embed.set_author(name=ctx.author.name, url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ban_logo.svg/2048px-Ban_logo.svg.png")
    embed.add_field(name="Membre banni", value=user.name)
    embed.add_field(name="Raison", value=reason, inline=False)
    embed.add_field(name="Invoker", value=ctx.author.name)
    embed.set_footer(text=random.choice(list6))
    await ctx.send(embed=embed)
    await ctx.message.delete()
    
@bot.command()
async def banlist(ctx):
    ids = []
    bans = await ctx.guild.bans()
    for i in bans:
        ids.append(str(i.user.id))
    await ctx.send("La liste des identifiants des utilisateurs bannis est la suivante :")
    await ctx.send("\n".join(ids))
    await ctx.message.delete()

    
### COMMANDE PING ###
    
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    embed = discord.Embed(title="Test de latence",
                          description="Cette commande permet d'afficher le ping actuel de Matou en ms (milliseconde(s))",
                          color=0xeed5b5)
    embed.add_field(name="Ping actuel (ms) :", value=f"{ping}ms")
    embed.set_footer(text="La valeur peut être faussée, il est recommandé de recommancer plusieurs fois le `!ping`")
    await ctx.send(embed=embed)
    await ctx.message.delete()
    
### COMMANDE DM ###

@bot.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, user: discord.User, *, message):
    message = message
    await user.send(message)
    embed = discord.Embed(title=" ", description=message, color=0x0080FF)
    embed.set_author(
        name=ctx.author.name + "#" + ctx.author.discriminator + "    →    " + user.name + "#" + user.discriminator)
    await ctx.send(embed=embed)
    await ctx.message.delete()
    
### COMMANDE SAY ###

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))
    await ctx.message.delete()

### COMMANDE BONJOUR ###

@bot.command()
async def bonjour(ctx):
    await ctx.send(ctx.author.display_name + " dit bonjour à **tout le monde**")
    await ctx.message.delete()


### END OF SCRIPT : TOKEN LOADING ###
bot.run('TOKEN HERE')
# REQUIRED TO START BOT !
