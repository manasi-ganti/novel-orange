import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


#client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
	#guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
	guild = discord.utils.get(bot.guilds, name=GUILD)
	
	print("We have logged in as {0.user}".format(bot))
	print("{0.user}  is connected to the following guild:\n".format(bot))
	print("{0.name} (id: {0.id})".format(guild))

	members = '\n - '.join([member.name for member in guild.members])
	print("Guild Members:\n - {0}".format(members))

#@bot.event
#async def on_message(message):
#	username = str(message.author).split("#")[0]
#	channel = str(message.channel.name)
#	user_message = str(message.content)

#	print(f'Message {user_message} by {username} on {channel}')
#	print(user_message)
#	if message.author == bot.user:
#		return
	#if message.content == '!hello':
	#	await message.channel.send(f'Hello {username}!')

@bot.command(name='hello')
async def say_hi(ctx):
	username = str(ctx.author).split("#")[0]
	print("hi")
	print(ctx)
	await ctx.channel.send(f'Hello {username}!')

@bot.command(name='ping')
async def say_hi(ctx):
	await ctx.channel.send(f'pong')

@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to my Discord server!'
	)


bot.run(TOKEN)