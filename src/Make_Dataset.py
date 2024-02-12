import os
import shutil
import random

# ソースとなるフォルダ
source_folder = "/workspace/data/data"

# 再構成後のフォルダ
output_folder = "/workspace/data/Dataset"

if os.path.exists(source_folder) == False:
    print("Dataset folder dosen't exists. please set data or dir")
    exit()

if os.path.exists(output_folder):
    print("Dataset folder already exists.")
    exit()
    
# Datasetフォルダを作成
os.makedirs(output_folder, exist_ok=True)

# 分割比率
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# 各クラスのサブフォルダを作成
for folder in os.listdir(source_folder):
    os.makedirs(os.path.join(output_folder, "train", folder), exist_ok=True)
    os.makedirs(os.path.join(output_folder, "validation", folder), exist_ok=True)
    os.makedirs(os.path.join(output_folder, "test", folder), exist_ok=True)

# 画像を移動し、分割比率に従ってテスト、検証、トレーニングに分配
for folder in os.listdir(source_folder):
    files = os.listdir(os.path.join(source_folder, folder))
    random.shuffle(files)

    num_files = len(files)
    train_split = int(train_ratio * num_files)
    val_split = int(val_ratio * num_files)

    train_files = files[:train_split]
    val_files = files[train_split:train_split + val_split]
    test_files = files[train_split + val_split:]

    for file in train_files:
        shutil.move(os.path.join(source_folder, folder, file), os.path.join(output_folder, "train", folder, file))
    for file in val_files:
        shutil.move(os.path.join(source_folder, folder, file), os.path.join(output_folder, "validation", folder, file))
    for file in test_files:
        shutil.move(os.path.join(source_folder, folder, file), os.path.join(output_folder, "test", folder, file))
shutil.rmtree(source_folder)
print("Train Ratio:", train_ratio)
print("Validation Ratio:", val_ratio)
print("Test Ratio:", test_ratio)
print("Dataset successfully created!")