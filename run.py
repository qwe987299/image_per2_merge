from PIL import Image
import os
import time

# 設定要處理的目錄
src_dir = "src"
build_dir = "build"

# 取得目錄下的所有圖片檔案
images = [os.path.join(src_dir, file) for file in os.listdir(
    src_dir) if file.endswith(('jpeg', 'png', 'jpg'))]

# 如果沒有圖片，退出程式
if len(images) == 0:
    print("當前目錄下沒有圖片")
    time.sleep(2)  # 停留兩秒
    exit()

# 如果圖片總數為單數，最後一張不合併
if len(images) % 2 == 1:
    images = images[:-1]

# 每兩張圖片合併
for i in range(0, len(images), 2):
    image1 = Image.open(images[i])
    image2 = Image.open(images[i+1])
    width = image1.width + image2.width
    height = image1.height
    new_image = Image.new('RGB', (width, height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1.width, 0))
    output_path = os.path.join(build_dir, f'merge_{i//2}.jpg')
    new_image.save(output_path)

# 刪除 src 目錄下的所有圖片檔案
for image in images:
    os.remove(image)

# 使用檔案總管打開 build 目錄
os.startfile(build_dir)
