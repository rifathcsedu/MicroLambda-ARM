import json
#import redis
#import face_recognition
#import requests
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
redis_host = "10.200.54.91"
redis_port = 6379
redis_password = ""
reload(sys)
sys.setdefaultencoding('utf8')

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf
'''
def publish_redis(D):
    r = redis.Redis(host=redis_host, port=redis_port)
    r.publish('SortTrigger',D)
'''
def handle(req):
    #known_image = face_recognition.load_image_file(requests.get("https://i.imgur.com/9yilMqm.jpg", stream=True).raw)
    #unknown_image = face_recognition.load_image_file(requests.get("https://i.imgur.com/Pg062zv.jpg", stream=True).raw)
    #biden_encoding = face_recognition.face_encodings(known_image)[0]
    #unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    #results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    #print(results)
    results=False
    return (json.dumps({"output": results}))
if __name__ == "__main__":
    st = get_stdin()
    print(handle(st))
