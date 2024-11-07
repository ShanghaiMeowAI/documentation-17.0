import re

def contains_chinese(text):
    """检查字符串中是否包含中文字符"""
    chinese_char_pattern = re.compile(r'[\u4e00-\u9fff]')
    return bool(chinese_char_pattern.search(text))

def process_file(input_path, output_path):
    line_number = 0
    current_msgid = []
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            stripped_line = line.strip()
            if stripped_line:  # Not an empty line
                current_msgid.append(stripped_line)
            else:  # Empty line, check and output the accumulated msgid if any
                if current_msgid:
                    # Check if any of the lines in current_msgid contains Chinese characters
                    if any(contains_chinese(line) for line in current_msgid):
                        start_line = line_number - len(current_msgid) + 1
                        outfile.write(f'#: ../../content/applications/customization/{input_path.split("/")[-1]}:{start_line}\n')
                        if len(current_msgid) == 1:
                            outfile.write(f'msgid "{current_msgid[0]}"\n')
                        else:
                            outfile.write('msgid ""\n')
                            for content in current_msgid:
                                outfile.write(f'"{content}"\n')
                        outfile.write('msgstr ""\n\n')
                    current_msgid = []
            line_number += 1

        # Output the last accumulated msgid if any and it contains Chinese characters
        if current_msgid and any(contains_chinese(line) for line in current_msgid):
            start_line = line_number - len(current_msgid) + 1
            outfile.write(f'#: ../../content/applications/customization/{input_path.split("/")[-1]}:{start_line}\n')
            if len(current_msgid) == 1:
                outfile.write(f'msgid "{current_msgid[0]}"\n')
            else:
                outfile.write('msgid ""\n')
                for content in current_msgid:
                    outfile.write(f'"{content}"\n')
            outfile.write('msgstr ""\n')

# 使用脚本
input_file_path = 'EDI.rst'
output_file_path = 'EDI.po'
process_file(input_file_path, output_file_path)