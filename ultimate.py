import os
import platform
import discord
import asyncio
import colorama
from colorama import Fore, Style
from discord.ext import commands
import aioconsole

colorama.init(autoreset=True)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", case_insensitive=True, self_bot=True, intents=intents)

os_type = platform.system()
if os_type == "Windows":
    os.system("cls")
else:
    os.system("clear")

print(f"""{Fore.RED}
 █    ██  ██▓  ▄▄▄█████▓ ██▓ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▓█████ 
 ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ 
▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   
▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ 
▒▒█████▓ ░██████▒▒██▒ ░ ░██░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ░ ░  ░
 ░░░ ░ ░   ░ ░   ░       ▒ ░░      ░     ░   ▒    ░         ░   
   ░         ░  ░        ░         ░         ░  ░           ░  ░
                                                            {Fore.MAGENTA}Developed by: ultimate{Style.RESET_ALL}
        """)

async def get_input(prompt):
    return await aioconsole.ainput(prompt)

async def show_menu():
    menu = f"""
{Fore.CYAN}
What would you like to clone? Enter the corresponding number:
1. Roles
2. Channels
3. Emojis
4. Guild Icon
5. Everything
{Style.RESET_ALL}
"""
    print(menu)
    choice = await get_input(f"{Fore.YELLOW}Enter your choice (1-5): {Style.RESET_ALL}")
    return choice

def print_add(message):
    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.RED}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.RED}[WARNING]{Style.RESET_ALL} {message}')

def print_error(message):
    print(f'{Fore.RED}[ERROR]{Style.RESET_ALL} {message}')

class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
        for role in guild_to.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
                    print_delete(f"Deleted Role: {role.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Role: {role.name}")
            except discord.HTTPException:
                print_error(f"Unable to Delete Role: {role.name}")

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = []
        for role in guild_from.roles:
            if role.name != "@everyone":
                roles.append(role)
        roles = roles[::-1]
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"Created Role {role.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Role: {role.name}")
            except discord.HTTPException:
                print_error(f"Unable to Create Role: {role.name}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Deleted Channel: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Channel: {channel.name}")

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        category_map = {}
        for category in guild_from.categories:
            try:
                overwrites_to = {}
                for key, value in category.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    if role is not None:
                        overwrites_to[role] = value
                new_category = await guild_to.create_category(
                    name=category.name,
                    overwrites=overwrites_to)
                await new_category.edit(position=category.position)
                category_map[category.id] = new_category
                print_add(f"Created Category: {category.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Category: {category.name}")
            except discord.HTTPException:
                print_error(f"Unable To Create Category: {category.name}")
        return category_map

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild, category_map):
        for channel in guild_from.channels:
            try:
                if isinstance(channel, discord.TextChannel):
                    new_channel = await guild_to.create_text_channel(
                        name=channel.name,
                        topic=channel.topic,
                        nsfw=channel.nsfw,
                        position=channel.position,
                        slowmode_delay=channel.slowmode_delay,
                        overwrites=channel.overwrites,
                        category=category_map.get(channel.category_id)
                    )
                elif isinstance(channel, discord.VoiceChannel):
                    new_channel = await guild_to.create_voice_channel(
                        name=channel.name,
                        position=channel.position,
                        user_limit=channel.user_limit,
                        bitrate=channel.bitrate,
                        overwrites=channel.overwrites,
                        category=category_map.get(channel.category_id)
                    )
                print_add(f"Created Channel: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable To Create Channel: {channel.name}")

    @staticmethod
    async def emojis_delete(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print_delete(f"Deleted Emoji: {emoji.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Emoji{emoji.name}")
            except discord.HTTPException:
                print_error(f"Error While Deleting Emoji {emoji.name}")

    @staticmethod
    async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
        for emoji in guild_from.emojis:
            try:
                emoji_image = await emoji.url.read()
                await guild_to.create_custom_emoji(
                    name=emoji.name,
                    image=emoji_image)
                print_add(f"Created Emoji {emoji.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Emoji {emoji.name} ")
            except discord.HTTPException:
                print_error(f"Error While Creating Emoji {emoji.name}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            try:
                icon_image = await guild_from.icon_url.read()
            except discord.errors.DiscordException:
                print_error(f"Can't read icon image from {guild_from.name}")
                icon_image = None
            await guild_to.edit(name=f'{guild_from.name}')
            if icon_image is not None:
                try:
                    await guild_to.edit(icon=icon_image)
                    print_add(f"Guild Icon Changed: {guild_to.name}")
                except:
                    print_error(f"Error While Changing Guild Icon: {guild_to.name}")
        except discord.Forbidden:
            print_error(f"Error While Changing Guild Icon: {guild_to.name}")

@bot.event
async def on_ready():
    print(f"Logged In as: {bot.user}")
    guild_from = bot.get_guild(int(input_guild_id))
    guild_to = bot.get_guild(int(output_guild_id))

    choice = await show_menu()
    
    if choice == '1':
        await Clone.roles_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
    elif choice == '2':
        await Clone.channels_delete(guild_to)
        category_map = await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from, category_map)
    elif choice == '3':
        await Clone.emojis_delete(guild_to)
        await Clone.emojis_create(guild_to, guild_from)
    elif choice == '4':
        await Clone.guild_edit(guild_to, guild_from)
    elif choice == '5':
        await Clone.roles_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.channels_delete(guild_to)
        category_map = await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from, category_map)
        await Clone.emojis_delete(guild_to)
        await Clone.emojis_create(guild_to, guild_from)
        await Clone.guild_edit(guild_to, guild_from)
    else:
        print_warning("Invalid choice. Please enter a number between 1 and 5.")

input_guild_id = input(f"{Fore.YELLOW}Enter The ID Of The Guild You Want To Clone: {Style.RESET_ALL}")
output_guild_id = input(f"{Fore.YELLOW}Enter The ID Of The Guild You Want To Add The Clone: {Style.RESET_ALL}")
    
token =  input(f"{Fore.YELLOW}Enter Your Token: {Style.RESET_ALL}")
bot.run(token, bot=False)

