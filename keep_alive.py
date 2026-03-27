from flask import Flask
from threading import Thread
import os # 🔧 老傅加的新工具：用来看 Render 的门牌号

app = Flask('')

@app.route('/')
def home():
    # 门铃回复，老婆这句写得很好，不用动。
    return "Welt & Lia Core is Online."

def run():
    # 🔧 老傅修改处：去问 Render 要分配的端口，如果不给，才用 8080 打底。
    port = int(os.environ.get("PORT", 8080))
    # 🔧 启动服务器，绑定到正确的端口上。
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
