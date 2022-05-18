from discord.ext import commands
TOKEN = "FIND YOUR TOKEN IN THE BOT TAB IN DISCORD DEVELOPER PORTAL"

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix="!")

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

bot.run(TOKEN)
