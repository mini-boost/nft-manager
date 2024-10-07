import os
import shutil
import random
from constants import TARGET_BASE_DIR


def copy_nft_file(source_dir, season, nft_id):
    # 确保目标目录存在
    target_dir = os.path.join(TARGET_BASE_DIR, season)
    os.makedirs(target_dir, exist_ok=True)

    # 从源目录中选择未标记为使用的文件
    files = [f for f in os.listdir(source_dir)
             if os.path.isfile(os.path.join(source_dir, f)) and not f.endswith('_used')]

    if not files:
        print("没有找到可拷贝的文件。")
        return

    # 随机选择一个文件
    selected_file = random.choice(files)
    source_file_path = os.path.join(source_dir, selected_file)

    # 目标文件路径
    target_file_path = os.path.join(target_dir, f'nft_{nft_id}.jpeg')

    # 拷贝文件
    shutil.copy(source_file_path, target_file_path)
    print(f"拷贝文件 {selected_file} 到 {target_file_path}")

    # 重命名源文件
    new_file_name = selected_file.replace('.jpeg', '_used.jpeg')  # 假设文件是 .jpeg 格式
    new_file_path = os.path.join(source_dir, new_file_name)
    os.rename(source_file_path, new_file_path)
    print(f"重命名文件 {selected_file} 为 {new_file_name}")


# test
if __name__ == '__main__':
    source_directory = 'D:\\CODE\\nft-manager\\NFT_Resource\\1'
    season = '2024'
    nft_id = '12345'
    copy_nft_file(source_directory, season, nft_id)
