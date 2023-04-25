import kaggle
import os
from zipfile import ZipFile


FILE_NAME = "housing.csv.zip"
DATA_DIR_PATH = "datasets/housing"
FILE_PATH = DATA_DIR_PATH + "/" + FILE_NAME

Error_Message = """
ConnectionError: Check the following
1. Proper network connection.
2. Proper Authentication setup for kaggle. Check link 
(https://www.kaggle.com/docs/api#getting-started-installation-&-authentication)
3. Network service provider.
"""

def main():
    try:
        if not os.path.exists(FILE_PATH):
            kaggle.api.dataset_download_file(
                dataset="camnugent/california-housing-prices",
                file_name="housing.csv",
                path=DATA_DIR_PATH
                )
            
            with ZipFile(FILE_PATH, "r") as f:
                f.extractall(DATA_DIR_PATH)
            f.close()
    except:
        print(Error_Message)

if __name__=="__main__":
    main()


