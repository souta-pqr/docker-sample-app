from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    name = ''
    fortune = ''
    if request.method == 'POST':
        name = request.form.get('name')
        fortunes = [
            "大吉！素晴らしい1日になるでしょう！",
            "中吉。良いことがありそうです。",
            "小吉。小さな幸せが待っています。",
            "吉。平和な1日になりそうです。",
            "凶…でも、明日はきっと良い日になります！"
        ]
        fortune = random.choice(fortunes)
    return render_template('index.html', name=name, fortune=fortune)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)