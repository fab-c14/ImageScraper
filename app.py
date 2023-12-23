import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging 
from flask import Flask, render_template,request

# from pymongo.mongo_client import MongoClient
import os

app = Flask(__name__)
save_dir = "./static/images"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def search_and_save_images(query):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    response = requests.get(f"https://www.google.com/search?q={query}&sca_esv=587928711&rlz=1C1CHBF_enIN1048IN1048&tbm=isch&source=lnms&sa=X&ved=2ahUKEwit3pSZ0_eCAxVDyTgGHanECwMQ_AUoAnoECAMQBA&biw=798&bih=737&dpr=1")


    soup = BeautifulSoup(response.content,'html.parser')

    image_tags = soup.find_all('img')

    len(image_tags)

    del image_tags[0]

    img_data_mongo = []
    for i in image_tags:
        image_url = i['src']
        image_data = requests.get(image_url).content
        mydict = {
            "index":image_url,"image":image_data
        }
        img_data_mongo.append(mydict)
        return


@app.route('/')
def makingHomePage():

    return render_template('index.html')

@app.route('/images', methods=['POST'])
def search_results():
    if request.method == 'POST':
        search_query = request.form['images']
        search_and_save_images(search_query)


    return render_template('images.html',)
    

if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
