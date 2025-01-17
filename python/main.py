import requests
import os
from dotenv import load_dotenv


def get_vector_urls(url_file, data_folder="data/metrolinx"):
    load_dotenv()
    token = os.getenv("MAPBOX_TOKEN")
    with open(url_file) as f:
        lines = f.readlines()
        urls = [line.strip() for line in lines]

    print(f"Downloading {len(urls)} vector files")
    for url in urls:
        filename = "-".join(url.split("/")[-3:])
        print(filename)
        r = requests.get(f"{url}?access_token={token}")
        if r.status_code == 200:
            with open(f"{data_folder}/{filename}", "wb") as f:
                f.write(r.content)
        else:
            print(r.status_code)


def get_vector_tiles(data_folder="data/metrolinx"):
    load_dotenv()
    token = os.getenv("MAPBOX_TOKEN")

    base_url = "https://api.mapbox.com/v4/spatialmedia.210216torontomassing,mapbox.mapbox-streets-v8,spatialmedia.cko3fmhw601m827msm2f2qqy9-3tdg2,mapbox.mapbox-terrain-v2,spatialmedia.240602metrolinxlayer,spatialmedia.6y0j7ndj"
    zoom_level = 14
    for col in range(4576, 4581):
        for row in range(5977, 5981):
            filename = f"{zoom_level}-{col}-{row}.vector.pbf"
            print(filename)
            r = requests.get(
                f"{base_url}/{zoom_level}/{col}/{row}.vector.pbf?access_token={token}"
            )
            if r.status_code == 200:
                with open(f"{data_folder}/{filename}", "wb") as f:
                    f.write(r.content)
            else:
                print(r.status_code)


def get_vector_toronto(data_folder="data/metrolinx"):
    load_dotenv()
    token = os.getenv("MAPBOX_TOKEN")

    base_url = "https://api.mapbox.com/v4/spatialmedia.cko3fmhw601m827msm2f2qqy9-3tdg2,spatialmedia.240602metrolinxlayer,spatialmedia.6y0j7ndj"
    zoom_level = 10
    for col in range(285, 287):
        for row in range(373, 374):
            filename = f"{zoom_level}-{col}-{row}.vector.pbf"
            print(filename)
            r = requests.get(
                f"{base_url}/{zoom_level}/{col}/{row}.vector.pbf?access_token={token}"
            )
            if r.status_code == 200:
                with open(f"{data_folder}/{filename}", "wb") as f:
                    f.write(r.content)
            else:
                print(r.status_code)


def main():
    # get_vector_urls('data/metrolinx/vector-urls.txt')
    get_vector_toronto()


if __name__ == "__main__":
    main()
