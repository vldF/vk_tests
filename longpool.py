import requests as req
import time
from multiprocessing import Queue, Process

API_ROOT = 'https://api.vk.com/method/'
access_token = ''
access_token_group = ''
group_id = ''

t_send = 0


def send_msg(q):
    global t_send
    time.sleep(1)
    data = {'access_token': access_token, 'v': '5.78', 'peer_id': -167143798, 'message': 'test'}
    ans = req.post(API_ROOT+'messages.send', data=data)
    print(ans.content)
    t_send = time.time()


def get_new_events(q):
    builder = 'https://api.vk.com/method/groups.getLongPollServer?access_token='+access_token_group+'&v=5.78&' \
                                                            'group_id='+group_id
    ans = req.post(builder, verify=False).json()['response']
    ts = ans.get('ts')

    while True:
        builder = '{}?act=a_check&key={}&ts={}&wait=15&mode=2&version=3'.format(ans.get('server'),
                                                                                        ans.get('key'),
                                                                                        ts)
        resp = req.post(builder, verify=False).json()
        if resp.get('ts'):
            ts = resp.get('ts')
        if resp.get('updates'):
            q.put(time.time())
            continue


if __name__ == '__main__':
    q = Queue()
    res = 0

    p = Process(target=get_new_events, args=(q,))
    p.start()

    for i in range(10):
        send_msg(q)
        t1 = t_send
        t2 = q.get()
        res += t2-t1
    print(res/10)
