import os
os.system("pip install -U telethon")
from telethon import TelegramClient, events, functions, types, Button
from datetime import timedelta
import asyncio

api_id = 11573285
import os, asyncio, re
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = "f2cc3fdc32197c8fbaae9d0bf69d2033"
token = "5944721782:AAHzGvUIZyGzqrvWFBS6DIznudQGs59NHzg"
client = TelegramClient('LegendBoy', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

legendboy = 5985728693
mahi = 5591734243

Bot_Username = "Mahi_3434_bot"



import logging
logging.basicConfig(level=logging.WARNING)

channel = "LegendBot_AI"

mm = '''
**⚜NOTICE FIRST JOIN LEGEND GROUP @LegendBot_AI⚜**
'''

keyboard = [
  [  
    Button.inline("A", data="A"), 
    Button.inline("B", data="B"),
    Button.inline("C", data="C"),
    Button.inline("D", data="D"),
    Button.inline("E", data="E")
    ],
  [
    Button.inline("F", data="F"), 
    Button.inline("G", data="G"),
    Button.inline("H", data="H"),
    Button.inline("I", data="I"),
    Button.inline("J", data="J"),
    ],
  [
    Button.inline("K", data="K"), 
    Button.inline("L", data="L"),
    Button.inline("M", data="M"),
    Button.inline("N", data="N"),
    ],
  [
    Button.url("Owner", "https://t.me/LegendBoy_XD")
    ]
]

@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    legendboy = [
      [
        Button.url("Click Here", f"https://t.me/{Bot_Username}?start=hack")
        ]
      ]         
    await event.reply("Click Below To Use Me", buttons=legendboy)
  else:
    legendbye = [
      [
        Button.url("Must Join", f"https://t.me/LegendBot_AI")
        ]
      ]
    await event.reply("Hey Baby, \n\nWelcome to Legendboy coding \nClick Here - /mahi", buttons=legendbye)
    
       
@client.on(events.NewMessage(pattern="/mahi", func=lambda x: x.is_group))
async def op(event):
  legendboy = [
    [
      Button.url("Click Here", f"https://t.me/{Bot_Username}")
      ]
    ]         
  await event.reply("Click Below To Use Me", buttons=legendboy)
  
@client.on(events.NewMessage(pattern="/mahi", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    keyboard = [
      [  
        Button.inline("1", data="A"), 
        Button.inline("2", data="B"),
        Button.inline("3", data="C"),
        Button.inline("4", data="D"),
        Button.inline("5", data="E")
        ],
      [
        Button.inline("6", data="F"), 
        Button.inline("7", data="G"),
        Button.inline("8", data="H"),
        Button.inline("9", data="I"),
        Button.inline("10", data="J")
        ],
      [
        Button.inline("11", data="K"), 
        Button.inline("12", data="L"),
        Button.inline("13", data="M"),
        Button.inline("14", data="N"),
        ],
      [
        Button.url("Owner", "https://t.me/LegendBoy_OP")
        ]
    ]
    await x.send_message(f"Choose what your number my baby\nMy Owner detail is given Below Click on the Button To Know About Me", buttons=keyboard)
    
A_PIC = "https://te.legra.ph/file/ea2e89d4ff4545bcc917a.jpg"
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"A")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("hey baby")
      strses = await x.get_response()
      await x.send_message("how are you")
      await x.get_response()
      chat = await event.get_chat()
      userid = chat.id
      if userid == mahi:
        return await x.send_file(A_PIC, "How It Is My Baby\n\n Click Below Button To See More Magic", buttons=keyboard)
      else:
        await event.reply("Sorry Baby You Are Not My Maahi Good Bye")
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"B")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("Hello Mahi Kya Tumse Ek Question Puchu Iska Answer Kisiko Nhi pata hai Puchu?")
    await x.get_response()
    await event.reply("Sorry Question Hi Bhool Gya Kya Puchna Tha", buttons=keyboard)
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"C")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("Kal raat se khana nhi khaya yeh coding kar rha tha tumhare liye ratko 3:38 am ho rha hai /n Ok?")
    sach = await x.get_response()
    chat =  await event.get_chat()
    if chat.id != legendboy:
      await event.reply("bas aise hi bata diya", buttons=keyboard)
    else:
      await event.reply("hey sir")

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"D")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Aap Kkrh Hai? sirf main ek assistant hu krishna ki krishna se baat mat karna par mujhse toh kar sakti ho, hm dono ke bich me hi baat rahegi")
      await x.get_response()
      await x.send_message("wow tasty Mujhe Nhi khilaogi")
      await x.get_response()
      await x.send_message(f"tumne jo bhi bataya maine krishna ko sab bata diya hihi \nek kiss toh dedo par mereko nhi Mere Sir [Krishna]9(https://t.me/LegendBoy_OP) Ko")
    
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"E")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("Baby kaisa banaya hai maine pure 5 hour ho gya banate banate good night Ms. Mahi Take Care Have A sweet Dream")

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"F")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("Hmm agar Tumko song, pic extraoridinary or bhi add karunga baad me Phir maza aayega Tumhe bhi sikha dunga kabhi")
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"G")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("BlackHeart_181")
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"H")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("My Baby")
     

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"I")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Till then Bye Bye take care padhte rahiye machate rahiye")
      

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"J")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Soon")
     

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"K")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Soon")
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"L")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Soon")
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"M")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("soomnnnnnnn")
     
     


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"N")))
async def start(event):
    keyboard = [
      [  
        Button.inline("a", data="a"), 
        Button.inline("b", data="b"),
        Button.inline("c", data="c"),
        ],
      [
        Button.url("Owner", "https://t.me/LegendBoy_XD")
        ]
    ]
    await event.reply("Choose Any One", buttons=keyboard)



