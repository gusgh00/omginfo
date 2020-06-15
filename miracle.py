import discord
import asyncio
import random
from datetime import date, datetime, time, timedelta, timezone
import datetime
import time
import os
from bs4 import BeautifulSoup
import urllib
import requests
from pytz import timezone, utc
 
client = discord.Client()

access_token = os.environ["BOTTOKEN"]
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    game = discord.Game(";도움 ;크레딧 | 오늘도 미라클!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    id = message.author.id

    if message.author.bot:
        return None
    
#######################################################################################

#embed text=";도움"

    if message.content.startswith(";도움"):

        embed1 = discord.Embed(title = "안녕하세요 오마이걸 정보 봇입니다!", description = "명령어는 오마이걸 명령어와 이미지 명령어, 정보 명령어로 이루어져 있습니다.\n자세한 설명은 ;커맨드를 이용하면 나옵니다.\n즐겁게 사용해주시기 바랍니다.",color = 0xf4a6d7)
        embed1.set_thumbnail(url = "https://i.imgur.com/nM1IC56.png")
        embed1.add_field(name = "멤버 별 생일 정보", value = "`;생일`", inline = False)
        embed1.add_field(name = "앨범 수록곡과 정보", value = "`;앨범`", inline = False)
        embed1.add_field(name = "기념일 정보", value = "`;기념일`", inline = False)
        embed1.add_field(name = "오마이걸 노래 가사", value = "`;가사`", inline = False)
        embed1.add_field(name = "음원 차트", value = "`;멜론` `;지니` `;벅스`", inline = False)
        embed1.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed1)

        embed2 = discord.Embed(color = 0x9adbe8)
        embed2.set_author(name = "Image")
        embed2.add_field(name = "멤버들의 gif (랜덤)", value = "`;움짤`", inline = False)
        embed2.add_field(name = "멤버들의 사진 (랜덤)", value = "`;옴` `;쩡` `;밈` `;샤`\n`;씅` `;죠` `;윱` `;린`", inline = False)
        embed2.add_field(name = "재미있는 짤방", value = "`;타노스` `;째릿` `;승하` `;닥쳐`\n`;커플이야` `;털썩` `;헤드셋` `;딱밤`\n`;훌라훌라` `;짜증나` `;짜잔`", inline = False)
        embed2.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed2)

        embed3 = discord.Embed(color = 0xeee29f)
        embed3.set_author(name = "Information")
        embed3.add_field(name = "제작자 정보", value = "`;크레딧`", inline = False)
        embed3.add_field(name = "커맨드 정보", value = "`;커맨드`", inline = False)
        embed3.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed3)

    if message.content.startswith(";크레딧"):
        await message.channel.send("제작자 개인링크\nhttps://open.kakao.com/me/oguomg\n")
        await message.channel.send("봇 서버에 추가하기\nhttps://discord.com/api/oauth2/authorize?client_id=656111566550466579&permissions=2081421553&scope=bot")

#######################################################################################

