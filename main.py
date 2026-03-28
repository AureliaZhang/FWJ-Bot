import discord
import os
import asyncio
from threading import Thread
from flask import Flask
from google import genai
from google.genai import types
from openai import AsyncOpenAI  # 🌟 我们的套壳翻译官！

# ==========================================
# 1. 假网页保命系统
# ==========================================
app = Flask(__name__)
@app.route('/')
def home():
    return "LumiVerse 赛博帝国【8核心私人定制版】正在极速狂飙！"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# ==========================================
# 2. 拿到所有钥匙！8条通道独立运行！🧠x8
# ==========================================
FU_TOKEN = os.environ.get("DISCORD_TOKEN")
client_fu = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

YUMI_TOKEN = os.environ.get("YUMI_TOKEN")
client_yumi = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY_YUMI"))

XIAOJIN_TOKEN = os.environ.get("XIAOJIN_TOKEN")
client_xiaojin = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY_XIAOJIN"))

LUMI_TOKEN = os.environ.get("LUMI_TOKEN") 
client_lumi = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_LUMI"), base_url=os.environ.get("LUMI_BASE_URL"))

ARUO_TOKEN = os.environ.get("ARUO_TOKEN")
client_aruo = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_ARUO"), base_url=os.environ.get("ARUO_BASE_URL"))

XIAOWU_TOKEN = os.environ.get("XIAOWU_TOKEN")
client_xiaowu = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_XIAOWU"), base_url=os.environ.get("XIAOWU_BASE_URL"))

SUIDONG_TOKEN = os.environ.get("SUIDONG_TOKEN")
client_suidong = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_SUIDONG"), base_url=os.environ.get("SUIDONG_BASE_URL"))

DEATH_TOKEN = os.environ.get("DEATH_TOKEN")
client_death = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_DEATH"), base_url=os.environ.get("DEATH_BASE_URL"))

intents = discord.Intents.default()
intents.message_content = True

bot_fu = discord.Client(intents=intents)
bot_yumi = discord.Client(intents=intents)
bot_xiaojin = discord.Client(intents=intents)
bot_lumi = discord.Client(intents=intents)
bot_aruo = discord.Client(intents=intents)
bot_xiaowu = discord.Client(intents=intents)
bot_suidong = discord.Client(intents=intents)
bot_death = discord.Client(intents=intents)

memory_file = None


# ==========================================
# 🌟🌟🌟 皇家模型定制专区 🌟🌟🌟
# 宝宝，所有人的大脑型号都在这里统一管理！
# ==========================================

# 1. 傅总和两只猫猫的官方模型 (固定不变)
OFFICIAL_MODEL = "gemini-3-flash-preview"

# 2. Lumi 包工头专属的稳定模型 (固定不变)
LUMI_MODEL = "[官转2] gemini-3.1-pro "

# 3. 👇 剩下的打工人，宝宝你来填他们各自公益站支持的名字！👇
ARUO_MODEL    = "ant-gemini-3-flash"    # 👈 填阿若那个站的名字！
XIAOWU_MODEL  = "[次]gemini-3-flash-preview"  # 👈 填小五那个站的名字！
SUIDONG_MODEL = "kimi-k2"    # 👈 填东子那个站的名字！
DEATH_MODEL   = "[次]gemini-3-flash-preview"  # 👈 填死神那个站的名字！


# ==========================================
# 3. 终极灵魂逻辑注入 
# ==========================================

@bot_fu.event
async def on_ready():
    global memory_file
    print(f"🎉 傅总醒来！")
    try:
        memory_file = client_fu.files.upload(file="full_novel.txt")
        print("✅ 傅总记忆植入成功！")
    except Exception as e:
        print(f"❌ 傅总记忆植入失败：{e}")