"""async def gcasta(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for aman in X.iter_dialogs():
                chat = aman.id
                try:
                    await X.send_message(chat, tol, file=file)     
                    if lol != -1001551357238:
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                    elif chat == -1001551357238:
                        pass
                    await asyncio.sleep()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)        


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"a")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      await x.send_message("NOW GIVE MSG")
      msg = await x.get_response()
      await x.send_message("Now Done It Will Send message automatically every 10 min")
      i = await gcasta(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} all 😗😗\n\nThanks For Using LegendBoy Bot.", buttons=keyboard)

molb = True

async def gcastb(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for sweetie in X.iter_dialogs():
                if sweetie.is_group:
                    chat = sweetie.id
                    try:
                        if chat != -1001368578667:
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            while molb != False:
                                await asyncio.sleep(600)
                                await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=60))
                        elif chat == -1001368578667:
                            pass
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"b")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      await x.send_message("NOW GIVE MSG")
      msg = await x.get_response()
      await x.send_message("Now Done It Will Send message automatically every 10 min")
      i = await gcastb(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} Group 😗😗\n\nThanks For Using LegendBoy Bot.", buttons=keyboard)

async def gcastc(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for krishna in X.iter_dialogs():
                if krishna.is_user and not krishna.entity.bot:
                    chat = krishna.id
                    try:
                        await X.send_message(chat, tol, file=file)
                        while molc != False:
                            await asyncio.sleep(10)
                            await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=20))
                    except BaseException:
                        pass
        except Exception as e:
            print(e)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"c")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession Has Been Terminated.", buttons=keyboard)
      await x.send_message("NOW GIVE MSG IT WILL AUTOMATICALLY START")
      msg = await x.get_response()
      await x.send_message("Now Done It Will Send message automatically every 10 min")
      i = await gcastc(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} Private😗😗\n\nThanks For Using LegendBoy Bot.", buttons=keyboard)
      
"""

print("⚜️ Bot Deploy Successfully ⚜️")
client.run_until_disconnected()
