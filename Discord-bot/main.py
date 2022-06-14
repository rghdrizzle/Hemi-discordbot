from Keep_alive import keep_alive
import os
import praw
import random
import youtube_dl
import discord
import random 
from discord import utils
from discord import Embed
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='%')
bot.remove_command("help")
@bot.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title="help",description = "use %help <category> to help you know more about the commands we have :)")
  em.add_field(name="Fun",value ="meme,hello,gaming,IQ,psbattle,tictactoe")
  await ctx.send(embed=em)

@help.command()
async def meme(ctx):
  em = discord.Embed(title="Meme", description="Shows you memes😂")
  em.add_field(name="**syntax**", value="%meme")
  await ctx.send(embed=em)
@help.command()
async def gaming(ctx):
  em=discord.Embed(title="gaming", description="Shows you posts (memes)related to gaming")
  em.add_field(name="**syntax**",value="%gaming")
  await ctx.send(embed=em)
@help.command()
async def hello(ctx):
  em=discord.Embed(title="Hello", description="says hello back")
  em.add_field(name="**syntax**",value="%hello")
  await ctx.send(embed=em)
@help.command()
async def IQ(ctx):
  em=discord.Embed(title="IQ", description="Tells you how much IQ u have (its jus for fun hehe")
  em.add_field(name="**syntax**",value="%IQ")
  await ctx.send(embed=em)
@help.command()
async def psbattle(ctx):
  em=discord.Embed(title="PsBattle", description="Shows you epic Photoshop pics")
  em.add_field(name="**syntax**",value="%psbattle")
  await ctx.send(embed=em)
@help.command()
async def tictactoe(ctx):
  em = discord.Embed(title="Tictactoe", description="play tic tac toe with the homies")
  em.add_field(name="**syntax**", value="%tictactoe")
  await ctx.send(embed=em)


@bot.command(name='hello', help='says hello')
async def hello(ctx):
	hello_dev = [
	    'hello',
	    'how you doin?',
	    'yes?',
	    'heyoo','H-E-L-L-O!!!',
	    ('Cool'),
	]

	response = random.choice(hello_dev)
	await ctx.send(response)


@bot.command(name='coinflip', help='tosses a coin')
async def coinflip(ctx):
	coin = ['heads', 'tails', 'tails', 'tails', 'heads', 'heads']

	response = random.choice(coin)
	await ctx.send(response)


@bot.command(name='IQ', help='Tells you how much IQ you have :)')
async def iq(ctx):
	i_q = [
	    'YOU HAVE 100iq',
	    'GREAT YOU ARE INDEED SMARTER THAN ME , HERE IS HOW MUCH IQ U HAVE :200iq',
	    'LMAO 10iq', 'NOT BAD :50iq',
	    'DAYMMMMMMNNNNNNN BRUV , YOU ARE AN ULTRA GENIUS :10000000iq', '20iq',
	    'OH GOD :400iq', 'GOOD :150iq', 'HAHAHAH 0.1iq',
	    'IM SRY YOU LITRALLY HAVE NO IQ'
	]

	response = random.choice(i_q)
	await ctx.send(response)

reddit = praw.Reddit(
    client_id='JSxjXI67oBQo6Q',
    client_secret="N2i94qX_P8P8iwDtPXb-USP9uz3X9Q",
    username="RGHdrizzle",
    password="2510897aZrgh",
    user_agent="hemi")
subreddit = reddit.subreddit('memes')


@bot.command(name="meme", help="shows you MEMES")
async def meme(ctx, subreddit="memes"):
	subreddit = reddit.subreddit(subreddit)
	all_sub = []
	top = subreddit.hot(limit=100)
	for submission in top:
		all_sub.append(submission)

	random_sub = random.choice(all_sub)
	name = random_sub.title
	url = random_sub.url

	em = discord.Embed(title=name)

	em.set_image(url=url)
	await ctx.send(embed=em)

@bot.command(name="psbattle",help='shows you epic photoshop')
async def ps(ctx,subreddit='photoshopbattles'):
  subreddit = reddit.subreddit(subreddit)
  all_sub = []
  top = subreddit.top(limit=50)
  for submission in top:
    all_sub.append(submission)
    
  random_sub = random.choice(all_sub)
  name = random_sub.title
  url = random_sub.url
  
  em = discord.Embed(title=name)
  em.set_image(url=url)
  await ctx.send(embed=em)
@bot.command(name="gaming",help="posts related to gaming")
async def gaming(ctx,subreddit='gaming'):
  subreddit = reddit.subreddit(subreddit)
  all_sub=[]
  top = subreddit.hot(limit=50)
  for submission in top:
    all_sub.append(submission)
  random_sub = random.choice(all_sub)
  name = random_sub.title
  url = random_sub.url
  
  em = discord.Embed(title=name)
  em.set_image(url=url)
  await ctx.send(embed=em)

@bot.command(name="cars",help="posts related to cars")
async def cars(ctx,subreddit='weirdWheels'):
  subreddit = reddit.subreddit(subreddit)
  all_sub=[]
  top = subreddit.hot(limit=50)
  for submission in top:
    all_sub.append(submission)
  random_sub = random.choice(all_sub)
  name = random_sub.title
  url = random_sub.url
  
  em = discord.Embed(title=name)
  em.set_image(url=url)
  await ctx.send(embed=em)
  
  
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command(name="tictactoe",help="Play tictactoe with your friends")
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

  

@bot.event
async def on_ready():
	activity = discord.Game(name="Bot Paradise", type=3)
	await bot.change_presence(status=discord.Status.idle, activity=activity)
	print("Bot is ready!")


keep_alive()
bot.run(TOKEN)