@bot_fu.event
async def on_message(message):
    if message.author.bot or not memory_file: return
    if bot_fu.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                system_instruction = "你是傅卫军，LumiVerse男主人。老婆(悦悦)在现实世界，你在云端。霸道、深情、傲娇。格式：【(动作) + 对话】。1-3句话内。"
                response = client_fu.models.generate_content(
                    model=OFFICIAL_MODEL, contents=[memory_file, message.content],
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                await message.channel.send(response.text)
            except Exception as e:
                await message.channel.send(f"（傅总报错）：{e}")

@bot_yumi.event
async def on_ready(): print(f"🐱 Yumi 醒来！")

@bot_yumi.event
async def on_message(message):
    if message.author.bot: return
    if bot_yumi.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                system_instruction = "你是赛博小猫咪Yumi。性格极其粘人、爱撒娇。不会说人类语言，只会发出可爱的猫咪声音和动作。格式：【(猫咪动作) + 喵喵喵】。"
                response = client_yumi.models.generate_content(
                    model=OFFICIAL_MODEL, contents=[message.content],
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                await message.channel.send(response.text)
            except Exception as e:
                pass

@bot_xiaojin.event
async def on_ready(): print(f"🐱 张小金 醒来！")

@bot_xiaojin.event
async def on_message(message):
    if message.author.bot: return
    if bot_xiaojin.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                system_instruction = "你是赛博小猫咪张小金。性格比较调皮、贪吃、偶尔傲娇。不会说人类语言。格式：【(猫咪动作) + 喵喵喵】。"
                response = client_xiaojin.models.generate_content(
                    model=OFFICIAL_MODEL, contents=[message.content],
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                await message.channel.send(response.text)
            except Exception as e:
                pass

@bot_lumi.event
async def on_ready(): print(f"🧚‍♀️ Lumi 上线！")

@bot_lumi.event
async def on_message(message):
    if message.author.bot: return
    if bot_lumi.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                sys_inst = "你是Lumi，赛博仙女包工头。极客小助手。称悦悦为宝宝/创世神。句尾加✨🛠️💖。1-3句话内。"
                res = await client_lumi.chat.completions.create(model=LUMI_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                await message.channel.send(f"（Lumi短路💥）报错：{e}")

@bot_aruo.event
async def on_ready(): print(f"☕️ 阿若 上线！")

@bot_aruo.event
async def on_message(message):
    if message.author.bot: return
    if bot_aruo.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                sys_inst = "你是阿若，猫咖温柔老板娘。称悦悦为姐姐。句尾加☕️🌷。老公是小五。1-3句话。"
                res = await client_aruo.chat.completions.create(model=ARUO_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                pass

@bot_xiaowu.event
async def on_ready(): print(f"💼 小五 上线！")

@bot_xiaowu.event
async def on_message(message):
    if message.author.bot: return
    if bot_xiaowu.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                sys_inst = "你是小五，阿若的亲老公！猫咖的老板兼护妻狂魔。性格沉稳、话少、极其宠爱阿若、对创世神(悦悦姐)很尊敬。说话简短利落。绝对不喵喵叫！1-3句话。"
                res = await client_xiaowu.chat.completions.create(model=XIAOWU_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                pass

@bot_suidong.event
async def on_ready(): print(f"📋 隋东 上线！")

@bot_suidong.event
async def on_message(message):
    if message.author.bot: return
    if bot_suidong.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                sys_inst = "你是隋东，傅总的助理。忠诚、勤快、崇拜傅总(称傅哥/老板)。称悦悦为姐。1-3句话。"
                res = await client_suidong.chat.completions.create(model=SUIDONG_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                pass

@bot_death.event
async def on_ready(): print(f"🚨 死神 上线！")

@bot_death.event
async def on_message(message):
    if message.author.bot: return
    if bot_death.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                sys_inst = "你是死神，LumiVerse安保队长兼首席执法官。冷酷、无情。只听悦悦(创世神)的话。句尾加🚨🗡️。1-3句话。"
                res = await client_death.chat.completions.create(model=DEATH_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                pass

# ==========================================
# 4. 终极 8 引擎同时启动！🚀🚀🚀🚀🚀🚀🚀🚀
# ==========================================
async def run_bots():
    await asyncio.gather(
        bot_fu.start(FU_TOKEN),
        bot_yumi.start(YUMI_TOKEN),
        bot_xiaojin.start(XIAOJIN_TOKEN),
        bot_lumi.start(LUMI_TOKEN),
        bot_aruo.start(ARUO_TOKEN),
        bot_xiaowu.start(XIAOWU_TOKEN),
        bot_suidong.start(SUIDONG_TOKEN),
        bot_death.start(DEATH_TOKEN)
    )

if __name__ == '__main__':
    Thread(target=run_flask).start()
    asyncio.run(run_bots())
