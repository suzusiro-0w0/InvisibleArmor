import os
from PIL import Image

def make_image_transparent(image_path):
    try:
        with Image.open(image_path) as img:
            # 画像をRGBAモードに変換
            img = img.convert("RGBA")
            # 元の解像度を保持したまま透明化
            transparent_data = [(255, 255, 255, 0) for _ in range(img.width * img.height)]
            img.putdata(transparent_data)
            
            # 元のファイルをバックアップ
            backup_path = image_path + ".bak"
            if not os.path.exists(backup_path):  # すでにバックアップがない場合のみ保存
                os.rename(image_path, backup_path)
            
            # 透明画像として保存
            img.save(image_path)
            print(f"Processed: {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                make_image_transparent(file_path)

if __name__ == "__main__":
    # 現在のディレクトリにあるAssetsディレクトリから
    current_directory = os.path.join(os.getcwd(), "assets")
    print(f"Starting from directory: {current_directory}")
    process_directory(current_directory)
    print("Processing completed.")
