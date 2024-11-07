import requests, random, json, time
from hashlib import md5
import re


def make_md5(s, encoding="utf-8"):
    # sign1 = md5().update(s.encode(encoding='utf-8')).hexdigest()
    sign = md5(s.encode(encoding="utf-8")).hexdigest()
    return sign


def translate_api(query, to_lang="en"):
    """
    #可以从https://fanyi-api.baidu.com/manage/developer 获取appid, token

    :param query: 待翻译的字符串
    :param to_lang: 默认翻译成英语en，如果要翻译成汉语，参数改成zh
    :return:
    """
    if query == "" :
        return ""

    appid = "20241107002196610"
    token = "MvYz_hevc3Vh_ifqKGCM"
    from_lang = "zh"  # 自动识别输入语言
    endpoint = "https://fanyi-api.baidu.com/"
    # path1 = 'api/trans/vip/doccount' # 文档翻译API
    path2 = "api/trans/vip/translate"
    url = endpoint + path2
    salt = random.randint(10000, 99999)
    sign = make_md5(appid + query + str(salt) + token)
    params = {
        "appid": appid,
        "q": query,
        "from": from_lang,
        "to": to_lang,
        "salt": salt,
        "sign": sign,
    }
    fanyiheaders = {"Content-Type": "application/x-www-form-urlencoded"}

    # proxies={} 表示强制不使用代理访问，大陆地区不需要使用代理，以便在科学上网时也能顺畅翻译
    r = requests.post(url, params=params, headers=fanyiheaders, proxies={})

    result = r.json()
    dic = eval(json.dumps(result, indent=4, ensure_ascii=False))
    res = "\n".join([i["dst"] for i in dic["trans_result"]])

    # https://api.fanyi.baidu.com/product/111
    # 根据官网文档，标准版QPS（每秒访问量）=1
    time.sleep(1)

    # 此处访问的是翻译好的文字，也就是字符串
    return res



def extract_msgid_msgstr(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    units = []  # 存储所有单元
    current_unit = []  # 当前正在处理的单元
    in_msgid = False  # 标记是否在处理msgid块

    for line in lines:
        line = line.strip()  # 去除每行的前后空格

        # 如果是msgid行，开始新的单元
        if line.startswith('msgid'):
            if current_unit:  # 如果当前有正在处理的单元，保存它
                units.append(current_unit)
            current_unit = [line]  # 新的msgid行开始一个新的单元
            in_msgid = True

        # 如果当前处于msgid块内，且未遇到msgstr
        elif in_msgid:
            if line.startswith('msgstr'):
                # 遇到msgstr行，结束当前单元并不包含msgstr行
                units.append(current_unit)
                current_unit = []  # 重置当前单元
                in_msgid = False
            else:
                # 继续添加当前msgid单元的内容
                current_unit.append(line)

    # 处理文件结束后的最后一个单元（如果有）
    if current_unit:
        units.append(current_unit)

    return units


def extract_strings_from_lines(units):
    # 提取每个单元中每一行的双引号内容
    extracted_strings = []
    for unit in units:
        unit_strings = []
        for line in unit:
            # 使用正则表达式提取双引号中的内容
            matches = re.findall(r'"(.*?)"', line)
            unit_strings.extend(matches)  # 将所有匹配的字符串添加到该单元的列表中
        extracted_strings.append(unit_strings)
    return extracted_strings


def replace_msgstr_content(file_path, output_file_path,units,to_lang):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()  # 读取文件的所有行

    modified_lines = []  # 用于存储修改后的行
    i = 0
    for line in lines:
        line = line.strip()  # 去掉前后空格

        if line.startswith('msgstr'):

            # 找到以msgstr开头的行
            parts = line.split(' ', 1)  # 将msgstr和后面的内容分开
            if len(parts) > 1:
                # 如果有内容在msgstr后面，替换掉
                for idx, unit_strings in enumerate(units[i]):
                    if idx == 0:
                        translation = translate_api(units[i][0],to_lang)
                        result = re.sub(r'\* \*', '**', translation)
                        new_line = parts[0] + ' ' + '"' + result + '"'
                    else:
                        translation = translate_api(unit_strings,to_lang)
                        result = re.sub(r'\* \*', '**', translation)
                        new_line = new_line + "\n"+ '"' + result + '"'
            modified_lines.append(new_line)
            i+=1
        else:
            # 其他行保持不变
            modified_lines.append(line)

    # 保存修改后的文件
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in modified_lines])

    print(f"文件已保存为 {output_file_path}")

dic = ['helpdesk.po','EDI.po','APQP.po']
# 使用方法
for file in dic :
    file_path = file  # 替换为你的文件路径
    msgid_msgstr_units = extract_msgid_msgstr(file_path)

    # 提取每个单元中的双引号内容
    extracted_strings = extract_strings_from_lines(msgid_msgstr_units)

    # 打印提取到的双引号中的内容
    for i, unit_strings in enumerate(extracted_strings):
        print(f"Unit {i + 1}:")
        for string in unit_strings:
            print(f"{string}")
        print('-' * 50)

    to_lang = "th"
    replace_msgstr_content(file_path,"_trans_"+file_path+"_"+to_lang,extracted_strings,to_lang)
    to_lang = "en"
    replace_msgstr_content(file_path,"_trans_"+file_path+"_"+to_lang,extracted_strings,to_lang)




