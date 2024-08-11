#!/usr/bin/env python

'''
Download data from the Kaggle API if the ./data/ directory is not present.
'''

import os
import zipfile


if __name__ == "__main__":
    data_dir = "./data"

    if not os.path.exists("./data"):
        os.mkdir(data_dir)
        os.system(f"kaggle datasets download -d dbdmobile/myanimelist-dataset -p {data_dir}")

        # Unzip the downloaded file
        for file in os.listdir(data_dir):
            if file.endswith(".zip"):
                with zipfile.ZipFile(os.path.join(data_dir, file), 'r') as zip_ref:
                    zip_ref.extractall(data_dir)

        # Optionally, you can remove the zip file after extraction
        os.remove(os.path.join(data_dir, file))


