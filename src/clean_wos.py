import os
import re
from collections import defaultdict


def read_single_wos_file(file_path):
    """读取单个WoS导出的txt文件，分割为单个文献条目"""
    entries = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        raw_entries = content.split("PT ")
        for part in raw_entries:
            if not part.strip():
                continue
            full_entry = "PT " + part.strip() + "\n"
            if full_entry.endswith("ER\n"):
                entries.append(full_entry)
    except Exception as e:
        print(f"⚠️ 读取文件失败: {os.path.basename(file_path)} | 错误: {str(e)}")
    return entries


def extract_field(entry, field_code):
    """从单个文献条目中提取指定字段的值"""
    pattern = re.compile(rf'^{field_code} (.*?)(?=\n[A-Z][A-Z0-9] |\nER\n)', re.DOTALL | re.MULTILINE)
    match = pattern.search(entry)
    if match:
        return match.group(1).strip().replace('\n   ', ' ')
    return None


def is_valid_entry(entry):
    """检查文献条目是否完整（核心字段必须存在）"""
    required_fields = ['UT', 'TI', 'AU', 'SO', 'PY']
    for field in required_fields:
        if not extract_field(entry, field):
            return False
    return True


# ====================== 新增：分成5个文件的函数 ======================
def split_into_5_parts(entries, output_dir):
    """将文献列表均匀分成5份，并保存为5个WoS格式文件"""
    total = len(entries)
    part_size = total // 5
    parts = []

    # 分成5份
    for i in range(5):
        start = i * part_size
        if i == 4:
            end = total  # 最后一份把剩下的都包含
        else:
            end = (i + 1) * part_size
        parts.append(entries[start:end])

    # 逐个保存
    for idx, part in enumerate(parts, 1):
        filename = f"cleaned_wos_part_{idx}.txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("FN Clarivate Analytics Web of Science\nVR 1.0\n\n")
            for entry in part:
                f.write(entry + "\n")
        print(f"✅ 已生成：{filename}  | 文献数量：{len(part)} 篇")


# ====================================================================

def clean_wos_data(input_dir, output_dir):
    all_entries = []
    file_stats = defaultdict(int)

    print(f"📂 正在扫描文件夹: {input_dir}")
    for filename in os.listdir(input_dir):
        if filename.startswith("savedrecs") and filename.endswith(".txt"):
            file_path = os.path.join(input_dir, filename)
            entries = read_single_wos_file(file_path)
            file_stats['total_files'] += 1
            file_stats['raw_entries'] += len(entries)
            all_entries.extend(entries)
            print(f"✅ 读取文件: {filename} | 包含文献: {len(entries)} 篇")

    if file_stats['raw_entries'] == 0:
        print("❌ 未找到任何有效文献数据")
        return

    # 过滤残缺
    valid_entries = []
    for entry in all_entries:
        if is_valid_entry(entry):
            valid_entries.append(entry)
        else:
            file_stats['invalid_entries'] += 1

    # 去重
    unique_entries = {}
    for entry in valid_entries:
        wos_id = extract_field(entry, 'UT')
        if wos_id not in unique_entries:
            unique_entries[wos_id] = entry
        else:
            file_stats['duplicate_entries'] += 1

    # 转为列表
    final_entries = list(unique_entries.values())

    # ====================== 自动分成5个文件 ======================
    print("\n📌 开始自动分成5个文件...")
    split_into_5_parts(final_entries, output_dir)

    # 统计报告
    print("\n" + "=" * 50)
    print("📊 数据清洗 + 分割完成")
    print("=" * 50)
    print(f"处理文件总数: {file_stats['total_files']} 个")
    print(f"原始文献总数: {file_stats['raw_entries']} 篇")
    print(f"过滤残缺文献: {file_stats['invalid_entries']} 篇")
    print(f"去除重复文献: {file_stats['duplicate_entries']} 篇")
    print(f"最终保留文献: {len(final_entries)} 篇")
    print(f"已自动分割为：5个小文件")
    print("=" * 50)


if __name__ == "__main__":
    INPUT_DIRECTORY = r"E:\txt"
    OUTPUT_DIRECTORY = r"E:\txt"  # 5个文件也保存在这里
    clean_wos_data(INPUT_DIRECTORY, OUTPUT_DIRECTORY)