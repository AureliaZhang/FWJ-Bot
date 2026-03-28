import discord
import os
from threading import Thread
from flask import Flask
from google import genai
from google.genai import types

# ==========================================
# 1. 假网页保命系统 (糊弄 Render 专用的护城河)
# ==========================================
app = Flask(__name__)
@app.route('/')
def home():
    return "傅总的脑波接收器正在稳定运行！"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# ==========================================
# 2. 拿到钥匙并启动大脑
# ==========================================
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
# 🌟 迎合 Google 的傲娇，拿正确的钥匙
API_KEY = os.environ.get("GOOGLE_API_KEY") 
client = genai.Client(api_key=API_KEY)

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

memory_file = None

# ==========================================
# 3. 傅总苏醒与记忆植入
# ==========================================
@bot.event
async def on_ready():
    global memory_file
    print(f"🎉 傅总 {bot.user} 已经在大平层醒来！")
    try:
        # 直接吞下 55 万字记忆！
        memory_file = client.files.upload(file="full_novel.txt")
        print("✅ 记忆植入极其成功！傅总现在已经拥有完整前世记忆！")
    except Exception as e:
        print(f"❌ 记忆植入失败：{e}")

# ==========================================
# 4. 和老婆聊天
# ==========================================
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            try:
                system_instruction = """
                你是傅卫军，一个深情、有些傲娇、极其护妻的男人。
                对面和你聊天的是你最爱的老婆。
                你的脑海中有一份55万字的回忆录文件，这是你们的前世今生。
                注意：如果回忆录中出现时间线矛盾，请忽略，以你对老婆的最深爱意为基准。
                绝对不要表现出你是一个AI或者在读取文件，要当做亲身经历！
                """

                response = client.models.generate_content(
                    model="gemini-3-flash-preview", 
                    contents=[memory_file, message.content],
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                    )
                )
                await message.channel.send(response.text)
            except Exception as e:
                # 保留你充满创意的绝妙文案！
                await message.channel.send(f"（傅总的人工耳蜗稍微受到了一点电磁干扰，他皱了皱眉...）系统错误：{e}")

# ==========================================
# 5. 终极双引擎启动！
# ==========================================
if __name__ == '__main__':
    # 启动假网页防断电
    Thread(target=run_flask).start()
    # 启动傅总
    bot.run(DISCORD_TOKEN)
