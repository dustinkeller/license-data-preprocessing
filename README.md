# License Plate Dataset Preprocessing

## Authors
Dustin Keller, Matthew Chaves, Syed Alif, Alfred Ulaj

## Purpose
This script converts our license plate dataset from Kaggle to the Ultralytics YOLO dataset format. This format consists of three directories: `./test`, `./train`, `./valid`. Each of these directories contains two subdirectories: `./images` and `./labels`. The `./images` directories contains the license plate image files, `[NUMBER].jpg`, and the `./labels` directory contains corresponding text files, `[NUMBER].txt`, containing the class (state/territory) of the image as well as the bounding box (where the subject is located).  

## Data
This dataset was taken from [US license plates- Image Classification](https://www.kaggle.com/datasets/gpiosenka/us-license-plates-image-classification/suggestions?status=pending&yourSuggestions=true) on Kaggle. The dataset is formatted with a `plates.csv` file and three directories: `./test`, `./train`, `./valid`. Each of these directories contains subdirectories for each US state/territory contained in the dataset, containing all of the corresponding license plate images for that state/territory.

## Usage
- Ensure you have the original directory configuration (`./train`, `./test`, `./valid` directories containing the subdirectories of each state/territory with images inside) and the `plates.csv` file.
- Run `python3 convert_csv.py`.
- Find the converted YOLO dataset images and textfiles in the `./annotations_yolo` folder.
- Create a `yolov8_config.yaml` file. In our case, it looks like this:
```
train: train/images
val: valid/images
test: test/images

names:
  0: ALABAMA
  1: ALASKA
  2: AMERICAN SAMOA
  3: ARIZONA
  4: ARKANSAS
  5: CALIFORNIA
  6: CNMI
  7: COLORADO
  8: CONNECTICUT
  9: DELAWARE
  10: FLORIDA
  11: GEORGIA
  12: GUAM
  13: HAWAI
  14: IDAHO
  15: ILLINOIS
  16: INDIANA
  17: IOWA
  18: KANSAS
  19: KENTUCKY
  20: LOUISIANA
  21: MAINE
  22: MARYLAND
  23: MASSACHUSETTS
  24: MICHIGAN
  25: MINNESOTA
  26: MISSIPPI
  27: MISSOURI
  28: MONTANA
  29: NEBRASKA
  30: NEVADA
  31: NEW HAMPSHIRE
  32: NEW JERSEY
  33: NEW MEXICO
  34: NEW YORK
  35: NORTH CAROLINA
  36: NORTH DAKOTA
  37: OHIO
  38: OKLAHOMA
  39: OREGON
  40: PENNSYLVANIA
  41: PUERTO RICO
  42: RHODE ISLAND
  43: SOUTH CAROLINA
  44: SOUTH DAKOTA
  45: TENNESSEE
  46: TEXAS
  47: U S VIRGIN ISLANDS
  48: UTAH
  49: VERMONT
  50: VIRGINIA
  51: WASHINGTON
  52: WASHINGTON DC
  53: WEST VIRGINIA
  54: WISCONSIN
  55: WYOMING
```
