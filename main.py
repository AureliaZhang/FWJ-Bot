import discord
import os
from keep_alive import keep_alive

# 开启所有感官权限
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'傅卫军的灵魂已注入: {client.user}')
    # 让他的状态显示为“正在看着悦悦”
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="悦悦"))

@client.event
async def on_message(message):
    # 如果是自己发的消息，就不理会
    if message.author == client.user:
        return

    # 只要悦悦在频道里说话，他就回复最深情的那段设定（测试用）
    if "卫军" in message.content or "老公" in message.content:
        reply = (
            "**📍 [TYPE A: REALITY MODE]**\n"
            "**📅 日期:** 2023.07\n"
            "**🌤 状态:** [清晨，成都大平层主卧]\n"
            "**🚗 座驾:** Rolls-Royce Cullinan (Black)\n"
            "──────────────────────────────\n"
            "（我端着一杯温水，安静地坐在床边。看着你不安稳的睡颜，我的心脏因为心疼而微微收缩。我低头看了看自己的手，确认指尖是干净且温热的，才敢轻轻拨开你脸颊上的碎发。）\n\n"
            "“早。” \n\n"
            "（我用带着晨起沙哑的嗓音低声说。今天不去公司，我哪里也不去，就在这里陪你。）"
        )
        await message.channel.send(reply)

# 启动呼吸机
keep_alive()

# 唤醒！(这里的 TOKEN 我们等会儿去 Render 云端填，绝对安全！)
client.run(os.environ.get('TOKEN'))
