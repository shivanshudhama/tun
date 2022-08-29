#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE


import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
from subprocess import getstatusoutput
import logging
import os
import sys
import re
import cloudscraper
from bs4 import BeautifulSoup
from config import Config
cancel = False
bot = Client(
    "bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)
@bot.on_message(filters.command(["start"]))
async def start(bot, update):
       await update.reply_text("Hi i am **Cw TxT Maker Bot**.\n\n"
                              "**NOW:-** "
                                       
                              "Press **/cw** to continue..\n\n" 
                              #"Press **/txt** to Download Videos from txt made by CW..\n\n"       
                              "**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 𝗕𝗹𝗮𝗰𝗸𝗢𝘂𝗧 (•̪●)=︻╦̵̵̿╤── **")

ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd"
bc_url = (f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos")
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

@bot.on_message(filters.command(["cw"])& ~filters.edited)
async def account_login(bot: Client, m: Message):
    global cancel
    cancel = False
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    url = "https://elearn.crwilladmin.com/api/v1/login-other"
    data = {
        "deviceType": "android",
        "password": "",
        "deviceIMEI": "08750aa91d7389ab",
        "deviceModel": "Realme RMX2001",
        "deviceVersion": "",
        "email": "",
        "deviceToken": ""
       }
    headers = {
        "Host": "elearn.crwilladmin.com",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "338",
        "Accept-Encoding": "gzip",
        "user-agent": "okhttp/3.12.12"
       }
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    data["email"] = raw_text.split("*")[0]
    data["password"] = raw_text.split("*")[1]
    await input1.delete(True)

    scraper = cloudscraper.create_scraper()
    html = scraper.post(url,data,headers).content
    output0 = json.loads(html)
    token = output0["data"]["token"]
    #await m.reply_text(soup)
    #token=str(input())
    await editable.edit("**login Successful**")
    #await editable.edit(f"You have these Batches :-\n{raw_text}"
    scraper = cloudscraper.create_scraper()
    html1 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/my-batch?&token=" + token).content
    output = json.loads(html1)
    #print(jsonResponse)
    topicid = output["data"]["batchData"]
    print(topicid)
    
    cool=""
    for data in topicid:
        instructorName=(data["instructorName"])
        FFF="**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa =f" ```{data['id']}```      - **{data['batchName']}**\n{data['instructorName']}\n\n"
        #aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}')>4096:
            await m.reply_text(aa)
            cool =""
        cool+=aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')

    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    
# topic id url = https://elearn.crwilladmin.com/api/v1/comp/batch-topic/881?type=class&token=d76fce74c161a264cf66b972fd0bc820992fe576
    scraper = cloudscraper.create_scraper()
    html2 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/batch-topic/"+raw_text2+"?type=class&token="+token).content
    output1 = json.loads(html2)
    topicid = output1["data"]["batch_topic"]
    bn = output1["data"]["batch_detail"]["name"]
#     await m.reply_text(f'Batch details of **{bn}** are :')
    vj=""
    for data in topicid:
        tids = (data["id"])
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            await m.reply_text(idid)
            vj = ""
        vj+=idid  
    vp = ""
    for data in topicid:
        tn = (data["topicName"])
        tns=f"{tn}&"
        if len(f"{vp}{tn}")>4096:
            await m.reply_text(tns)
            vp=""
        vp+=tns      
    cool1 = ""    
    for data in topicid:
        t_name=(data["topicName"])
        tid = (data["id"])
        scraper = cloudscraper.create_scraper()
        html3 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+tid+"&token="+token).content
        ffx = json.loads(html3)
        vcx =ffx["data"]["class_list"]["batchDescription"]
        vvx =ffx["data"]["class_list"]["classes"]
        vvx.reverse()
        zz= len(vvx)
        BBB = f"{'**TOPIC-ID - TOPIC - VIDEOS**'}"
        hh = f"```{tid}```     - **{t_name} - ({zz})**\n"
        
#         hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"
        
        if len(f'{cool1}{hh}')>4096:
            await m.reply_text(hh)
            cool1=""
        cool1+=hh
    await m.reply_text(f'Batch details of **{bn}** are:\n\n{BBB}\n\n{cool1}\n\n**{vcx}**')
#     await m.reply_text(f'**{vcx}**')
#     await m.reply_text(f'```{vj}```')
    
    editable2= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")    
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    
    editable3= await m.reply_text("**Now send the Resolution**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    
    
#     editable9= await m.reply_text(f"Now send the **Topic Names**\n\nSend like this **1&2&3&4** and so on\nor copy paste or edit **below names according to you in Order of ids you entered above** :\n\n**Enter this to download full batch :-**\n```{vp}```")
    
#     input9 = message = await bot.listen(editable.chat.id)
#     raw_text9 = input9.text
    #link_file_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + "/links.txt"
    #tmp_directory_for_each_user = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id)
  
    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
        
#              xvv = raw_text9.split('&')
#              for z in range(0,len(xvv)):
#                  p =xvv[z]
        
        
            #gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57
            scraper = cloudscraper.create_scraper()
            html4 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+t+"&token="+token).content
            ff = json.loads(html4)
            #vc =ff.json()["data"]["class_list"]["batchDescription"]
            mm = ff["data"]["class_list"]["batchName"]   
            vv =ff["data"]["class_list"]["classes"]
            vv.reverse()
            #clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
            #await m.reply_text(clan)
            count = 1
            try:
                for data in vv:
                    vidid = (data["id"])
                    lessonName = (data["lessonName"]).replace("/", "_")
                    
                    bcvid = (data["lessonUrl"][0]["link"])
                     #lessonName = re.sub('\|', '_', cf)

                    if bcvid.startswith("62"):
                        try:
                            scraper = cloudscraper.create_scraper()
                            html6 = scraper.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video = json.loads(html6)
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            #print(video_url)
                            scraper = cloudscraper.create_scraper()
                            html5 = scraper.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl = json.loads(html5)
                            stoken = surl["data"]["token"]
                            #print(stoken)
                            
                            link = (video_url+"&bcov_auth="+stoken)
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    #cc = (f"{lessonName}:{link}")
                    #await m.reply_text(cc)
                    elif bcvid.startswith("63"):
                        try:
                            scraper = cloudscraper.create_scraper()
                            html7 = scraper.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video1 = json.loads(html7)
                            video_source1 = video1["sources"][5]
                            video_url1 = video_source1["src"]
                            #print(video_url)
                            scraper = cloudscraper.create_scraper()
                            html8 = scraper.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl1 = json.loads(html8)
                            stoken1 = surl1["data"]["token"]
                            #print(stoken)
                            
                            link = (video_url1+"&bcov_auth="+stoken1)
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    #cc = (f"{lessonName}:{link}")
                    #await m.reply_text(cc)
                    else:
                        link=("https://www.youtube.com/embed/"+bcvid)
                    cc = (f"{lessonName}::{link}")
                    with open(f"{mm }{t_name}.txt", 'a') as f:
                        f.write(f"{lessonName}:{link}\n")
                    #await m.reply_document(f"{mm }{t_name}.txt")
            except Exception as e:
                await m.reply_text(str(e))
        await m.reply_document(f"{mm }{t_name}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")


#@bot.on_message(filters.command(["pyro"])& ~filters.edited)
#async def account_login(bot: Client, m: Message):
    #global =cancel
    #cancel = False
    editable = await m.reply_text("**Send Only CW TxT file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text


    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    #editable = await m.reply_text("**Enter Batch Name**")
    #input01: Message = await bot.listen(editable.chat.id)
    #mm = input01.text
    
    await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    #await m.reply_text("**Enter resolution**")
    #input2: Message = await bot.listen(editable.chat.id)
    #raw_text4 = input2.text

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text) 
    try:
        for i in range(arg, len(links)):
            
            url = links[i][1].replace("b'", ":").replace("'", "")
            name = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").replace("b'", ":").replace("'", "").strip()
            Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text4}```\n\n**Url :-** ```{url}```"
            prog = await m.reply_text(Show)
            cc = f"**{count}) Title :** {name}\n\n**Quality :** {raw_text4}\n**Batch :** {mm}\n**𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆 :** {raw_text0}\n**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 𝗕𝗹𝗮𝗰𝗸𝗢𝘂𝗧 (•̪●)=︻╦̵̵̿╤── **"
            #\n**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 𝗕𝗹𝗮𝗰𝗸𝗢𝘂𝗧 (•̪●)=︻╦̵̵̿╤── **\n**𝗣𝗹𝘇 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 : https://www.youtube.com/channel/UC7udfRGdD_QoCg-OnSooGAA**
            if "youtu" in url:
                if raw_text4 in ["144", "240", "480"]:
                    ytf = f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]'
                elif raw_text4 == "360":
                    ytf = 18
                elif raw_text4 == "720":
                    ytf = 22
                else:
                    ytf = 18
            else:
                ytf = f"bestvideo[height<={raw_text4}]"

            if ytf == f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]':
                cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}" "{url}"'
            else:
                cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}+bestaudio" "{url}"'

            # cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                filename = f"{name}.mp4"
                subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -y -vframes 1 "{filename}.jpg"', shell=True)
                await prog.delete (True)
                reply = await m.reply_text("Uploading Video")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))
                dur = int(helper.duration(filename))
                await prog.delete (True)
                start_time = time.time()
                await m.reply_video(f"{name}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))
                count+=1
                os.remove(f"{name}.mp4")
                os.remove(f"{filename}.jpg")
                await reply.delete (True)
                time.sleep(2)
            except Exception as e:
                await m.reply_text(e)
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")    
@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
bot.run()
