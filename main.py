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


def videourl():
    while True:
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
