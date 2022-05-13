# Download Images (single-threaded)
import time
import requests


def get_urls():
    filename = 'coco_img_urls.txt'
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    return lines


def download_image(img_url):
    img_bytes = requests.get(img_url).content  # slowest part of the program
    img_name = img_url.split('/')[-1]
    img_file = open(f'images/{img_name}', "wb")  # wb | ab | rb
    img_file.write(img_bytes)
    img_file.close()
    print(f'{img_name} was downloaded...')


if __name__ == '__main__':
    start = time.perf_counter()
    img_urls = get_urls()[:100]

    for url in img_urls:
        download_image(url)

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
