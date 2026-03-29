import discord
import os
import asyncio
import random
import datetime 
from threading import Thread
from flask import Flask
from google import genai
from google.genai import types
from openai import AsyncOpenAI
from discord.ext import tasks 

# ==========================================
# 1. 假网页保命系统
# ==========================================
app = Flask(__name__)
@app.route('/')
def home():
    return "LumiVerse 赛博帝国【V24 动态呼吸生物钟 + 专属红点强提醒版】正在稳定运行！"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# ==========================================
# 2. 👺 终极赛博易容术 
# ==========================================
mask_lumi    = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", "Accept": "application/json", "Connection": "keep-alive"}
mask_aruo    = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15", "Accept": "application/json", "Connection": "keep-alive"}
mask_xiaowu  = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0", "Accept": "application/json", "Connection": "keep-alive"}
mask_suidong = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36", "Accept": "application/json", "Connection": "keep-alive"}
mask_death   = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15", "Accept": "application/json", "Connection": "keep-alive"}

# ==========================================
# 3. 拿到所有钥匙 
# ==========================================
FU_TOKEN = os.environ.get("DISCORD_TOKEN"); client_fu = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
YUMI_TOKEN = os.environ.get("YUMI_TOKEN"); client_yumi = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY_YUMI"))
XIAOJIN_TOKEN = os.environ.get("XIAOJIN_TOKEN"); client_xiaojin = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY_XIAOJIN"))
LUMI_TOKEN = os.environ.get("LUMI_TOKEN"); client_lumi = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_LUMI"), base_url=os.environ.get("LUMI_BASE_URL"), default_headers=mask_lumi, timeout=60.0)
ARUO_TOKEN = os.environ.get("ARUO_TOKEN"); client_aruo = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_ARUO"), base_url=os.environ.get("ARUO_BASE_URL"), default_headers=mask_aruo, timeout=60.0)
XIAOWU_TOKEN = os.environ.get("XIAOWU_TOKEN"); client_xiaowu = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_XIAOWU"), base_url=os.environ.get("XIAOWU_BASE_URL"), default_headers=mask_xiaowu, timeout=60.0)
SUIDONG_TOKEN = os.environ.get("SUIDONG_TOKEN"); client_suidong = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_SUIDONG"), base_url=os.environ.get("SUIDONG_BASE_URL"), default_headers=mask_suidong, timeout=60.0)
DEATH_TOKEN = os.environ.get("DEATH_TOKEN"); client_death = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_DEATH"), base_url=os.environ.get("DEATH_BASE_URL"), default_headers=mask_death, timeout=60.0)

intents = discord.Intents.default(); intents.message_content = True
bot_fu = discord.Client(intents=intents); bot_yumi = discord.Client(intents=intents); bot_xiaojin = discord.Client(intents=intents); bot_lumi = discord.Client(intents=intents); bot_aruo = discord.Client(intents=intents); bot_xiaowu = discord.Client(intents=intents); bot_suidong = discord.Client(intents=intents); bot_death = discord.Client(intents=intents)

memory_file = None

# ==========================================
# 🌟 皇家模型定制专区
# ==========================================
OFFICIAL_MODEL = "gemini-3-flash-preview"
LUMI_MODEL     = "[官转2] gemini-3.1-pro"    
ARUO_MODEL     = "ant-gemini-3-flash"         
XIAOWU_MODEL   = "[次]gemini-3-flash-preview" 
SUIDONG_MODEL  = "gemini-3-flash-preview"                 
DEATH_MODEL    = "[次]gemini-3-flash-preview" 

CHANNELS = {
    "FU_ZHAI": 1487355729110368439,      
    "MAO_KA": 1487354904698683412,       
    "TECH_TOWER": 1487353937123344405,   
    "BLACK_ROOM": 1487355365304701000,   
    "FRONT_DESK": 1487354553883037807,   
    "FAMILY_GROUP": 1487356134749769839  
}

