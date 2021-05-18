import discord
from discord import client
from discord import member
from discord import user
from discord import message 
from discord.ext import commands


bot = commands.Bot(command_prefix="+",case_insensitive=True)


class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)
bot.help_command = NewHelpName()



@bot.command()
async def hi(ctx):
    await ctx.send(f"hello {ctx.message.author}")

@bot.command(name='server')
async def fetchServerInfo(context):
	guild = context.guild

@bot.command(
  help="allows you to type something u want" 
)  
async def say(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)


@bot.event
async def on_ready() :
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Listening to +help"))
    print("I am online")

@bot.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@bot.command()
async def avatar(ctx, member:discord.Member):
 await ctx.send(member.avatar_url)

@bot.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@bot.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

@bot.command(
	help="Uses come crazy logic to determine if noob is actually the correct value or not.",
	brief="CALLS A PRo."
)
async def PRO(ctx):
	await ctx.channel.send("UR PRO XD")


#NVM IF U WANT TO PUT IN CODE

@bot.command(
	help="Looks like you need some help.",
	brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg
	await ctx.channel.send(response)


intents = discord.Intents.default()
client = discord.Client(intents=intents)


#KICK BAN CMD

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)


@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)


@bot.command(name='dm',pass_context=True)
async def dm(ctx, *argument):
    #creating invite link
    invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
    #dming it to the person
    await ctx.author.send(invitelink)



# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="DEMON OP", url="http://www.twitch.tv/accountname"))
    print('My Ready is Body')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)

        
        #SERVER INFO
 @bot.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="owner", value=owner, inline=True)
  embed.add_field(name="server id", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)     
  
  #GIVES ROLE TO ANTHORE PERSON
@bot.command(pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

    #DMS SERVER INVITE
@bot.event  
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

    #MATHS CALCULATION CMD
@bot.command() 
async def add(ctx, *nums):
    operation = " + ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@bot.command() 
async def sub(ctx, *nums): 
    operation = " - ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@bot.command() 
async def multiply(ctx, *nums): 
    operation = " * ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@bot.command() 
async def divide(ctx, *nums): 
    operation = " / ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')


bot.run('TOKEN')    
