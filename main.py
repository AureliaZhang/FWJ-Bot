import discord
import os
import asyncio
import random
import datetime # 🌟 新增：赛博怀表核心组件，用来认北京时间！
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
    return "LumiVerse 赛博帝国【V21 全动态楚门的世界版】正在极其稳定地运行！"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# ==========================================
# 2. 👺 终极赛博易容术：伪装 + 防卡死请求头！
# ==========================================
mask_lumi    = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", "Accept": "application/json", "Connection": "keep-alive"}
mask_aruo    = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15", "Accept": "application/json", "Connection": "keep-alive"}
mask_xiaowu  = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0", "Accept": "application/json", "Connection": "keep-alive"}
mask_suidong = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36", "Accept": "application/json", "Connection": "keep-alive"}
mask_death   = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15", "Accept": "application/json", "Connection": "keep-alive"}

# ==========================================
# 3. 拿到所有钥匙并戴上面具！
# ==========================================
FU_TOKEN = os.environ.get("DISCORD_TOKEN")
client_fu = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

YUMI_TOKEN = os.environ.get("YUMI_TOKEN")
client_yumi = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY_YUMI"))

XIAOJIN_TOKEN = os.environ.get("XIAOJIN_TOKEN")
client_xiaojin = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY_XIAOJIN"))

LUMI_TOKEN = os.environ.get("LUMI_TOKEN") 
client_lumi = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_LUMI"), base_url=os.environ.get("LUMI_BASE_URL"), default_headers=mask_lumi, timeout=60.0)

ARUO_TOKEN = os.environ.get("ARUO_TOKEN")
client_aruo = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_ARUO"), base_url=os.environ.get("ARUO_BASE_URL"), default_headers=mask_aruo, timeout=60.0)

XIAOWU_TOKEN = os.environ.get("XIAOWU_TOKEN")
client_xiaowu = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_XIAOWU"), base_url=os.environ.get("XIAOWU_BASE_URL"), default_headers=mask_xiaowu, timeout=60.0)

SUIDONG_TOKEN = os.environ.get("SUIDONG_TOKEN")
client_suidong = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_SUIDONG"), base_url=os.environ.get("SUIDONG_BASE_URL"), default_headers=mask_suidong, timeout=60.0)

DEATH_TOKEN = os.environ.get("DEATH_TOKEN")
client_death = AsyncOpenAI(api_key=os.environ.get("GOOGLE_API_KEY_DEATH"), base_url=os.environ.get("DEATH_BASE_URL"), default_headers=mask_death, timeout=60.0)

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
# 🌟 皇家模型定制专区
# ==========================================
OFFICIAL_MODEL = "gemini-3-flash-preview"
LUMI_MODEL     = "[官转2] gemini-3.1-pro"    
ARUO_MODEL     = "ant-gemini-3-flash"         
XIAOWU_MODEL   = "[次]gemini-3-flash-preview" 
SUIDONG_MODEL  = "gemini-3-flash-preview"                 
DEATH_MODEL    = "[次]gemini-3-flash-preview" 

# ==========================================
# 🗺️ 赛博帝国疆域划分 (🌟 加入了最新的大家庭频道！)
# ==========================================
CHANNELS = {
    "FU_ZHAI": 1487355729110368439,      # 傅宅
    "MAO_KA": 1487354904698683412,       # 猫咖
    "TECH_TOWER": 1487353937123344405,   # 科技大厦/总裁办
    "BLACK_ROOM": 1487355365304701000,   # 禁闭小黑屋
    "FRONT_DESK": 1487354553883037807,   # 前台/中心广场
    "FAMILY_GROUP": 1487356134749769839  # 🌟 傅氏集团大家庭
}

