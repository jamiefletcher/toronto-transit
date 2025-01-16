import requests
import os
from dotenv import load_dotenv

def get_vector_urls(url_file, data_folder='data/metrolinx'):
    load_dotenv()
    token = os.getenv('MAPBOX_TOKEN')
    with open(url_file) as f:
        lines = f.readlines()
        urls = [line.strip() for line in lines]
    
    print(f"Downloading {len(urls)} vector files")
    for url in urls:
        filename = '-'.join(url.split('/')[-3:])
        print(filename)
        r = requests.get(f"{url}?access_token={token}")
        if r.status_code == 200:
            with open(f"{data_folder}/{filename}", "wb") as f:
                f.write(r.content)
        else:
            print(r.status_code)

        

def main():
    get_vector_urls('data/metrolinx/vector-urls.txt')

if __name__ == '__main__':
    main()