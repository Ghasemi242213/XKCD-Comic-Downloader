import threading
import multiprocessing
import time
import requests
import os
from concurrent.futures import ThreadPoolExecutor

os.makedirs('photos', exist_ok=True)

def get_comic(comic_no):
    print(f'start getting image number {comic_no}')
    res = requests.get(f"https://xkcd.com/{comic_no}/info.0.json")
    if res.status_code != 200:
        print(f"comic {comic_no} NOT FOUND")
        return
    
    image_url = res.json()['img']
    image_name = image_url.split('/')[-1]
    img = requests.get(image_url)

    with open(f"photos/{image_name}", 'wb') as f:
        f.write(img.content)

    print(f'end of getting image number {comic_no}')
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(get_comic, range(1, 101))
