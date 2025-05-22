# -*- coding: utf-8 -*-
# 利用 https://github.com/wkentaro/gdown 这个项目直接下载google drive里的文件

# ## 文件下载
# import gdown
# url = 'https://drive.google.com/file/d/1uFTzwFc3tmS-D7azjMiJcxSfn71BPqKt/view?usp=sharing'
# output_path = 'graph_ML.pk'
# gdown.download(url, output_path, quiet=False,fuzzy=True)

# 文件夹下载
import gdown
url = "https://drive.google.com/drive/folders/1y2N-xV5xzRziM3QejBWrSQgMBQFE1kIr" # 直接下载所需文件夹
gdown.download_folder(url, quiet=True, use_cookies=False)