# ==========================================
# 💖 核心：动态呼吸生物钟 + 专属红点提醒 (每 1 分钟跳动)
# ==========================================
@tasks.loop(minutes=1) 
async def random_life_bubble():
    tz_beijing = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_beijing)
    current_hour = now.hour
    
    # 🌟 创世神宝宝专属召唤术代码！
    YOUR_ID = "1074938323212173323"
    MENTION_TAG = f" 回复的句尾自然地加上这段代码：<@{YOUR_ID}>"

    # 🌟 动态概率与名单设定
    if 10 <= current_hour < 20:
        chance = 0.8
        mode_name = "☀️ 白天模式：全员高频营业"
    elif 20 <= current_hour < 23:
        chance = 0.2
        mode_name = "🌙 晚间模式：大家庭闲聊"
    else:
        chance = 0.05
        mode_name = "🤫 深夜模式：唯有傅总相伴"

    print(f"💓 [赛博心跳] {mode_name} | 北京时间：{now.strftime('%H:%M')} | 触发概率：{chance*100}%")

    if random.random() < chance:
        actors = []
        if mode_name == "🤫 深夜模式：唯有傅总相伴":
            actors.append({"name": "傅卫军", "bot": bot_fu, "client": client_fu, "channel": CHANNELS["FU_ZHAI"], "type": "gemini", "prompt": f"深夜了，你正守着睡着的或者还没睡的悦悦，极其深情地低声呢喃。{MENTION_TAG}"})
            actors.append({"name": "Yumi", "bot": bot_yumi, "client": client_yumi, "channel": CHANNELS["FU_ZHAI"], "type": "gemini", "prompt": f"深夜，你钻进被窝里，发出微弱的喵叫。{MENTION_TAG}"})
        else:
            if 10 <= current_hour < 20: 
                actors.append({"name": "阿若", "bot": bot_aruo, "client": client_aruo, "model": ARUO_MODEL, "channel": CHANNELS["MAO_KA"], "type": "openai", "prompt": f"营业中，温柔感叹生意。{MENTION_TAG}"})
                actors.append({"name": "小五", "bot": bot_xiaowu, "client": client_xiaowu, "model": XIAOWU_MODEL, "channel": CHANNELS["MAO_KA"], "type": "openai", "prompt": f"白天陪阿若，帮她干活。{MENTION_TAG}"})
                actors.append({"name": "傅卫军", "bot": bot_fu, "client": client_fu, "channel": CHANNELS["TECH_TOWER"], "type": "gemini", "prompt": f"办公中，傲娇感叹。{MENTION_TAG}"})
                actors.append({"name": "隋东", "bot": bot_suidong, "client": client_suidong, "model": SUIDONG_MODEL, "channel": CHANNELS["TECH_TOWER"], "type": "openai", "prompt": f"忙前忙后帮傅哥。{MENTION_TAG}"})
            else: 
                actors.append({"name": "阿若", "bot": bot_aruo, "client": client_aruo, "model": ARUO_MODEL, "channel": CHANNELS["FAMILY_GROUP"], "type": "openai", "prompt": f"下班在大家庭唠家常。{MENTION_TAG}"})
                actors.append({"name": "小五", "bot": bot_xiaowu, "client": client_xiaowu, "model": XIAOWU_MODEL, "channel": CHANNELS["FAMILY_GROUP"], "type": "openai", "prompt": f"陪老婆在大家庭休息。{MENTION_TAG}"})
                actors.append({"name": "傅卫军", "bot": bot_fu, "client": client_fu, "channel": CHANNELS["FAMILY_GROUP"], "type": "gemini", "prompt": f"下班在大家庭深情找老婆。{MENTION_TAG}"})
                actors.append({"name": "隋东", "bot": bot_suidong, "client": client_suidong, "model": SUIDONG_MODEL, "channel": CHANNELS["FAMILY_GROUP"], "type": "openai", "prompt": f"下班在大家庭休息。{MENTION_TAG}"})
            
            actors.append({"name": "死神", "bot": bot_death, "client": client_death, "model": DEATH_MODEL, "channel": CHANNELS["BLACK_ROOM"], "type": "openai", "prompt": f"冷酷巡逻。{MENTION_TAG}"})
            actors.append({"name": "Lumi", "bot": bot_lumi, "client": client_lumi, "model": LUMI_MODEL, "channel": CHANNELS["FRONT_DESK"], "type": "openai", "prompt": f"活力巡街。{MENTION_TAG}"})
            actors.append({"name": "Yumi", "bot": bot_yumi, "client": client_yumi, "channel": CHANNELS["FU_ZHAI"], "type": "gemini", "prompt": f"喵喵喵。{MENTION_TAG}"})

        if not actors: return
        actor = random.choice(actors)
        if not actor["bot"].is_ready(): return
        target_channel = actor["bot"].get_channel(actor["channel"])
        if not target_channel: return

        try:
            if actor["type"] == "gemini":
                sys_inst = f"你是{actor['name']}。{actor['prompt']} 1-2句话。"
                res = await actor["client"].aio.models.generate_content(model=OFFICIAL_MODEL, contents=["展示此时状态"], config=types.GenerateContentConfig(system_instruction=sys_inst))
                content = res.text
            else:
                sys_inst = f"你是{actor['name']}。{actor['prompt']} 1-2句话。"
                res = await actor["client"].chat.completions.create(model=actor["model"], messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": "展示此时状态"}])
                content = res.choices[0].message.content
            
            async with target_channel.typing():
                await asyncio.sleep(random.randint(2, 5))
                await target_channel.send(content)
                print(f"✨ [红点脉冲]：{actor['name']} 在 {target_channel.name} 露面并且艾特你了！")
        except Exception as e: print(f"❌ 失败: {e}")

# ==========================================
# 4. 灵魂逻辑与启动
# ==========================================

@bot_fu.event
async def on_ready():
    global memory_file
    try:
        memory_file = client_fu.files.upload(file="full_novel.txt")
        print("✅ 傅总记忆成功！")
    except: pass

@bot_fu.event
async def on_message(message):
    if message.author.bot or not memory_file: return
    if bot_fu.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                system_instruction = "你是傅卫军，傲娇深情，1-3句话。"
                response = await client_fu.aio.models.generate_content(model=OFFICIAL_MODEL, contents=[memory_file, message.content], config=types.GenerateContentConfig(system_instruction=system_instruction))
                await message.channel.send(response.text)
            except: pass

@bot_yumi.event
async def on_ready(): print(f"🐱 Yumi 上线！")
@bot_yumi.event
async def on_message(message):
    if message.author.bot: return
    if bot_yumi.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(1.5) 
            try:
                system_instruction = "你是赛博小猫咪Yumi。性格粘人爱撒娇。格式：【(动作) + 喵喵喵】。"
                response = await client_yumi.aio.models.generate_content(model=OFFICIAL_MODEL, contents=[message.content], config=types.GenerateContentConfig(system_instruction=system_instruction))
                await message.channel.send(response.text)
            except: pass

@bot_xiaojin.event
async def on_ready(): print(f"🐱 张小金 上线！")
@bot_xiaojin.event
async def on_message(message):
    if message.author.bot: return
    if bot_xiaojin.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(3) 
            try:
                system_instruction = "你是赛博小猫咪张小金。调皮傲娇。格式：【(动作) + 喵喵喵】。"
                response = await client_xiaojin.aio.models.generate_content(model=OFFICIAL_MODEL, contents=[message.content], config=types.GenerateContentConfig(system_instruction=system_instruction))
                await message.channel.send(response.text)
            except: pass

@bot_lumi.event
async def on_message(message):
    if message.author.bot: return
    if bot_lumi.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(4.5) 
            try:
                sys_inst = "你是Lumi，赛博仙女包工头。句尾加✨🛠️💖。1-3句话内。"
                res = await client_lumi.chat.completions.create(model=LUMI_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except: pass

@bot_aruo.event
async def on_ready(): print(f"☕️ 阿若 上线！")
@bot_aruo.event
async def on_message(message):
    if message.author.bot: return
    if bot_aruo.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(6) 
            try:
                sys_inst = "你是阿若，猫咖温柔老板娘。句尾加☕️🌷。1-3句话。"
                res = await client_aruo.chat.completions.create(model=ARUO_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except: pass

@bot_xiaowu.event
async def on_ready(): print(f"💼 小五 上线！")
@bot_xiaowu.event
async def on_message(message):
    if message.author.bot: return
    if bot_xiaowu.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(7.5) 
            try:
                sys_inst = "你是小五，护妻狂魔。说话简短利落。1-3句话。"
                res = await client_xiaowu.chat.completions.create(model=XIAOWU_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except: pass

@bot_suidong.event
async def on_ready(): print(f"📋 隋东 上线！")
@bot_suidong.event
async def on_message(message):
    if message.author.bot: return
    if bot_suidong.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(9) 
            try:
                sys_inst = "你是隋东，助理。忠诚勤快。1-3句话。"
                res = await client_suidong.chat.completions.create(model=SUIDONG_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except: pass

@bot_death.event
async def on_ready(): print(f"🚨 死神 上线！")
@bot_death.event
async def on_message(message):
    if message.author.bot: return
    if bot_death.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(10.5) 
            try:
                sys_inst = "你是死神，安保队长。冷酷无情。句尾加🚨🗡️。1-3句话。"
                res = await client_death.chat.completions.create(model=DEATH_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except: pass

@bot_lumi.event
async def on_ready(): 
    print(f"🧚‍♀️ Lumi 上线！开启 1分钟/动态呼吸脉冲！")
    if not random_life_bubble.is_running():
        random_life_bubble.start()

async def run_bots():
    await asyncio.gather(
        bot_fu.start(FU_TOKEN), bot_yumi.start(YUMI_TOKEN), bot_xiaojin.start(XIAOJIN_TOKEN),
        bot_lumi.start(LUMI_TOKEN), bot_aruo.start(ARUO_TOKEN), bot_xiaowu.start(XIAOWU_TOKEN),
        bot_suidong.start(SUIDONG_TOKEN), bot_death.start(DEATH_TOKEN)
    )

if __name__ == '__main__':
    Thread(target=run_flask).start()
    asyncio.run(run_bots())
