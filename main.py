from pymongo.mongo_client import MongoClient
import json
import os
import time
import threading
import requests
conp = MongoClient("mongodb+srv://thejatin:jatinkalwar@attacknum.nmuaiq8.mongodb.net/?retryWrites=true&w=majority")
from pymongo.mongo_client import MongoClient
import json
import os
import time
import threading
from datetime import datetime
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi import BackgroundTasks
from fastapi.responses import PlainTextResponse
import requests
conp = MongoClient("mongodb+srv://thejatin:jatinkalwar@attacknum.nmuaiq8.mongodb.net/?retryWrites=true&w=majority")
kalwar = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


def statt():
    def videourl():
        while True:
            print("Upon here")
            for x in conp.SumayaAcademyapk.youtubeurl.find():
                print("here")
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
            print("Sumaya Server Start")
            requests.get("https://sumayaacademy.onrender.com/")
            time.sleep(780)
    def video():
        while True:
            requests.get("https://autourl-3ptn.onrender.com/")
            time.sleep(300)

    def printt():
        while True:
            print("working")
            time.sleep(5)
            
            
            




    t1 = threading.Thread(target=videourl)
    t2 = threading.Thread(target=startserver)
    
    t3 = threading.Thread(target=video)
    t4 = threading.Thread(target=printt)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
@kalwar.get("/", response_class=PlainTextResponse)
async def verif(background_tasks: BackgroundTasks):
   background_tasks.add_task(statt)
   return "ok"
