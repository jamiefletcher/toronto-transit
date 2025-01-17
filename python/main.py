import requests
import os
from dotenv import load_dotenv


def get_mapbox_tiles(
    token,
    data_folder,
    layers,
    zoom_level,
    cols,
    rows,
    base_url="https://api.mapbox.com/v4",
):
    # base_url = "https://api.mapbox.com/v4/spatialmedia.210216torontomassing,mapbox.mapbox-streets-v8,spatialmedia.cko3fmhw601m827msm2f2qqy9-3tdg2,mapbox.mapbox-terrain-v2,spatialmedia.240602metrolinxlayer,spatialmedia.6y0j7ndj"
    # zoom_level = 14
    # for col in range(4576, 4581):
    #     for row in range(5977, 5981):

    for col in cols:
        for row in rows:
            filename = f"{zoom_level}-{col}-{row}.vector.pbf"
            print(filename)
            r = requests.get(
                f"{base_url}/{layers}/{zoom_level}/{col}/{row}.vector.pbf?access_token={token}"
            )
            if r.status_code == 200:
                with open(f"{data_folder}/{filename}", "wb") as f:
                    f.write(r.content)
            else:
                print(r.status_code)


def main():
    load_dotenv()
    get_mapbox_tiles(
        token=os.getenv("MAPBOX_TOKEN"),
        data_folder="data/metrolinx",
        layers="spatialmedia.cko3fmhw601m827msm2f2qqy9-3tdg2,spatialmedia.240602metrolinxlayer,spatialmedia.6y0j7ndj",
        zoom_level=10,
        cols=range(285, 287),
        rows=range(373, 374),
    )


if __name__ == "__main__":
    main()