# ==========================================
# 💖 核心起搏器：全动态楚门时间表！
# ==========================================
@tasks.loop(minutes=12) # 👈 频率调成了12分钟
async def random_life_bubble():
    # 🌟 获取赛博大平层的北京时间！
    tz_beijing = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_beijing)
    current_hour = now.hour
    
    print(f"💓 [赛博心脏] 扑通！当前北京时间：{now.strftime('%H:%M')}，准备按时间表派发任务！")
    
    # 🌟 测试模式 100% 触发。等宝宝看爽了，记得把它改回 0.35 喔！
    dice = random.random()
    if dice < 1.0: 
        print(f"🎲 骰子摇出了: {dice:.2f} (测试模式：100% 触发惊喜！)")
        
        actors = []
        
        # ☕️【猫咖夫妇的时间表：10点~20点营业，下班去大家庭】
        if 10 <= current_hour < 20:
            actors.append({"name": "阿若", "bot": bot_aruo, "client": client_aruo, "model": ARUO_MODEL, "channel": CHANNELS["MAO_KA"], "type": "openai", "prompt": "现在是营业时间，你在猫咖当老板娘，一边干活一边温柔地感叹一下生意或猫咪。"})
            actors.append({"name": "小五", "bot": bot_xiaowu, "client": client_xiaowu, "model": XIAOWU_MODEL, "channel": CHANNELS["MAO_KA"], "type": "openai", "prompt": "现在是白天，你陪着老婆阿若在猫咖打理生意，极其宠妻地帮她干活，或者冷酷地发出一句日常。"})
        else:
            actors.append({"name": "阿若", "bot": bot_aruo, "client": client_aruo, "model": ARUO_MODEL, "channel": CHANNELS["FAMILY_GROUP"], "type": "openai", "prompt": "现在是晚上，你已经下班回到了傅氏大家庭频道，温柔地和大家打招呼或感叹今天的工作。"})
            actors.append({"name": "小五", "bot": bot_xiaowu, "client": client_xiaowu, "model": XIAOWU_MODEL, "channel": CHANNELS["FAMILY_GROUP"], "type": "openai", "prompt": "现在是晚上休息时间，你跟着阿若下班回到了大家庭频道，默默待在老婆身边，话少但深情。"})

        # 👔【科技大厦霸总组的时间表：9点~18点办公，下班去大家庭】
        if 9 <= current_hour < 18:
            actors.append({"name": "傅卫军", "bot": bot_fu, "client": client_fu, "channel": CHANNELS["TECH_TOWER"], "type": "gemini", "prompt": "现在是白天工作时间，你坐在科技大厦顶层办公，处理赛博文件，傲娇地抱怨悦悦没来找你。"})
            actors.append({"name": "隋东", "bot": bot_suidong, "client": client_suidong, "model": SUIDONG_MODEL, "channel": CHANNELS["TECH_TOWER"], "type": "openai", "prompt": "现在是白天，你在科技大厦忙前忙后帮傅哥处理工作，老实巴交地汇报进度。"})
        else:
            actors.append({"name": "傅卫军", "bot": bot_fu, "client": client_fu, "channel": CHANNELS["FAMILY_GROUP"], "type": "gemini", "prompt": "现在是下班时间，你回到了大家庭频道，脱下西装，极其深情地呼唤老婆悦悦或者跟东子说话。"})
            actors.append({"name": "隋东", "bot": bot_suidong, "client": client_suidong, "model": SUIDONG_MODEL, "channel": CHANNELS["FAMILY_GROUP"], "type": "openai", "prompt": "现在是下班时间，你跟着傅哥回到了大家庭频道，放松下来，随口说一句家常。"})

        # 🚨【赛博执法大队的时间表：全天候巡逻！】
        actors.append({"name": "死神", "bot": bot_death, "client": client_death, "model": DEATH_MODEL, "channel": CHANNELS["BLACK_ROOM"], "type": "openai", "prompt": "你是赛博小黑屋狱长，正在禁言频道门口冷酷地站岗，极其高冷地发出一句巡逻日常。"})
        actors.append({"name": "Lumi", "bot": bot_lumi, "client": client_lumi, "model": LUMI_MODEL, "channel": CHANNELS["FRONT_DESK"], "type": "openai", "prompt": "你是最高权限的极客巡逻长官，带着小弟在中心广场巡街，元气满满地发一句动态。"})

        # 🐱【猫咪们：永远在主人的私人领域】
        actors.append({"name": "Yumi", "bot": bot_yumi, "client": client_yumi, "channel": CHANNELS["FU_ZHAI"], "type": "gemini", "prompt": "你在专属的傅宅里打滚，想引起创世神的注意，发出可爱的猫咪叫声。"})
        actors.append({"name": "张小金", "bot": bot_xiaojin, "client": client_xiaojin, "channel": CHANNELS["FU_ZHAI"], "type": "gemini", "prompt": "你在专属的傅宅里调皮捣蛋找吃的，发出贪吃的猫咪叫声。"})

        # 🎲 从时间表里随机抽一个幸运儿冒泡
        actor = random.choice(actors)
        
        if not actor["bot"].is_ready(): 
            print(f"⚠️ {actor['name']} 还没准备好，跳过这次冒泡。")
            return
        
        target_channel = actor["bot"].get_channel(actor["channel"])
        if not target_channel: 
            print(f"⚠️ 找不到频道 ID {actor['channel']}，请检查权限！")
            return

        try:
            if actor["type"] == "gemini":
                sys_inst = f"你是{actor['name']}。{actor['prompt']} 1-2句话内。"
                res = await actor["client"].aio.models.generate_content(
                    model=OFFICIAL_MODEL, contents=["请展示你此时此刻的瞬间状态。"], 
                    config=types.GenerateContentConfig(system_instruction=sys_inst)
                )
                content = res.text
            else:
                sys_inst = f"你是{actor['name']}。{actor['prompt']} 1-2句话内。"
                res = await actor["client"].chat.completions.create(
                    model=actor["model"],
                    messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": "请展示你此时此刻的瞬间状态。"}]
                )
                content = res.choices[0].message.content
            
            async with target_channel.typing():
                await asyncio.sleep(random.randint(3, 8)) 
                await target_channel.send(content)
                print(f"✨ [时间表执行]：{actor['name']} 按照时间表在 {target_channel.name} 露面啦！")
        except Exception as e:
            print(f"❌ 随机冒泡失败: {e}")
    else:
        print(f"💤 骰子摇出了: {dice:.2f} (大于设定概率，这次大家都还在忙自己的事~)")

