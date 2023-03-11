import argparse
import threading
import requests

def send_request(url, method, data=None):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
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
    else:
        return None

def worker(url, method, data=None):
    while True:
        try:
            response = send_request(url, method, data)
            print(response.status_code)
        except requests.exceptions.RequestException as e:
            print(e)

def run_threads(url, method, num_threads, data=None):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(url, method, data))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Website load testing tool')
    parser.add_argument('url', help='URL of the website')
    parser.add_argument('method', choices=['GET', 'POST', 'HEAD', 'HTTP-SYN', 'HTTP-SYN-TPC'], help='HTTP request method')
    parser.add_argument('-n', '--num_threads', type=int, default=1, help='number of threads to run')
    parser.add_argument('-d', '--data', help='data to send in a POST request')
    args = parser.parse_args()

    run_threads(args.url, args.method, args.num_threads, args.data)
