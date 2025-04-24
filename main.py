import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intent  = discord.Intents.default()
intent.message_content = True
intent.members = True

bot = commands.Bot(command_prefix="!", intents=intent)

secret_role = "Knight"

@bot.event
async def on_ready():
    print(f"We are ready to go in", bot.user.name)

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} Please do not use that word!")

    await bot.process_commands(message) #

@bot.command()
async def dm(ctx, *, message):
    await ctx.author.send(f" You said {message}")

@bot.command()
async def reply(ctx):
    await ctx.reply("Reply to your message.")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.name} has been assigned the {secret_role} role.")
    else:
        await ctx.send(f"Role {secret_role} does not exist.")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.name} has been removed from the {secret_role} role.")
    else:
        await ctx.send(f"Role does not exist")

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="Poll", description=question, color=discord.Color.blue())
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send(f"Hello {ctx.author.name}, here is your Valaryian Steel Sword!")

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"You do not have the permission to do that.")

bot.run(token,log_handler=handler,log_level=logging.DEBUG)