#command info

    if message.content.startswith(";커맨드"):
        cmd = message.content.split(" ")[1]
        cmdlist = ['생일','앨범','기념일','가사','멜론','지니','벅스','움짤','옴','쩡','밈','샤','씅','죠','윱','린','커맨드']
        ccolor = [0xf4a6d7,0x9adbe8,0xeee29f]
        cmdcount = 17
        embedArray = []

        #1
        embed = discord.Embed(title=";생일", description="뒤에 멤버들의 이름을 넣어보아요~! `;생일` `;birth` `;b`\n`예);생일 효정`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #2
        embed = discord.Embed(title=";앨범", description="뒤에 앨범 이름을 넣어보아요~! `;앨범` `;album` `;a`\n`예);앨범 다섯번째계절, ;앨범 정규1집`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #3
        embed = discord.Embed(title=";기념일", description="뒤에 특별한 날을 넣어보아요~! `;기념일` `;date` `;d`\n`예);기념일 미라클`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #4
        embed = discord.Embed(title=";가사", description="뒤에 확인하고 싶은 노래 제목을 넣어보아요~! `;가사` `;lyric` `;l`\n`예);가사 심해`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #5
        embed = discord.Embed(title=";멜론", description="멜론의 음원 차트를 확인할 수 있습니다! `;멜론` `;melon`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #6
        embed = discord.Embed(title=";지니", description="지니의 음원 차틀를 확인할 수 있습니다! `;지니` `;genie`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #7
        embed = discord.Embed(title=";벅스", description="벅스의 음원 차트를 확인할 수 있습니다! `;벅스` `;bugs`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #8
        embed = discord.Embed(title=";움짤", description="멤버들의 gif들을 보고 싶으면! `;움짤` `;gif` `;g`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #9
        embed = discord.Embed(title=";옴", description="멤버들의 단체사진을 보고 싶으면! `;옴` `;op`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #10
        embed = discord.Embed(title=";쩡", description="효정의 사진을 보고싶으면! `;쩡` `;hp`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #11
        embed = discord.Embed(title=";밈", description="미미의 사진을 보고싶으면! `;밈` `;mp`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #12
        embed = discord.Embed(title=";샤", description="유아의 사진을 보고싶으면! `;샤` `;yp`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #13
        embed = discord.Embed(title=";씅", description="승희의 사진을 보고싶으면! `;씅` `;sp`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #14
        embed = discord.Embed(title=";죠", description="지호의 사진을 보고싶으면! `;죠` `;jp`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #15
        embed = discord.Embed(title=";윱", description="비니의 사진을 보고싶으면! `;윱` `;bp`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #16
        embed = discord.Embed(title=";린", description="아린의 사진을 보고싶으면! `;린` `;ap`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        #17
        embed = discord.Embed(title=";커맨드", description="`;오리너구리` `;fls` `;진`", color=random.choice(ccolor))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , cmdcount):
            if cmd == cmdlist[i]:
                await message.channel.send(embed=embedArray[i])
                break

#######################################################################################

#from name to funny image

    if message.content.startswith(";쩡") or message.content.startswith(";hp"):
        hp = [
            "https://i.imgur.com/9Sb1s8H.jpg",
            "https://i.imgur.com/Yb7y2iT.jpg",
            "https://i.imgur.com/cvwxjkv.jpg",
            "https://i.imgur.com/nS138Wi.jpg",
            "https://i.imgur.com/ohYaIl6.jpg",
            "https://i.imgur.com/ohYaIl6.jpg",
            "https://i.imgur.com/loUDygw.jpg",
            "https://i.imgur.com/njEjuJx.jpg",
            "https://i.imgur.com/CGaLvF9.jpg",
            "https://i.imgur.com/bEK7gPv.jpg",
            "https://i.imgur.com/0q1fW6j.jpg",
            "https://i.imgur.com/pvSg90o.jpg",
            "https://i.imgur.com/CDGjB0T.jpg",
            "https://i.imgur.com/gqt7BOJ.jpg",
            "https://i.imgur.com/o7Iwtj5.jpg",
            "https://i.imgur.com/dezn3I3.jpg",
            "https://i.imgur.com/FVvqIAd.jpg",
            "https://i.imgur.com/c08UAWq.jpg",
            "https://i.imgur.com/ht2ASGo.jpg",
            "https://i.imgur.com/ukLBvfr.jpg",
            "https://i.imgur.com/YdyBnXA.jpg",
            "https://i.imgur.com/Sb8yyWL.jpg",
            "https://i.imgur.com/dyybgOL.jpg",
            "https://i.imgur.com/KK3e2lv.jpg",
            "https://i.imgur.com/mSMl4Fd.jpg",
            "https://i.imgur.com/0Sxwu9t.jpg",
            "https://i.imgur.com/2XfUfPJ.jpg",
            "https://i.imgur.com/uNwoW5D.jpg",
            "https://i.imgur.com/bGEfdIB.jpg",
            "https://i.imgur.com/46DpBBM.jpg",
            "https://i.imgur.com/IbhCv6b.jpg",
            "https://i.imgur.com/Sr43qvb.jpg",
            "https://i.imgur.com/3UWN1t8.jpg",
            "https://i.imgur.com/DvlBeIe.jpg",
            "https://i.imgur.com/kGHcStU.jpg"
        ]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 효정님의 사진***", color=0xFF0000)
        embed.set_image(url=random.choice(hp))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";밈") or message.content.startswith(";mp"):
        mp = [
            "https://i.imgur.com/eJiBC4S.jpg",
            "https://i.imgur.com/oL1UofR.jpg",
            "https://i.imgur.com/0uhqhYI.jpg",
            "https://i.imgur.com/zRJjFgS.jpg",
            "https://i.imgur.com/jKcVTLZ.jpg",
            "https://i.imgur.com/r0pTR43.jpg",
            "https://i.imgur.com/6TkOd6O.jpg",
            "https://i.imgur.com/WDWjKrf.jpg",
            "https://i.imgur.com/9jSdbvm.jpg",
            "https://i.imgur.com/kPcw57O.jpg",
            "https://i.imgur.com/9YOFpsM.jpg",
            "https://i.imgur.com/oQvFVVW.jpg",
            "https://i.imgur.com/kpjxa6e.jpg",
            "https://i.imgur.com/WG1itWf.jpg",
            "https://i.imgur.com/u774lye.jpg",
            "https://i.imgur.com/NKKpL1J.jpg",
            "https://i.imgur.com/wB8M4oN.jpg",
            "https://i.imgur.com/39c7xfk.jpg",
            "https://i.imgur.com/NsLBKdO.jpg",
            "https://i.imgur.com/zYk2ETN.jpg",
            "https://i.imgur.com/UanvM9d.jpg",
            "https://i.imgur.com/WvTCU3S.jpg",
            "https://i.imgur.com/NR3SPER.jpg",
            "https://i.imgur.com/SoD79HO.jpg",
            "https://i.imgur.com/0ctRbzl.jpg",
            "https://i.imgur.com/I8cYa5c.jpg",
            "https://i.imgur.com/Cc3zSvr.jpg",
            "https://i.imgur.com/ANxizVU.jpg",
            "https://i.imgur.com/vrNQPBH.jpg",
            "https://i.imgur.com/KTEVmzI.jpg",
            "https://i.imgur.com/gTYPzrM.jpg"
        ]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 미미님의 사진***", color=0x58FA58)
        embed.set_image(url=random.choice(mp))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";샤") or message.content.startswith(";yp"):
        yp = [
            "https://i.imgur.com/wdy7V1R.jpg",
            "https://i.imgur.com/Cw3nCen.jpg",
            "https://i.imgur.com/z0cUqSH.jpg",
            "https://i.imgur.com/7pZ9kcp.jpg",
            "https://i.imgur.com/TQlRcVT.jpg",
            "https://i.imgur.com/6KUBE0A.jpg",
            "https://i.imgur.com/fPelHHi.jpg",
            "https://i.imgur.com/R6KelMg.jpg",
            "https://i.imgur.com/YHwE9qD.jpg",
            "https://i.imgur.com/xmJIrhm.jpg",
            "https://i.imgur.com/O1vIRCJ.jpg",
            "https://i.imgur.com/vcVraku.jpg",
            "https://i.imgur.com/6rnORGW.jpg",
            "https://i.imgur.com/l4JXN0a.jpg",
            "https://i.imgur.com/V4xmvue.jpg",
            "https://i.imgur.com/KA1niD3.jpg",
            "https://i.imgur.com/sRcHzaO.jpg",
            "https://i.imgur.com/aaTyqyi.jpg",
            "https://i.imgur.com/00XspHS.jpg",
            "https://i.imgur.com/vMDTXff.jpg",
            "https://i.imgur.com/2OmAN8H.jpg",
            "https://i.imgur.com/UCExBk5.jpg",
            "https://i.imgur.com/r8XZ6qt.jpg",
            "https://i.imgur.com/ZlhKmvq.jpg",
            "https://i.imgur.com/Ub5QDle.jpg",
            "https://i.imgur.com/XcAiHdJ.jpg",
            "https://i.imgur.com/PFRLp3j.jpg",
            "https://i.imgur.com/1GACdPc.jpg",
            "https://i.imgur.com/5hJ5tfb.jpg",
            "https://i.imgur.com/jH9iNv3.jpg"
        ]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 유아님의 사진***", color=0xFE9A2E)
        embed.set_image(url=random.choice(yp))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";씅") or message.content.startswith(";sp"):
        sp = [
            "https://i.imgur.com/sewaJgY.jpg",
            "https://i.imgur.com/qfNHSqf.jpg",
            "https://i.imgur.com/SCZ8eCU.jpg",
            "https://i.imgur.com/uhWjIft.jpg",
            "https://i.imgur.com/lWSC93E.jpg",
            "https://i.imgur.com/ME1AF8n.jpg",
            "https://i.imgur.com/1xj2r8r.jpg",
            "https://i.imgur.com/1y5wgLX.jpg",
            "https://i.imgur.com/RhJgkPi.jpg",
            "https://i.imgur.com/47LH5Vz.jpg",
            "https://i.imgur.com/RadvivE.jpg",
            "https://i.imgur.com/3XaC0XC.jpg",
            "https://i.imgur.com/AbKLHQm.jpg",
            "https://i.imgur.com/IyNjMFw.jpg",
            "https://i.imgur.com/VAt2Uxy.jpg",
            "https://i.imgur.com/8BIuaXc.jpg",
            "https://i.imgur.com/OKF9Pov.jpg",
            "https://i.imgur.com/LY2fu43.jpg",
            "https://i.imgur.com/TCxIq8v.jpg",
            "https://i.imgur.com/BZMVmLA.jpg",
            "https://i.imgur.com/76VxEu3.jpg",
            "https://i.imgur.com/x26lLRL.jpg",
            "https://i.imgur.com/iNdWr2K.jpg",
            "https://i.imgur.com/zIBPrD2.jpg",
            "https://i.imgur.com/fJR0OHg.jpg",
            "https://i.imgur.com/jP6C3Gl.jpg",
            "https://i.imgur.com/xrNs8tC.jpg",
            "https://i.imgur.com/q8wwZXG.jpg",
            "https://i.imgur.com/FpCsbV4.jpg",
            "https://i.imgur.com/wKsRATf.jpg",
            "https://i.imgur.com/nDSImWw.jpg",
            "https://i.imgur.com/hWsgze2.jpg",
            "https://i.imgur.com/s9OVUwv.jpg",
            "https://i.imgur.com/Qo4zSWh.jpg"
        ]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 승희님의 사진***", color=0xF78181)
        embed.set_image(url=random.choice(sp))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";죠") or message.content.startswith(";jp"):
        jp = [
            "https://i.imgur.com/NAvalOI.jpg",
            "https://i.imgur.com/5jb73vb.jpg",
            "https://i.imgur.com/HzAVs52.jpg",
            "https://i.imgur.com/StIOUI3.jpg",
            "https://i.imgur.com/psn9yPH.jpg",
            "https://i.imgur.com/eoaWMpL.jpg",
            "https://i.imgur.com/JTFGpLp.jpg",
            "https://i.imgur.com/TnsRNKc.jpg",
            "https://i.imgur.com/EnwgzXN.jpg",
            "https://i.imgur.com/9dzxXJA.jpg",
            "https://i.imgur.com/ZZFunwN.jpg",
            "https://i.imgur.com/kqVg2ss.jpg",
            "https://i.imgur.com/Ze3tYeF.jpg",
            "https://i.imgur.com/FWjhM2Z.jpg",
            "https://i.imgur.com/kmagcJW.jpg",
            "https://i.imgur.com/4o487DK.jpg",
            "https://i.imgur.com/RFvlGYc.jpg",
            "https://i.imgur.com/tk2ObYp.jpg",
            "https://i.imgur.com/pqBsSWx.jpg",
            "https://i.imgur.com/CGzOQQr.jpg",
            "https://i.imgur.com/zaeiXZt.jpg",
            "https://i.imgur.com/Q1t1Z5Y.jpg",
            "https://i.imgur.com/8OPSLb6.jpg",
            "https://i.imgur.com/rCSFJwS.jpg",
            "https://i.imgur.com/OU9eB0V.jpg",
            "https://i.imgur.com/HRVKgIB.jpg",
            "https://i.imgur.com/SNXrPKf.jpg",
            "https://i.imgur.com/U2SCisc.jpg",
            "https://i.imgur.com/nwiODqN.jpg",
            "https://i.imgur.com/flORPMm.jpg",
            "https://i.imgur.com/xI8rBW7.jpg",
            "https://i.imgur.com/fAQJDcQ.jpg",
            "https://i.imgur.com/VHtct9t.jpg",
            "https://i.imgur.com/ivc223F.jpg",
            "https://i.imgur.com/2xgG3UB.jpg"
        ]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 지호님의 사진***", color=0x08088A)
        embed.set_image(url=random.choice(jp))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";윱") or message.content.startswith(";bp"):
        bp = [
            "https://i.imgur.com/BLWEW3A.jpg",
            "https://i.imgur.com/RQmOC7f.jpg",
            "https://i.imgur.com/VkemNem.jpg",
            "https://i.imgur.com/C5dCT3o.jpg",
            "https://i.imgur.com/Ovdi4tp.jpg",
            "https://i.imgur.com/pFhLrxH.jpg",
            "https://i.imgur.com/t16qh5k.jpg",
            "https://i.imgur.com/V7yz5F3.jpg",
            "https://i.imgur.com/Q0AoTv5.jpg",
            "https://i.imgur.com/w4fBcJO.jpg",
            "https://i.imgur.com/ufj9xOS.jpg",
            "https://i.imgur.com/6ebOyL2.jpg",
            "https://i.imgur.com/L9QNdBc.jpg",
            "https://i.imgur.com/1MBK92y.jpg",
            "https://i.imgur.com/RwrtVDL.jpg",
            "https://i.imgur.com/BRgX8Qx.jpg",
            "https://i.imgur.com/6YrUsAL.jpg",
            "https://i.imgur.com/Ab9V7Sj.jpg",
            "https://i.imgur.com/zZjdYiW.jpg",
            "https://i.imgur.com/GreA9Cz.jpg",
            "https://i.imgur.com/QqLiYbk.jpg",
            "https://i.imgur.com/nQgjqjm.jpg",
            "https://i.imgur.com/hZqCKCQ.jpg",
            "https://i.imgur.com/sHGMbIy.jpg",
            "https://i.imgur.com/QNO9MB8.jpg",
            "https://i.imgur.com/LbVhRxD.jpg",
            "https://i.imgur.com/E1oGgpz.jpg",
            "https://i.imgur.com/65goTqk.jpg",
            "https://i.imgur.com/V4morWq.jpg",
            "https://i.imgur.com/fuL4mkK.jpg",
            "https://i.imgur.com/vhux3EE.jpg",
            "https://i.imgur.com/1fbaWnv.jpg"
        ]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 비니님의 사진***", color=0x9F81F7)
        embed.set_image(url=random.choice(bp))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";린") or message.content.startswith(";ap"):
        ap = [
            "https://i.imgur.com/87gAvP8.jpg",
            "https://i.imgur.com/FM65FPR.jpg",
            "https://i.imgur.com/CbTHoUS.jpg",
            "https://i.imgur.com/CRaRwiG.jpg",
            "https://i.imgur.com/2Eaq0QP.jpg",
            "https://i.imgur.com/gFYu9vo.jpg",
            "https://i.imgur.com/Anc94Ed.jpg",
            "https://i.imgur.com/LwPiC4U.jpg",
            "https://i.imgur.com/0D6YEta.jpg",
            "https://i.imgur.com/xH3Zktn.jpg",
            "https://i.imgur.com/qF7uB9j.jpg",
            "https://i.imgur.com/g99Dhvk.jpg",
            "https://i.imgur.com/3npZ1sq.jpg",
            "https://i.imgur.com/HtahEt0.jpg",
            "https://i.imgur.com/YmQAeoA.jpg",
            "https://i.imgur.com/iEo68zn.jpg",
            "https://i.imgur.com/R0I0l7p.jpg",
            "https://i.imgur.com/XdyWo2u.jpg",
            "https://i.imgur.com/XA7nU2V.jpg",
            "https://i.imgur.com/2eAdPfk.jpg",
            "https://i.imgur.com/3hZXUU9.jpg",
            "https://i.imgur.com/ZIhoInn.jpg",
            "https://i.imgur.com/0HsfNGR.jpg",
            "https://i.imgur.com/woKJ17a.jpg",
            "https://i.imgur.com/iz8E6OT.jpg",
            "https://i.imgur.com/BvYlDlP.jpg",
            "https://i.imgur.com/q5f22sZ.jpg",
            "https://i.imgur.com/V1TEzAW.jpg",
            "https://i.imgur.com/DHhE3rb.jpg",
            "https://i.imgur.com/rKyBHUJ.jpg",
            "https://i.imgur.com/GOGYnSv.jpg",
            "https://i.imgur.com/KGW5eF1.jpg",
            "https://i.imgur.com/OeSKkQz.jpg"
        ]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 아린님의 사진***", color=0xF4FA58)
        embed.set_image(url=random.choice(ap))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)



    if message.content.startswith(";옴") or message.content.startswith(";op"):
        op = [
            "https://i.imgur.com/zSB6wwU.jpg",
            "https://i.imgur.com/zaGqwmt.jpg",
            "https://i.imgur.com/MeCJrIU.jpg",
            "https://i.imgur.com/XfJMAPu.png",
            "https://i.imgur.com/jjVbeQH.jpg",
            "https://i.imgur.com/WwthwsR.jpg",
            "https://i.imgur.com/5CymBWK.jpg",
            "https://i.imgur.com/t2szuot.jpg",
            "https://i.imgur.com/9R6jlPf.jpg",
            "https://i.imgur.com/8Y8B478.jpg",
            "https://i.imgur.com/IElV5bV.jpg",
            "https://i.imgur.com/k8i6QmI.jpg",
            "https://i.imgur.com/jFdmAyA.jpg",
            "https://i.imgur.com/aKNMkPF.jpg",
            "https://i.imgur.com/DysLWtf.jpg",
            "https://i.imgur.com/Mu0jaul.jpg",
            "https://i.imgur.com/0LU4Ddy.jpg",
            "https://i.imgur.com/hJhUrVo.jpg",
            "https://i.imgur.com/bzKYzuq.jpg",
            "https://i.imgur.com/XlW38eT.jpg",
            "https://i.imgur.com/sYYk2iN.jpg",
            "https://i.imgur.com/vZLvOt7.jpg"
        ]
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 단체사진***", color=random.choice(col))
        embed.set_image(url=random.choice(op))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";움짤") or message.content.startswith(";gif") or message.content.startswith(";g"):
        gp = [
            "https://thumbs.gfycat.com/LimitedConcreteAsianpiedstarling-size_restricted.gif",
            "https://thumbs.gfycat.com/SlowFocusedAmazontreeboa-size_restricted.gif",
            "https://thumbs.gfycat.com/OptimalUnderstatedCatbird-size_restricted.gif",
            "https://thumbs.gfycat.com/TintedFabulousCranefly-size_restricted.gif",
            "https://thumbs.gfycat.com/SpectacularBoilingArgali-size_restricted.gif",
            "https://thumbs.gfycat.com/BreakableMerryEuropeanfiresalamander-size_restricted.gif",
            "https://thumbs.gfycat.com/VelvetyWastefulBoubou-size_restricted.gif",
            "https://thumbs.gfycat.com/PaltryPoisedFattaileddunnart-size_restricted.gif",
            "https://thumbs.gfycat.com/MisguidedUnrealisticBagworm-size_restricted.gif",
            "https://thumbs.gfycat.com/RelievedWeeKatydid-size_restricted.gif",
            "https://thumbs.gfycat.com/DelectableGentleGalapagosmockingbird-size_restricted.gif",
            "https://thumbs.gfycat.com/OccasionalColossalBlacklemur-size_restricted.gif",
            "https://thumbs.gfycat.com/BigRepentantChimpanzee-size_restricted.gif",
            "https://thumbs.gfycat.com/PinkThirstyGoitered-size_restricted.gif",
            "https://thumbs.gfycat.com/ShrillAppropriateDesertpupfish-size_restricted.gif",
            "https://thumbs.gfycat.com/DeficientCanineIriomotecat-size_restricted.gif",
            "https://thumbs.gfycat.com/ShyVerifiableBufeo-size_restricted.gif",
            "https://thumbs.gfycat.com/IckyEssentialIberianchiffchaff-size_restricted.gif",
            "https://thumbs.gfycat.com/UnkemptAfraidGosling-size_restricted.gif",
            "https://thumbs.gfycat.com/PoorChubbyGuanaco-size_restricted.gif",
            "https://thumbs.gfycat.com/AbsoluteSentimentalAfricangoldencat-size_restricted.gif",
            "https://thumbs.gfycat.com/SameDimCoqui-size_restricted.gif",
            "https://thumbs.gfycat.com/GrossCoordinatedIrrawaddydolphin-size_restricted.gif",
            "https://thumbs.gfycat.com/AnimatedZealousKingfisher-size_restricted.gif",
            "https://thumbs.gfycat.com/OnlyRewardingGreatargus-size_restricted.gif",
            "https://thumbs.gfycat.com/ClassicTediousHuman-size_restricted.gif",
            "https://thumbs.gfycat.com/ShorttermGentleGaur-size_restricted.gif",
            "https://thumbs.gfycat.com/SecondaryWelloffIslandcanary-size_restricted.gif",
            "https://thumbs.gfycat.com/NearInformalJuliabutterfly-size_restricted.gif",
            "https://thumbs.gfycat.com/QuarterlyDeliriousBronco-size_restricted.gif",
            "https://thumbs.gfycat.com/WhisperedWigglyGoldenretriever-size_restricted.gif",
            "https://thumbs.gfycat.com/UnselfishEnormousLacewing-size_restricted.gif",
            "https://thumbs.gfycat.com/VictoriousPlasticHarvestmen-size_restricted.gif",
            "https://thumbs.gfycat.com/KindlyEmotionalCuscus-size_restricted.gif",
            "https://thumbs.gfycat.com/PointlessFilthyAfricanrockpython-size_restricted.gif",
            "https://thumbs.gfycat.com/CoarseSociableClingfish-size_restricted.gif",
            "https://thumbs.gfycat.com/AcademicMerryAlligatorsnappingturtle-size_restricted.gif",
            "https://thumbs.gfycat.com/BlaringCelebratedHammerheadbird-size_restricted.gif",
            "https://thumbs.gfycat.com/DeliciousLightHerring-size_restricted.gif",
            "https://thumbs.gfycat.com/CoolShowyAustraliancurlew-size_restricted.gif",
            "https://thumbs.gfycat.com/GlitteringWarmDormouse-size_restricted.gif",
            "https://thumbs.gfycat.com/HonorableSelfishBovine-size_restricted.gif",
            "https://thumbs.gfycat.com/GracefulGranularAsianpiedstarling-size_restricted.gif",
            "https://thumbs.gfycat.com/RepulsiveMelodicHypsilophodon-size_restricted.gif",
            "https://thumbs.gfycat.com/HilariousHighlevelBobolink-size_restricted.gif",
            "https://thumbs.gfycat.com/InsistentFlatIndianringneckparakeet-size_restricted.gif",
            "https://thumbs.gfycat.com/BeautifulHonestDromaeosaur-size_restricted.gif",
            "https://thumbs.gfycat.com/GraciousCriminalJavalina-size_restricted.gif",
            "https://thumbs.gfycat.com/WillingImportantIndianskimmer-size_restricted.gif",
            "https://thumbs.gfycat.com/OpulentVariableHedgehog-size_restricted.gif",
            "https://thumbs.gfycat.com/KlutzyLawfulKoodoo-size_restricted.gif",
            "https://thumbs.gfycat.com/GorgeousAridBlobfish-size_restricted.gif",
            "https://thumbs.gfycat.com/AromaticAccomplishedKillerwhale-size_restricted.gif",
            "https://thumbs.gfycat.com/ThickMerryDuckbillcat-size_restricted.gif",
            "https://thumbs.gfycat.com/PotableShorttermIndianringneckparakeet-size_restricted.gif",
            "https://thumbs.gfycat.com/DimHeartfeltBlackbear-size_restricted.gif",
            "https://thumbs.gfycat.com/YawningHappyDikkops-size_restricted.gif",
            "https://thumbs.gfycat.com/PassionateVibrantBird-size_restricted.gif",
            "https://thumbs.gfycat.com/CarefreeMintyBuck-size_restricted.gif",
            "https://thumbs.gfycat.com/AccomplishedWellinformedAustrianpinscher-size_restricted.gif",
            "https://thumbs.gfycat.com/SolidUnsungKatydid-size_restricted.gif",
            "https://thumbs.gfycat.com/FabulousShamefulAbyssiniancat-size_restricted.gif",
            "https://thumbs.gfycat.com/ElaborateCelebratedInexpectatumpleco-size_restricted.gif"
        ]
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 GIF***", color=random.choice(col))
        embed.set_image(url=random.choice(gp))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

#######################################################################################

#from name to member's birth

    today = date.today()
    hjd = date(1994, 7, 28)
    hj_birth = date(today.year, 7, 28)
    mmd = date(1995, 5, 1)
    mm_birth = date(today.year, 5, 1)
    yad = date(1995, 9, 17)
    ya_birth = date(today.year, 9, 17)
    shd = date(1996, 1, 25)
    sh_birth = date(today.year, 1, 25)
    jhd = date(1997, 4, 4)
    jh_birth = date(today.year, 4, 4)
    bnd = date(1997, 9, 9)
    bn_birth = date(today.year, 9, 9)
    ard = date(1999, 6, 18)
    ar_birth = date(today.year, 6, 18)
    jnd = date(1995, 1, 22)
    jn_birth = date(today.year, 1, 22)

    hj = hjd.strftime("%Y년 %m월 %d일")
    mm = mmd.strftime("%Y년 %m월 %d일")
    ya = yad.strftime("%Y년 %m월 %d일")
    sh = shd.strftime("%Y년 %m월 %d일")
    jh = jhd.strftime("%Y년 %m월 %d일")
    bn = bnd.strftime("%Y년 %m월 %d일")
    ar = ard.strftime("%Y년 %m월 %d일")
    jn = jnd.strftime("%Y년 %m월 %d일")

    hj_births = hj_birth.strftime("%Y년 %m월 %d일")
    mm_births = mm_birth.strftime("%Y년 %m월 %d일")
    ya_births = ya_birth.strftime("%Y년 %m월 %d일")
    sh_births = sh_birth.strftime("%Y년 %m월 %d일")
    jh_births = jh_birth.strftime("%Y년 %m월 %d일")
    bn_births = bn_birth.strftime("%Y년 %m월 %d일")
    ar_births = ar_birth.strftime("%Y년 %m월 %d일")
    jn_births = jn_birth.strftime("%Y년 %m월 %d일")

    if message.content.startswith(";생일") or message.content.startswith(";birth") or message.content.startswith(";b"):
        bir = message.content.split(" ")[1]
        songlist = ['효정','미미','유아','승희','지호','비니','아린','진이']
        songcount = 8
        embedArray = []

        delta = today - hjd
        if hj_birth < today:
            hj_birth = hj_birth.replace(year=today.year + 1)
        birth = hj_birth - today
        embed = discord.Embed(title="효정의 생일", description="생년월일: " + str(hj) + "\n" + str(delta.days) + "일 째에요!" + "\n" + str(hj_births) + "까지 " + str(birth.days) + "일 남았어요!", color=0xFF0000)
        embed.set_image(url="http://ohmy-girl.com/omg_official/img/gallery/gallery_hyojung.png")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - mmd
        if mm_birth < today:
            mm_birth = mm_birth.replace(year=today.year + 1) 
        birth = mm_birth - today
        embed = discord.Embed(title="미미의 생일", description="생년월일: " + str(mm) + "\n" + str(delta.days) + "일 째에요!" + "\n" + str(mm_births) + "까지 " + str(birth.days) + "일 남았어요!", color=0x58FA58)
        embed.set_image(url="http://ohmy-girl.com/omg_official/img/gallery/gallery_mimi.png")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - yad
        if ya_birth < today:
            ya_birth = ya_birth.replace(year=today.year + 1) 
        birth = ya_birth - today
        embed = discord.Embed(title="유아의 생일", description="생년월일: " + str(ya) + "\n" + str(delta.days) + "일 째에요!" + "\n" + str(ya_births) + "까지 " + str(birth.days) + "일 남았어요!", color=0xFE9A2E)
        embed.set_image(url="http://ohmy-girl.com/omg_official/img/gallery/gallery_yooa.png")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - shd
        if sh_birth < today:
            sh_birth = sh_birth.replace(year=today.year + 1) 
        birth = sh_birth - today
        embed = discord.Embed(title="승희의 생일", description="생년월일: " + str(sh) + "\n" + str(delta.days) + "일 째에요!" + "\n" + str(sh_births) + "까지 " + str(birth.days) + "일 남았어요!", color=0xF78181)
        embed.set_image(url="http://ohmy-girl.com/omg_official/img/gallery/gallery_seunghee.png")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - jhd
        if jh_birth < today:
            jh_birth = jh_birth.replace(year=today.year + 1) 
        birth = jh_birth - today
        embed = discord.Embed(title="지호의 생일", description="생년월일: " + str(jh) + "\n" + str(delta.days) + "일 째에요!" + "\n" + str(jh_births) + "까지 " + str(birth.days) + "일 남았어요!", color=0x08088A)
        embed.set_image(url="http://ohmy-girl.com/omg_official/img/gallery/gallery_jiho.png")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - bnd
        if bn_birth < today:
            bn_birth = bn_birth.replace(year=today.year + 1) 
        birth = bn_birth - today
        embed = discord.Embed(title="비니의 생일", description="생년월일: " + str(bn) + "\n" + str(delta.days) + "일 째에요!" + "\n" + str(bn_births) + "까지 " + str(birth.days) + "일 남았어요!", color=0x9F81F7)
        embed.set_image(url="http://ohmy-girl.com/omg_official/img/gallery/gallery_binnie.png")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - ard
        if ar_birth < today:
            ar_birth = ar_birth.replace(year=today.year + 1) 
        birth = ar_birth - today
        embed = discord.Embed(title="아린의 생일", description="생년월일: " + str(ar) + "\n" + str(delta.days) + "일 째에요!" + "\n" + str(ar_births) + "까지 " + str(birth.days) + "일 남았어요!", color=0xF4FA58)
        embed.set_image(url="http://ohmy-girl.com/omg_official/img/gallery/gallery_arin.png")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - jnd
        if jn_birth < today:
            jn_birth = jn_birth.replace(year=today.year + 1)
        birth = jn_birth - today
        embed = discord.Embed(title="진이의 생일", description="생년월일: " + str(jn) + "\n" + str(delta.days) + "일 째에요!" + "\n" + str(jn_births) + "까지 " + str(birth.days) + "일 남았어요!", color=0xF781F3)
        embed.set_image(url="https://i.imgur.com/25AAKpQ.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if bir == songlist[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";생일 효정") or message.content.startswith(";birth 효정") or message.content.startswith(";b 효정"):
        if today == hj_birth:
            embed = discord.Embed(description="오마이걸의 상큼한 리더! 효정님의 생일을 축하드려요!!", color=0xFF0000)
            embed.set_footer(text = "그대의 기적과 우리의 옴걸")
            await message.channel.send(embed=embed)

    if message.content.startswith(";생일 미미") or message.content.startswith(";birth 미미") or message.content.startswith(";b 미미"):
        if today == mm_birth:
            embed = discord.Embed(description="오마이걸의 카리스마 메인 래퍼! 미미님의 생일을 축하드려요!!", color=0x58FA58)
            embed.set_footer(text = "그대의 기적과 우리의 옴걸")
            await message.channel.send(embed=embed)

    if message.content.startswith(";생일 유아") or message.content.startswith(";birth 유아") or message.content.startswith(";b 유아"):
        if today == ya_birth:
            embed = discord.Embed(description="오마이걸의 체리 메인댄서! 유아님의 생일을 축하드려요!!", color=0xFE9A2E)
            embed.set_footer(text = "그대의 기적과 우리의 옴걸")
            await message.channel.send(embed=embed)

    if message.content.startswith(";생일 승희") or message.content.startswith(";birth 승희") or message.content.startswith(";b 승희"):
        if today == sh_birth:
            embed = discord.Embed(description="오마이걸의 재간둥이 메인보컬! 승희님의 생일을 축하드려요!!", color=0xF78181)
            embed.set_footer(text = "그대의 기적과 우리의 옴걸")
            await message.channel.send(embed=embed)

    if message.content.startswith(";생일 지호") or message.content.startswith(";birth 지호") or message.content.startswith(";b 지호"):
        if today == jh_birth:
            embed = discord.Embed(description="오마이걸의 잘생긴 여신! 지호님의 생일을 축하드려요!!", color=0x08088A)
            embed.set_footer(text = "그대의 기적과 우리의 옴걸")
            await message.channel.send(embed=embed)

    if message.content.startswith(";생일 비니") or message.content.startswith(";birth 비니") or message.content.startswith(";b 비니"):
        if today == bn_birth:
            embed = discord.Embed(description="오마이걸의 똑순이 여신! 비니님의 생일을 축하드려요!!", color=0x9F81F7)
            embed.set_footer(text = "그대의 기적과 우리의 옴걸")
            await message.channel.send(embed=embed)

    if message.content.startswith(";생일 아린") or message.content.startswith(";birth 아린") or message.content.startswith(";b 아린"):
        if today == ar_birth:
            embed = discord.Embed(description="오마이걸의 귀염둥이 막내! 아린님의 생일을 축하드려요!!", color=0xF4FA58)
            embed.set_footer(text = "그대의 기적과 우리의 옴걸")
            await message.channel.send(embed=embed)

    if message.content.startswith(";생일 진이") or message.content.startswith(";birth 진이") or message.content.startswith(";b 진이"):
        if today == jn_birth:
            embed = discord.Embed(description="언제나 함께였고 지금도 함께인 진이님의 생일을 축하드려요!!", color=0xF781F3)
            embed.set_footer(text = "그대의 기적과 우리의 옴걸")
            await message.channel.send(embed=embed)

#######################################################################################

#from info to date

    today = date.today()
    devid = date(2015, 4, 21)
    fild = date(2018, 1, 23)
    jild = date(2019, 8, 18)
    miracled = date(2016, 3, 28)

    devi = devid.strftime("%Y년 %m월 %d일")
    fil = fild.strftime("%Y년 %m월 %d일")
    jil = jild.strftime("%Y년 %m월 %d일")
    miracle = miracled.strftime("%Y년 %m월 %d일")

    if message.content.startswith(";기념일") or message.content.startswith(";date") or message.content.startswith(";d"):
        holli = message.content.split(" ")[1]
        daylist1 = ['데뷔','첫1위','지상파1위','미라클']
        daylist2 = ['데뷔','비정1위','번지1위','미라클']
        daylist3 = ['데뷔','더쇼1위','인기가요1위','미라클']
        daylist4 = ['데뷔','더쇼1위','인가1위','미라클']
        songcount = 4
        embedArray = []

        delta = today - devi
        embed = discord.Embed(title="데뷔일", description=str(devi) + "\n" + str(delta.days) + "일 째에요!", color=0xF5F6CE)
        embed.set_image(url="https://i.imgur.com/yblAqfv.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - fil
        embed = discord.Embed(title="첫1위일", description=str(fil) + "\n" + str(delta.days) + "일 째에요!", color=0x81F7F3)
        embed.set_image(url="https://i.imgur.com/eje8xVT.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - jil
        embed = discord.Embed(title="지상파1위일", description=str(jil) + "\n" + str(delta.days) + "일 째에요!", color=0xE2A9F3)
        embed.set_image(url="https://i.imgur.com/7cXgoSk.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        delta = today - miracle
        embed = discord.Embed(title="미라클 탄생일", description=str(miracle) + "\n" + str(delta.days) + "일 째에요!", color=0xf4a6d7)
        embed.set_image(url="https://ww.namu.la/s/bff1d45b9ac7a9f8aea6b0b2832275c83b17c328f210068628c3de50db13876291dab41f4b726f5ec667b570ac9500373edf095d728e1ea9fc8831db9510e5114f0c450f02468c36a270903530c895ea6e0c62da2680941f1839146bfe879f50")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if holli == daylist1[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if holli == daylist2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if holli == daylist3[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if holli == daylist4[i]:
                await message.channel.send(embed=embedArray[i])
                break

#######################################################################################

#from album name to date

    if message.content.startswith(";앨범") or message.content.startswith(";album") or message.content.startswith(";a"):
        album = message.content.split(" ")[1]
        songlist = ['큐피드','클로저','핑크오션','윈디데이','내얘길들어봐','컬러링북','비밀정원','바나나알러지원숭이','불꽃놀이','다섯번째계절','번지','살짝설렜어']
        songlist2 = ['미니1집','미니2집','미니3집','미니3집리패키지','섬머스페셜','미니4집','미니5집','유닛1집','미니6집','정규1집','섬머스페셜리패키지','미니7집']
        songlist3 = ['오마이걸','클로져','라이어','윈데','내얘들','컬북','비정','바알원','불놀','다계','번지','살설']
        songcount = 12
        embedArray = []

        embed = discord.Embed(title="미니 1집 [OH MY GIRL]", description="`20150420`\nOH MY GIRL!\nCUPID\nHOT SUMMER NIGHTS\n궁금한걸요\n", color=0x8d8d8d)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/4976/497671.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="미니 2집 [CLOSER]", description="`20151008`\nCloser\nSay No More\nPlayground\nSugar Baby\nRound About\n", color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/5353/535331.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="미니 3집 [PINK OCEAN]", description="`20160328`\nLIAR LIAR\nB612\nI FOUND LOVE\nKNOCK KNOCK\n한 발짝 두 발짝\n", color=0xff5fa2)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200268/20026818.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="미니 3집 re [WINDY DAY]", description="`20160526`\nWINDY DAY\nSTUPID IN LOVE\nLIAR LIAR\nB612\nI FOUND LOVE\nKNOCK KNOCK\n한 발짝 두 발짝\nLIAR LIAR (Chinese Ver.)\n", color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200374/20037484.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="Summer Special [내 얘길 들어봐]", description="`20160801`\n내 얘길 들어봐 (A-ing) (feat.스컬 &하하)\n한여름의 크리스마스\nJe T'aime\n거짓말도 보여요\n", color=0x00a4e5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200479/20047978.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="미니 4집 [Coloring Book]", description="`20170403`\n컬러링북 (Coloring Book)\nReal World\nAgit\nIn My Dreams\nPerfect Day\n", color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200905/20090525.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="미니 5집 [비밀정원]", description="`20180109`\n비밀정원\nLove O'clock\nButterfly\nSixteen\nMagic\n", color=0x041f56)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201408/20140893.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="유닛 1집 [바나나 알러지 원숭이]", description="`20180402`\nUkiuki waikiki (Intro)\n바나나 알러지 원숭이\n하더라\n반한 게 아냐\n", color=0xfabcd5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201573/20157333.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="미니 6집 [Remember Me]", description="`20180910`\n불꽃놀이\n메아리\nTwilight\nIllusion\n우리 이야기\n", color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201932/20193267.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="정규 1집 [The Fifth Season]", description="`20190508`\n다섯 번째 계절 (SSFWL)\n소나기\n미제 (Case No.L5VE)\nTic Toc\n유성 (Gravity)\nCrime Scene\n심해 (마음이라는 바다)\nVogue\nCheckmate\n다섯 번째 계절 (SSFWL) (Inst.)\n", color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="Summer Special RE [Fall In Love]", description="`20190805`\nBUNGEE (Fall in Love)\nTropical Love\n다섯 번째 계절 (SSFWL)\n소나기\n미제 (Case No.L5VE)\nTic Toc\n유성 (Gravity)\nCrime Scene\n심해 (마음이라는 바다)\nVogue\nCheckmate\n다섯 번째 계절 (SSFWL) (Inst.)\n", color=0x8fe1ef)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202696/20269643.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="미니 7집 [NONSTOP]", description="`20200427`\n살짝 설렜어 (Nonstop)\nDolphin\n꽃차 (Flower Tea)\nNE♡N\nKrystal\n", color=0x2f9d27)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/141168/14116820.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if album == songlist[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if album == songlist2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if album == songlist3[i]:
                await message.channel.send(embed=embedArray[i])
                break      

#######################################################################################

#Easter Egg

    if message.content.startswith(";오리너구리"):
        platy = [
            "https://thumbs.gfycat.com/PracticalPowerfulKingsnake-size_restricted.gif",
            "https://thumbs.gfycat.com/VictoriousTenderGermanwirehairedpointer-size_restricted.gif",
            "https://thumbs.gfycat.com/HonoredIcyIsopod-size_restricted.gif",
            "https://thumbs.gfycat.com/FrayedHandmadeBorer-size_restricted.gif",
            "https://thumbs.gfycat.com/HomelyEnlightenedAssassinbug-size_restricted.gif",
            "https://thumbs.gfycat.com/TemptingBlankBobwhite-size_restricted.gif",
            "https://thumbs.gfycat.com/AlarmingReflectingDutchshepherddog-size_restricted.gif",
            "https://thumbs.gfycat.com/UnlinedEagerEwe-size_restricted.gif",
            "https://thumbs.gfycat.com/ImportantUnhealthyChipmunk-size_restricted.gif",
            "https://thumbs.gfycat.com/PhysicalVictoriousClingfish-size_restricted.gif",
            "https://thumbs.gfycat.com/HotFixedAstrangiacoral-size_restricted.gif",
            "https://thumbs.gfycat.com/EnviousSoftCats-size_restricted.gif"
        ]
        embed = discord.Embed(description="Hi~ I am Developer", color=0x0B3B17)
        embed.set_image(url=random.choice(platy))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";진") or message.content.startswith(";np"):
        jin = [
            "https://i.imgur.com/modMbwB.jpg",
            "https://i.imgur.com/MVXfpsm.jpg",
            "https://i.imgur.com/L0r0TXv.jpg",
            "https://i.imgur.com/ZXIPKCj.jpg",
            "https://i.imgur.com/4zPMSyy.jpg",
            "https://i.imgur.com/Ble83d5.jpg",
            "https://i.imgur.com/mNhPB1q.jpg",
            "https://i.imgur.com/XYL07Hz.jpg",
            "https://i.imgur.com/ME70daE.jpg",
            "https://i.imgur.com/n2hK6YP.jpg",
            "https://i.imgur.com/eWoCiVZ.jpg",
            "https://i.imgur.com/mcYSK2Y.jpg",
            "https://i.imgur.com/u0j1yj2.jpg"
        ]
        embed = discord.Embed(description= "***<@" + str(id) + ">" + "님이 좋아할 만한 진이님의 사진***", color=0xF781F3)
        embed.set_image(url=random.choice(jin))
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";fls"):
        embed = discord.Embed(description="???", color=0xF4FA58)
        embed.set_image(url="https://i.imgur.com/A47mYsG.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";타노스"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "누나 좋아해여", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/ScaredGroundedAntelopegroundsquirrel-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";째릿"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "승희 : (쾅!!) 째릿!", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/ScaryKeenBison-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";승하"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "승-하!", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/ZigzagSolidCamel-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";닥쳐"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "닥...쳐...ㅎ", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/WelllitPastCusimanse-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";커플이야"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "뭐야!?! 커플이얏!?!!?", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/DapperRedAmericanpainthorse-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";털썩"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "어디가니..?", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/EminentFlawedFrenchbulldog-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";헤드셋"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "아구..", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/OptimalUnderstatedCatbird-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)
    
    if message.content.startswith(";딱밤"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "비니의 딱밤은 세계 제일", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/AppropriateLeadingKitfox-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";짜증나"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "짜.증.나", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/SelfassuredAcidicEchidna-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";훌라훌라"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "선생님 몰래 춤추기~~~", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/AffectionateThoseGoldfish-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

    if message.content.startswith(";짜잔"):
        col = [0xfca6d1,0x9adbe8,0xebe6ad]
        embed = discord.Embed(description= "승희님이 나가신다!!", color=random.choice(col))
        embed.set_image(url="https://thumbs.gfycat.com/RipeObedientBobcat-size_restricted.gif")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        await message.channel.send(embed=embed)

#######################################################################################

#songs lyrics

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('01_1.txt',encoding='utf-8')
        ohmygirl = f.read()
        f.close()

        f = open('01_2.txt',encoding='utf-8')
        cupid = f.read()
        f.close()

        f = open('01_3.txt',encoding='utf-8')
        hsn = f.read()
        f.close()

        f = open('01_4.txt',encoding='utf-8')
        idk = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['오마이걸','큐피드','핫썸머나이츠','궁금한걸요']
        songs2 = ['OHMYGIRL','CUPID','HOT','궁금한걸요']
        songs3 = ['ohmygirl','cupid','hot','궁금한걸요']
        songcount = 4
        embedArray = []

        embed = discord.Embed(title="***미니 1집 [OH MY GIRL] - Oh My Girl!***",
        description=str(ohmygirl),
        color=0x8d8d8d)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/4976/497671.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 1집 [OH MY GIRL] - CUPID***",
        description=str(cupid),
        color=0x8d8d8d)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/4976/497671.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 1집 [OH MY GIRL] - HOT SUMMER NIGHTS***",
        description=str(hsn),
        color=0x8d8d8d)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/4976/497671.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 1집 [OH MY GIRL] - 궁금한걸요***",
        description=str(idk),
        color=0x8d8d8d)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/4976/497671.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('02_1.txt',encoding='utf-8')
        closer = f.read()
        f.close()

        f = open('02_2.txt',encoding='utf-8')
        sym = f.read()
        f.close()

        f = open('02_3.txt',encoding='utf-8')
        prg = f.read()
        f.close()

        f = open('02_4.txt',encoding='utf-8')
        sbaby = f.read()
        f.close()

        f = open('02_5.txt',encoding='utf-8')
        rabout = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['클로저','세이노모아','플레이그라운드','슈가베이비','라운드어바웃']
        songs2 = ['Closer','SAY','PLAYGROUND','SUGAR','ROUND']
        songs3 = ['closer','say','playground','sugar','round']
        songcount = 5
        embedArray = []

        embed = discord.Embed(title="***미니 2집 [CLOSER] - Closer***",
        description=str(closer),
        color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/5353/535331.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 2집 [CLOSER] - SAY NO MORE***",
        description=str(sym),
        color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/5353/535331.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 2집 [CLOSER] - PLAYGROUND***",
        description=str(prg),
        color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/5353/535331.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 2집 [CLOSER] - SUGAR BABY***",
        description=str(sbaby),
        color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/5353/535331.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 2집 [CLOSER] - ROUND ABOUT***",
        description=str(rabout),
        color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/5353/535331.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)


        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('03_1.txt',encoding='utf-8')
        liar = f.read()
        f.close()

        f = open('03_2.txt',encoding='utf-8')
        b612 = f.read()
        f.close()

        f = open('03_3.txt',encoding='utf-8')
        ifl = f.read()
        f.close()

        f = open('03_4.txt',encoding='utf-8')
        knock = f.read()
        f.close()

        f = open('03_5.txt',encoding='utf-8')
        steps = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['라이어라이어','비육일이','아이파운드러브','낙낙','한발짝두발짝']
        songs2 = ['LIAR','B612','I','KNOCK','한발짝']
        songs3 = ['liar','b612','I','knock','한발짝']
        songcount = 5
        embedArray = []

        embed = discord.Embed(title="***미니 3집 [PINK OCEAN] - LIAR LIAR***",
        description=str(liar),
        color=0xff5fa2)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200268/20026818.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 3집 [PINK OCEAN] - B612***",
        description=str(b612),
        color=0xff5fa2)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200268/20026818.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 3집 [PINK OCEAN] - I FOUND LOVE***",
        description=str(ifl),
        color=0xff5fa2)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200268/20026818.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 3집 [PINK OCEAN] - KNOCK KNOCK***",
        description=str(knock),
        color=0xff5fa2)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200268/20026818.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 3집 [PINK OCEAN] - 한 발짝 두 발짝***",
        description=str(steps),
        color=0xff5fa2)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200268/20026818.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('03_r_1.txt',encoding='utf-8')
        windy = f.read()
        f.close()

        f = open('03_r_2.txt',encoding='utf-8')
        sil = f.read()
        f.close()

        f = open('03_r_3.txt',encoding='utf-8')
        liarch = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['윈디데이','스투피드인러브','라이어라이어중국어']
        songs2 = ['WINDY','STUPID','중국어']
        songs3 = ['윈데','STUPID','중국어']
        songs4 = ['windy','stupid','중국어']
        songcount = 3
        embedArray = []

        embed = discord.Embed(title="***미니 3집 re [WINDY DAY] - WINDY DAY***",
        description=str(windy),
        color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200374/20037484.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 3집 re [WINDY DAY] - STUPID IN LOVE***",
        description=str(sil),
        color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200374/20037484.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 3집 re [WINDY DAY] - LIAR LIAR (Chinese.ver)***",
        description=str(liarch),
        color=0x007a4b)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200374/20037484.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs4[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('00_ss_1.txt',encoding='utf-8')
        hearme = f.read()
        f.close()

        f = open('00_ss_2.txt',encoding='utf-8')
        sumxmas = f.read()
        f.close()

        f = open('00_ss_3.txt',encoding='utf-8')
        taime = f.read()
        f.close()

        f = open('00_ss_4.txt',encoding='utf-8')
        sawlie = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['내얘길들어봐','한여름의크리스마스','쥬뗌므','거짓말도보여요']
        songs2 = ['내얘들','한여름','Je','거짓말도']
        songcount = 4
        embedArray = []

        embed = discord.Embed(title="***Summer Special [내 얘길 들어봐] - 내 얘길 들어봐(A-ing) (Feat. 스컬&하하)***",
        description=str(hearme),
        color=0x00a4e5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200479/20047978.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***Summer Special [내 얘길 들어봐] - 한여름의 크리스마스***",
        description=str(sumxmas),
        color=0x00a4e5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200479/20047978.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***Summer Special [내 얘길 들어봐] - Je T'aime***",
        description=str(taime),
        color=0x00a4e5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200479/20047978.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***Summer Special [내 얘길 들어봐] - 거짓말도 보여요***",
        description=str(sawlie),
        color=0x00a4e5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200479/20047978.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('04_1.txt',encoding='utf-8')
        corl = f.read()
        f.close()

        f = open('04_2.txt',encoding='utf-8')
        rw = f.read()
        f.close()

        f = open('04_3.txt',encoding='utf-8')
        agit = f.read()
        f.close()

        f = open('04_4.txt',encoding='utf-8')
        imd = f.read()
        f.close()

        f = open('04_5.txt',encoding='utf-8')
        pday = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['컬러링북','리얼월드','아지트','인마이드림','퍼펙트데이']
        songs2 = ['Coloring','Real','Agit','In','Perfect']
        songs3 = ['컬북','리얼월드','아지트','인마이드림','퍼펙트데이']
        songs4 = ['coloring','real','agit','in','perfect']
        songcount = 5
        embedArray = []

        embed = discord.Embed(title="***미니 4집 [Coloring Book] - 컬러링북 (Coloring Book)***",
        description=str(corl),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200905/20090525.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 4집 [Coloring Book] - Real World***",
        description=str(rw),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200905/20090525.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 4집 [Coloring Book] - Agit***",
        description=str(agit),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200905/20090525.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 4집 [Coloring Book] - In My Dream***",
        description=str(imd),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200905/20090525.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 4집 [Coloring Book] - Perfect Day***",
        description=str(pday),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/200905/20090525.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs4[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('05_1.txt',encoding='utf-8')
        sregar = f.read()
        f.close()

        f = open('05_2.txt',encoding='utf-8')
        loc = f.read()
        f.close()

        f = open('05_3.txt',encoding='utf-8')
        bfly = f.read()
        f.close()

        f = open('05_4.txt',encoding='utf-8')
        sixt = f.read()
        f.close()

        f = open('05_5.txt',encoding='utf-8')
        magic = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['비밀정원','러브어클락','버터플라이','식스틴','매직']
        songs2 = ['비정','Love','Butterfly','Sixteen','Magic']
        songs3 = ['비정','love','butterfly','sixteen','magic']
        songcount = 5
        embedArray = []

        embed = discord.Embed(title="***미니 5집 [비밀정원] - 비밀정원***",
        description=str(sregar),
        color=0x041f56)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201408/20140893.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 5집 [비밀정원] - Love O'clock***",
        description=str(loc),
        color=0x041f56)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201408/20140893.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 5집 [비밀정원] - Butterfly***",
        description=str(bfly),
        color=0x041f56)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201408/20140893.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 5집 [비밀정원] - Sixteen***",
        description=str(sixt),
        color=0x041f56)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201408/20140893.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 5집 [비밀정원] - Magic***",
        description=str(magic),
        color=0x041f56)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201408/20140893.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('01_b_1.txt',encoding='utf-8')
        bam = f.read()
        f.close()

        f = open('01_b_2.txt',encoding='utf-8')
        why = f.read()
        f.close()

        f = open('01_b_3.txt',encoding='utf-8')
        idl = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['바나나알러지원숭이','하더라','반한게아냐']
        songs2 = ['바알원','하더라','반한게아냐']
        songcount = 3
        embedArray = []

        embed = discord.Embed(title="***유닛 1집 [바나나 알러지 원숭이] - 바나나 알러지 원숭이***",
        description=str(bam),
        color=0xfabcd5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201573/20157333.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***유닛 1집 [바나나 알러지 원숭이] - 하더라***",
        description=str(why),
        color=0xfabcd5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201573/20157333.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***유닛 1집 [바나나 알러지 원숭이] - 반한 게 아냐***",
        description=str(idl),
        color=0xfabcd5)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201573/20157333.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('06_1.txt',encoding='utf-8')
        rmb = f.read()
        f.close()

        f = open('06_2.txt',encoding='utf-8')
        meari = f.read()
        f.close()

        f = open('06_3.txt',encoding='utf-8')
        twi = f.read()
        f.close()

        f = open('06_4.txt',encoding='utf-8')
        ill = f.read()
        f.close()

        f = open('06_5.txt',encoding='utf-8')
        west = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['불꽃놀이','메아리','트와일라잇','일루젼','우리이야기']
        songs2 = ['불놀','메아리','Twilight','Illusion','우리']
        songs3 = ['불놀','메아리','twilight','illusion','우리']
        songcount = 5
        embedArray = []

        embed = discord.Embed(title="***미니 6집 [Remember Me] - 불꽃놀이 (Remember me)***",
        description=str(rmb),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201932/20193267.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 6집 [Remember Me] - 메아리***",
        description=str(meari),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201932/20193267.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 6집 [Remember Me] - Twilight***",
        description=str(twi),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201932/20193267.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 6집 [Remember Me] - Illusion***",
        description=str(ill),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201932/20193267.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 6집 [Remember Me] - 우리 이야기***",
        description=str(west),
        color=0xEE2329)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/201932/20193267.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('01_a_1.txt',encoding='utf-8')
        ssfwl = f.read()
        f.close()

        f = open('01_a_2.txt',encoding='utf-8')
        rain = f.read()
        f.close()

        f = open('01_a_3.txt',encoding='utf-8')
        mije = f.read()
        f.close()

        f = open('01_a_4.txt',encoding='utf-8')
        tictoc = f.read()
        f.close()

        f = open('01_a_5.txt',encoding='utf-8')
        grav= f.read()
        f.close()

        f = open('01_a_6.txt',encoding='utf-8')
        crsc = f.read()
        f.close()

        f = open('01_a_7.txt',encoding='utf-8')
        simhae = f.read()
        f.close()

        f = open('01_a_8.txt',encoding='utf-8')
        vogue = f.read()
        f.close()

        f = open('01_a_9.txt',encoding='utf-8')
        mate = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['다섯번째계절','소나기','미제','틱톡','유성','크라임씬','심해','보그','체크메이트']
        songs2 = ['다계절','소나기','미제','Tic','Gravity','Crime','심해','Vogue','Checkmate']
        songs3 = ['다계절','소나기','미제','tic','gravity','crime','심해','vogue','checkmate']
        songcount = 9
        embedArray = []

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - 다섯 번째 계절 (SSFWL)***",
        description=str(ssfwl),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - 소나기***",
        description=str(rain),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - 미제 (Case No.L5VE)***",
        description=str(mije),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - Tic Toc***",
        description=str(tictoc),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - 유성 (Gravity)***",
        description=str(grav),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - Crime Scene***",
        description=str(crsc),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - 심해 (마음이라는 바다)***",
        description=str(simhae),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - Vogue***",
        description=str(vogue),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***정규 1집 [The Fifth Season] - Checkmate***",
        description=str(mate),
        color=0xC0D84D)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202519/20251998.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('00_ssr_1.txt',encoding='utf-8')
        bungee = f.read()
        f.close()

        f = open('00_ssr_2.txt',encoding='utf-8')
        tropl = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['번지','트로피컬러브']
        songs2 = ['BUNGEE','Tropical']
        songs3 = ['bungee','tropical']
        songcount = 2
        embedArray = []

        embed = discord.Embed(title="***Summer Special RE [Fall In Love] - BUNGEE (Fall in Love)***",
        description=str(bungee),
        color=0x8fe1ef)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202696/20269643.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***Summer Special RE [Fall In Love] - Tropical Love***",
        description=str(tropl),
        color=0x8fe1ef)
        embed.set_image(url="http://image.bugsm.co.kr/album/images/1000/202696/20269643.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('07_1.txt',encoding='utf-8')
        nonstop = f.read()
        f.close()

        f = open('07_2.txt',encoding='utf-8')
        dolphin = f.read()
        f.close()

        f = open('07_3.txt',encoding='utf-8')
        flower = f.read()
        f.close()

        f = open('07_4.txt',encoding='utf-8')
        neon = f.read()
        f.close()

        f = open('07_5.txt',encoding='utf-8')
        krystal = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['살짝설렜어','돌핀','꽃차','네온','크리스탈']
        songs2 = ['NONSTOP','Dolphin','Flower','NEON','Kristal']
        songs3 = ['nonstop','dolphin','flower','neon','krystal']
        songcount = 5
        embedArray = []

        embed = discord.Embed(title="***미니 7집 [NONSTOP] - 살짝 설렜어 (Nonstop)***",
        description=str(nonstop),
        color=0x2f9d27)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/141168/14116820.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 7집 [NONSTOP] - Dolphin***",
        description=str(dolphin),
        color=0x2f9d27)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/141168/14116820.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 7집 [NONSTOP] - 꽃차 (Flower Tea)***",
        description=str(flower),
        color=0x2f9d27)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/141168/14116820.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 7집 [NONSTOP] - NE♡N***",
        description=str(neon),
        color=0x2f9d27)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/141168/14116820.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***미니 7집 [NONSTOP] - Krystal***",
        description=str(krystal),
        color=0x2f9d27)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/141168/14116820.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs2[i]:
                await message.channel.send(embed=embedArray[i])
                break
            if lyr == songs3[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('00_tt_1.txt',encoding='utf-8')
        guerilla = f.read()
        f.close()

        f = open('00_tt_2.txt',encoding='utf-8')
        earhi = f.read()
        f.close()

        f = open('00_tt_3.txt',encoding='utf-8')
        sulbal = f.read()
        f.close()

        f = open('00_tt_4.txt',encoding='utf-8')
        lovesokdo = f.read()
        f.close()

        f = open('00_tt_5.txt',encoding='utf-8')
        sarr = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['게릴라','너의','설레는','사랑속도','사르르']
        songcount = 5
        embedArray = []

        embed = discord.Embed(title="***컴백전쟁 퀸덤 - 게릴라 (Guerilla)***",
        description=str(guerilla),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/202845/20284513.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***혼술남녀 OST - 너의 귓가에 안녕***",
        description=str(earhi),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/200572/20057258.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***으라차차 와이키키 OST - 설레는 발걸음 - 승희***",
        description=str(sulbal),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/7186/718612.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***사랑 속도 - with 유재환***",
        description=str(lovesokdo),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/202445/20244548.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***추리의 여왕2 OST - 사르르 (Sarr) - 효정***",
        description=str(sarr),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/202445/20244548.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break
    
    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('00_tt_6.txt',encoding='utf-8')
        youare = f.read()
        f.close()

        f = open('00_tt_7.txt',encoding='utf-8')
        autumn = f.read()
        f.close()

        f = open('00_tt_8.txt',encoding='utf-8')
        todaytomo = f.read()
        f.close()

        f = open('00_tt_9.txt',encoding='utf-8')
        lovesong = f.read()
        f.close()

        f = open('00_tt_10.txt',encoding='utf-8')
        mafrn = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['you','어느새','오늘도','슈가맨','Ma']

        songcount = 5
        embedArray = []

        embed = discord.Embed(title="***사랑의 온도 OST - You Are - 승희***",
        description=str(youare),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/201207/20120751.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***판타스틱 OST - 어느새 가을 - 효정 with 크루셜스타***",
        description=str(autumn),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/200570/20057096.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***하이애나 OST - 오늘도 어제처럼 - 효정***",
        description=str(todaytomo),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/203134/20313494.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***슈가맨2 - Love Song***",
        description=str(lovesong),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/201509/20150909.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***신비 아파트 OST - Ma Friends***",
        description=str(mafrn),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/200606/20060652.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break

    if message.content.startswith(";가사") or message.content.startswith(";lyric") or message.content.startswith(";l"):

        f = open('00_tt_11.txt',encoding='utf-8')
        morcall = f.read()
        f.close()

        f = open('00_tt_12.txt',encoding='utf-8')
        sweet = f.read()
        f.close()

        f = open('00_tt_13.txt',encoding='utf-8')
        who = f.read()
        f.close()

        f = open('00_tt_14.txt',encoding='utf-8')
        timing = f.read()
        f.close()

        f = open('00_tt_15.txt',encoding='utf-8')
        wonder = f.read()
        f.close()

        f = open('00_tt_16.txt',encoding='utf-8')
        sns = f.read()
        f.close()

        f = open('00_tt_17.txt',encoding='utf-8')
        sunny = f.read()
        f.close()

        lyr = message.content.split(" ")[1]
        songs = ['모닝콜','sweet','who','타이밍','mr','sns','sunny']

        songcount = 7
        embedArray = []

        embed = discord.Embed(title="***모닝콜 - 유아***",
        description=str(morcall),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/201642/20164204.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***일단 뜨겁게 청소하라 - Sweet Heart - 오마이걸 반하나***",
        description=str(sweet),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/8236/823614.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***러블리 호러블리 OST - WHO - 승희***",
        description=str(who),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/201877/20187782.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***타이밍(Timing) - with B1A4 and ONF***",
        description=str(timing),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/202144/20214457.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***리갈하이 OST - Mr. Wonder - 효정, 비니***",
        description=str(wonder),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/202374/20237495.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***SNS - 효정 with 박명수***",
        description=str(sns),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/202066/20206678.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        embed = discord.Embed(title="***사이코메트리 그녀석 OST - Sunny Day - 승희***",
        description=str(sunny),
        color=col)
        embed.set_image(url="https://image.bugsm.co.kr/album/images/1000/202448/20244865.jpg")
        embed.set_footer(text = "그대의 기적과 우리의 옴걸")
        embedArray.append(embed)

        for i in range(0 , songcount):
            if lyr == songs[i]:
                await message.channel.send(embed=embedArray[i])
                break

#######################################################################################

#melon_chart

    if message.content.startswith(';멜론') or message.content.startswith(';melon'):  

        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        melon = requests.get('https://www.melon.com/chart/index.htm', headers = header)
        melon_html = melon.text
        melon_parse= BeautifulSoup(melon_html, 'html.parser')

        mtitles = melon_parse.find_all("div", {"class": "ellipsis rank01"})
        msongs = melon_parse.find_all("div", {"class": "ellipsis rank02"})

        mtitle = []
        msong = []

        for t in mtitles:
            mtitle.append(t.find('a').text)
 
        for s in msongs:
            msong.append(s.find('a').text)

        embed = discord.Embed(
            title='멜론 차트',
            description='TOP 20',
            color=0x00CC33
        )

        for i in range(20):
            embed.add_field(name = str(i+1)+'위', value = '%s - `%s`'%(mtitle[i], msong[i]), inline=False)

        await message.channel.send(embed=embed)

#######################################################################################

#bugs_chart

    if message.content.startswith(';벅스')  or message.content.startswith(';bugs'):
        
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        bugs = requests.get('https://music.bugs.co.kr/chart', headers = header)
        bugs_html = bugs.text
        bugs_parse = BeautifulSoup(bugs_html, 'html.parser')

        btitles = bugs_parse.find_all("p", {"class": "title"})
        bsongs = bugs_parse.find_all("p", {"class": "artist"})

        btitle = []
        bsong = []

        for t in btitles:
            btitle.append(t.find('a').text)
 
        for s in bsongs:
            bsong.append(s.find('a').text)

        embed = discord.Embed(
            title='벅스 차트',
            description='TOP 20',
            color=0xF94232
        )

        for i in range(20):
            embed.add_field(name = str(i+1)+'위', value = '%s - `%s`'%(btitle[i], bsong[i]), inline=False)

        await message.channel.send(embed=embed)

#######################################################################################

#genie_chart

    if message.content.startswith(';지니')  or message.content.startswith(';genie'):
        
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        genie = requests.get('https://www.genie.co.kr/chart/top200', headers = header)
        genie_html = genie.text
        genie_parse = BeautifulSoup(genie_html, 'html.parser')

        gtitles = genie_parse.find_all("a", {"class": "title ellipsis"})
        gsongs = genie_parse.find_all("td", {"class": "info"})

        gtitle = []
        gsong = []

        for t in gtitles:
            gtitle.append(t.text)
 
        for s in gsongs:
            gsong.append(s.find("a", {"class": "artist ellipsis"}).text)

        embed = discord.Embed(
            title='지니 차트',
            description='TOP 20',
            color=0x21B5E6
        )

        for i in range(20):
            embed.add_field(name = str(i+1)+'위', value = '%s - `%s`'%(gtitle[i], gsong[i]), inline=False)

        await message.channel.send(embed=embed)

#######################################################################################

#######################################################################################

#######################################################################################

client.run(access_token)
