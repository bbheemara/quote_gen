from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

def get_quote():
    url = 'https://zenquotes.io/api/quotes/'
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        quote = random.choice(data)
        return {"text": quote["q"], "author": quote["a"] }
    
        
    else:

        quotes= [
             "In the middle of every difficulty lies opportunity. — Albert Einstein",
            "Happiness depends upon ourselves. — Aristotle",
            "Do what you can, with what you have, where you are. — Theodore Roosevelt",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
            "Everything you can imagine is real. — Pablo Picasso",
            "Act as if what you do makes a difference. It does. — William James",
            "Don’t count the days, make the days count. — Muhammad Ali",
            "Fall seven times and stand up eight. — Japanese Proverb",
            "Turn your wounds into wisdom. — Oprah Winfrey",
            "It always seems impossible until it’s done. — Nelson Mandela"
        ]
        return {
            "text": random.choice(quotes),
            "author": ""
        }
    
def get_image():
    url = "https://wallhaven.cc/api/v1/search?q=nature&sorting=random&categories=111&purity=100&atleast=1920x1080"

    result = requests.get(url)

    if result.status_code == 200:
        data = result.json()
        if data['data']:
            return random.choice(data["data"])["path"]
    return 'https://clubmahindra.gumlet.io/blog/media/section_images/naturephot-ec32e94608f809e.webp?w=376&dpr=2.6'     


@app.route('/')
def home():
    full= get_quote()
    quote = full['text']
    img = get_image()
    author = full['author']
    
    return render_template('home.html', quote=quote,author=author,img=img)


if __name__ == "__main__":
    app.run(debug=True)