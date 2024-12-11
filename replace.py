import os
import zipfile
from PIL import Image

mods_path = "../../mods"

def make_image_transparent(image_path):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGBA")
            transparent_data = [(255, 255, 255, 0) for _ in range(img.width * img.height)]
            img.putdata(transparent_data)

            backup_path = image_path + ".bak"
            if not os.path.exists(backup_path):
                os.rename(image_path, backup_path)

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

def extract_armor_textures_from_mods(mods_dir, dest_assets_dir):
    for file_name in os.listdir(mods_dir):
        if file_name.endswith('.jar'):
            jar_path = os.path.join(mods_dir, file_name)
            with zipfile.ZipFile(jar_path, 'r') as jar:
                for member in jar.namelist():
                    if member.lower().endswith(('.png', '.jpg', '.jpeg')) \
                       and member.startswith('assets/') \
                       and 'textures/models/armor/' in member:
                        # assets/ 部分を取り除き、assets_dir直下に展開する
                        relative_path = member[len('assets/'):]
                        dest_path = os.path.join(dest_assets_dir, relative_path)
                        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                        with jar.open(member) as src, open(dest_path, 'wb') as dst:
                            dst.write(src.read())

if __name__ == "__main__":
    current_directory = os.getcwd()
    assets_dir = os.path.join(current_directory, "assets")

    # modsフォルダからアーマーテクスチャを抽出
    extract_armor_textures_from_mods(mods_path, assets_dir)

    # 抽出後、assets以下のディレクトリを走査して画像を透明化
    process_directory(assets_dir)
    print("Processing completed.")
