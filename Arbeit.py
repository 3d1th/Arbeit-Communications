
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!!!', intents=intents)

TOKEN = 'sexsexsexsexsexsexsexsexsexsexsex'  # 이곳에 봇 토큰을 입력해주세요.


@bot.event
async def on_ready():
    print(f'봇이 다음과 같이 로그인 했습니다: {bot.user.name} ({bot.user.id})')
    invite_link = discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions(permissions=8))
    print(f'봇 초대 코드: {invite_link}')
    game = discord.Game(name='Hogwarts Legacy')
    await bot.change_presence(activity=game)


@bot.command()
@commands.has_permissions(administrator=True)
async def 디엠공지(ctx, *, content):
    if not ctx.guild:
        await ctx.send("ㄴㄱㅁ.")
        return

    log_user_id = 1087798717781917867  # 로그를 받을 유저의 ID
    log_user = bot.get_user(log_user_id)

    members = [m for m in ctx.guild.members if m.status != discord.Status.offline]  # Exclude offline members
    member_count = len(members)
    sent_count = 0
    failed_members = []

    for member in members:
        if member.bot or member.id == log_user_id:
            continue

        try:

            await member.send(content)
            sent_count += 1


            embed = discord.Embed(title=f"디엠전송 성공: {member.name}", color=0x00FF00)
            embed.description = f"남은유저수: {member_count - sent_count - 1}\n디엠을 보낸 유저수: {sent_count}\n디엠을 보내지못한 유저 수: {len(failed_members)}"
            await log_user.send(embed=embed)

        except Exception as e:

            failed_members.append(member)
            embed = discord.Embed(title=f"디엠전송 실패: {member.name}", color=0xFF0000)
            embed.description = f"남은유저수: {member_count - sent_count - 1}\n디엠을 보낸 유저수: {sent_count}\n디엠을 보내지못한 유저 수: {len(failed_members)}"
            await log_user.send(embed=embed)

    if failed_members:
        failed_names = ", ".join([member.name for member in failed_members])
        await log_user.send(f"디엠공지 실패 인one: {failed_names}")
    else:
        await log_user.send("디엠공지완료.")


bot.run(TOKEN)