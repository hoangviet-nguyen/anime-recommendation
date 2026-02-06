#!/usr/bin/env python

'''
Download data from the Kaggle API if the ./data/ directory is not present.
'''

import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


if __name__ == "__main__":
    data_dir = "./data"

    if not os.path.exists("./data"):
        os.mkdir(data_dir)

        try:
            api = KaggleApi()
            api.authenticate()
            # Dataset herunterladen
            api.dataset_download_files("dbdmobile/myanimelist-dataset", path=data_dir, unzip=True)

            print("Completed the download")
        except Exception as err:
            print("Error:", err)
            os.removedirs(data_dir)
