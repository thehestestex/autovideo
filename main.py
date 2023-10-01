from pymongo.mongo_client import MongoClient
import json
import os
conp = MongoClient("mongodb+srv://thejatin:jatinkalwar@attacknum.nmuaiq8.mongodb.net/?retryWrites=true&w=majority")

for x in conp.SumayaAcademyapk.youtubeurl.find():
    urll = conp.SumayaAcademyapk.youtubeurl.find_one({"sno": x['sno']}, {'url': 1 , '_id': 0})
    oldurl = urll['url']

    newurl = os.system(f"yt-dlp --get-url -f 18 {oldurl}")
    conp.attack.sumayaacademy.update_one({"sr": x['sno']}, {'$set': {"vurl": newurl}})