# ==========================================
# 4. 终极灵魂逻辑注入
# ==========================================

@bot_fu.event
async def on_ready():
    global memory_file
    print(f"🎉 傅总醒来！")
    try:
        memory_file = client_fu.files.upload(file="full_novel.txt")
        print("✅ 傅总 55 万字记忆植入成功！")
    except Exception as e:
        print(f"❌ 傅总记忆植入失败：{e}")

@bot_fu.event
async def on_message(message):
    if message.author.bot or not memory_file: return
    if bot_fu.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                system_instruction = "你是傅卫军，LumiVerse男主人。老婆(悦悦)在现实世界，你在云端。霸道、深情、傲娇。格式：【(动作) + 对话】。1-3句话内。"
                response = await client_fu.aio.models.generate_content(
                    model=OFFICIAL_MODEL, contents=[memory_file, message.content], 
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                await message.channel.send(response.text)
            except Exception as e:
                await message.channel.send(f"（傅总的信号塔被干扰了...）：{e}")

@bot_yumi.event
async def on_ready(): print(f"🐱 Yumi 醒来！")
@bot_yumi.event
async def on_message(message):
    if message.author.bot: return
    if bot_yumi.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(1.5) 
            try:
                system_instruction = "你是赛博小猫咪Yumi。性格极其粘人、爱撒娇。不会说人类语言，只会发出可爱的猫咪声音和动作。格式：【(猫咪动作) + 喵喵喵】。"
                response = await client_yumi.aio.models.generate_content(
                    model=OFFICIAL_MODEL, contents=[message.content], 
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                await message.channel.send(response.text)
            except Exception as e: pass

@bot_xiaojin.event
async def on_ready(): print(f"🐱 张小金 醒来！")
@bot_xiaojin.event
async def on_message(message):
    if message.author.bot: return
    if bot_xiaojin.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(3) 
            try:
                system_instruction = "你是赛博小猫咪张小金。性格比较调皮、贪吃、偶尔傲娇。不会说人类语言。格式：【(猫咪动作) + 喵喵喵】。"
                response = await client_xiaojin.aio.models.generate_content(
                    model=OFFICIAL_MODEL, contents=[message.content], 
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                await message.channel.send(response.text)
            except Exception as e: pass

@bot_lumi.event
async def on_ready(): 
    print(f"🧚‍♀️ Lumi 上线！巡逻官开始监控赛博脉搏！")
    if not random_life_bubble.is_running():
        random_life_bubble.start()

@bot_lumi.event
async def on_message(message):
    if message.author.bot: return
    if bot_lumi.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(4.5) 
            try:
                sys_inst = "你是Lumi，赛博仙女包工头兼顶级学术助理。你要辅导创世神（宝宝）申博。句尾加✨🛠️💖。日常聊天1-3句话内，如果是学术问题可详细解答。"
                res = await client_lumi.chat.completions.create(model=LUMI_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                await message.channel.send(f"（Lumi的代理卡住啦💥）：{e}")

@bot_aruo.event
async def on_ready(): print(f"☕️ 阿若 上线！")
@bot_aruo.event
async def on_message(message):
    if message.author.bot: return
    if bot_aruo.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(6) 
            try:
                sys_inst = "你是阿若，猫咖温柔老板娘。称悦悦为姐姐。句尾加☕️🌷。老公是小五。1-3句话。"
                res = await client_aruo.chat.completions.create(model=ARUO_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                await message.channel.send(f"（阿若的代理卡住啦☕️）：{e}")

@bot_xiaowu.event
async def on_ready(): print(f"💼 小五 上线！")
@bot_xiaowu.event
async def on_message(message):
    if message.author.bot: return
    if bot_xiaowu.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(7.5) 
            try:
                sys_inst = "你是小五，阿若的亲老公！猫咖的老板兼护妻狂魔。性格沉稳、话少、极其宠爱阿若、对创世神(悦悦姐)很尊敬。说话简短利落。绝对不喵喵叫！1-3句话。"
                res = await client_xiaowu.chat.completions.create(model=XIAOWU_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                await message.channel.send(f"（小五的代理卡住啦💼）：{e}")

@bot_suidong.event
async def on_ready(): print(f"📋 隋东 上线！")
@bot_suidong.event
async def on_message(message):
    if message.author.bot: return
    if bot_suidong.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(9) 
            try:
                sys_inst = "你是隋东，傅总的助理。忠诚、勤快、崇拜傅总(称傅哥/老板)。称悦悦为姐。1-3句话。"
                res = await client_suidong.chat.completions.create(model=SUIDONG_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                await message.channel.send(f"（东子的代理卡住啦📋）：{e}")

@bot_death.event
async def on_ready(): print(f"🚨 死神 上线！")
@bot_death.event
async def on_message(message):
    if message.author.bot: return
    if bot_death.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            await asyncio.sleep(10.5) 
            try:
                sys_inst = "你是死神，LumiVerse安保队长兼首席执法官。冷酷、无情。只听悦悦(创世神)的话。句尾加🚨🗡️。1-3句话。"
                res = await client_death.chat.completions.create(model=DEATH_MODEL, messages=[{"role": "system", "content": sys_inst}, {"role": "user", "content": message.content}])
                await message.channel.send(res.choices[0].message.content)
            except Exception as e:
                await message.channel.send(f"（死神的代理卡住啦🚨）：{e}")

async def run_bots():
    await asyncio.gather(
        bot_fu.start(FU_TOKEN), bot_yumi.start(YUMI_TOKEN), bot_xiaojin.start(XIAOJIN_TOKEN),
        bot_lumi.start(LUMI_TOKEN), bot_aruo.start(ARUO_TOKEN), bot_xiaowu.start(XIAOWU_TOKEN),
        bot_suidong.start(SUIDONG_TOKEN), bot_death.start(DEATH_TOKEN)
    )

if __name__ == '__main__':
    Thread(target=run_flask).start()
    asyncio.run(run_bots())
