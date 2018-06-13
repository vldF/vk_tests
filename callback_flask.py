from multiprocessing import Queue, Process
import time
import requests as req
from flask import Flask, request


app = Flask(__name__)
q = Queue()
t_send = 0

API_ROOT = 'https://api.vk.com/method/'
access_token = ''
group_id = -00000


@app.route('/', methods=['POST'])
def main():
    global q
    decoded = request.get_json()
    if decoded.get('type') == 'message_new':
        t = time.time()
        q.put(t)
    return 'ok', 200


def send_msg():
    global t_send
    time.sleep(1)
    data = {'access_token': access_token, 'v': '5.78', 'peer_id': group_id, 'message': 'test'}
    req.post(API_ROOT+'messages.send', data=data)
    t_send = time.time()
    return


def checker(q):
    res = 0
    for i in range(10):
        send_msg()
        t1 = t_send
        t2 = q.get()
        res += t2-t1
    print(res/10)


if __name__ == '__main__':
    p = Process(target=checker, args=(q,))
    p.daemon = True
    p.start()
    app.run(host='0.0.0.0', port=80)
