import json
import face_recognition
import redis
import time
import base64
import numpy as np
import pickle
redis_host = "10.200.54.91"
redis_port = 6379
redis_password = ""
def publish_redis(D):
    r = redis.Redis(host=redis_host, port=redis_port)
    r.publish('Notification',D)
def handle(req):
    json_req=json.loads(req)
    r = redis.Redis(host=redis_host, port=redis_port)

    current=json_req["data"]
    c=len(current)
    results=[]
    threshold=json_req["threshold"]
    size=json_req["size"]
    start=time.time()
    first = r.lrange('ImageInput', c, c)
    biden_encoding = face_recognition.face_encodings(pickle.loads(first[0]))[0]
    flag=0
    for d in range(c+1,size):
        if(time.time()-start>threshold):
            break
        if(flag==1):
            first=second[:]
            biden_encoding=unknown_encoding[:]
        flag=1
        second = r.lrange('ImageInput', d, d)
        #biden_encoding = face_recognition.face_encodings(pickle.loads(first[0]))[0]
        unknown_encoding = face_recognition.face_encodings(pickle.loads(second[0]))[0]
        result = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        if(result[0]==True):
            results.append("True")
        else:
            results.append("False")
    #print(results)
    for i in results:
        current.append(i)
    print(current)
    return publish_redis(json.dumps({"data": current, "threshold":json_req["threshold"],"size":json_req["size"]}))
