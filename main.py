from pymongo.mongo_client import MongoClient
import json
import os
import time
import threading
import requests
conp = MongoClient("mongodb+srv://thejatin:jatinkalwar@attacknum.nmuaiq8.mongodb.net/?retryWrites=true&w=majority")
def videourl():
    while True:
        for x in conp.SumayaAcademyapk.youtubeurl.find():
            urll = conp.SumayaAcademyapk.youtubeurl.find_one({"sno": x['sno']}, {'url': 1 , '_id': 0})
            oldurl = urll['url']
            os.system(f"yt-dlp --get-url -f 18 {oldurl} >> vurl.txt")
            with open('vurl.txt') as f:
                newurl = f.read()
            os.system("rm vurl.txt")
            conp.attack.sumayaacademy.update_one({"sr": x['sno']}, {'$set': {"vurl": newurl}})
        print("done")
        time.sleep(18000)
        print("start Again")

def startserver():
    while True:
        requests.get("https://sumayaacademy.onrender.com/")
        time.sleep(780)




t1 = threading.Thread(target=videourl)
t2 = threading.Thread(target=startserver)

t1.start()
t2.start()
