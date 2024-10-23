import os
import shutil
import random
from constants import TARGET_BASE_DIR


def create_nft_by_season_template(nft_template_dir, season_id, nft_id):
    # 确保目标目录存在
    target_dir = os.path.join(TARGET_BASE_DIR, season_id)
    os.makedirs(target_dir, exist_ok=True)

    # 从源目录中选择未标记为使用的文件
    files = [f for f in os.listdir(nft_template_dir)
             if os.path.isfile(os.path.join(nft_template_dir, f)) and not f.endswith('_used')]

    if not files:
        print("没有找到可拷贝的文件。")
        return

    # 随机选择一个文件
    selected_file = random.choice(files)
    source_file_path = os.path.join(nft_template_dir, selected_file)

    # 目标文件路径
    target_file_path = os.path.join(target_dir, f'nft_{nft_id}.jpeg')

    # 拷贝文件
    shutil.copy(source_file_path, target_file_path)
    print(f"拷贝文件 {selected_file} 到 {target_file_path}")

    # 重命名源文件
#     new_file_name = selected_file.replace('.jpeg', '_used.jpeg')  # 假设文件是 .jpeg 格式
#     new_file_path = os.path.join(nft_template_dir, new_file_name)
#     os.rename(source_file_path, new_file_path)
#     print(f"重命名文件 {selected_file} 为 {new_file_name}")


# test
if __name__ == '__main__':
    nft_template_directory = 'D:\\code\\nft-manager\\nft_template'
    season_id = '1'
    nft_id = '12345'
    create_nft_by_season_template(nft_template_directory, season_id, nft_id)
