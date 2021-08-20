import os
import hashlib
import sys
import shutil
from pyDes import des, PAD_PKCS5, ECB
from pathlib import Path

from core.dbToJson import sqlite_to_json
from core.metaInfo import meta_info
from core.zip import zip_file


def get_private_key() -> str:
    with open('./private_key.txt') as f:
        private_key = f.readline()
        return private_key


def cve_encrpt_tool():
    fill_path_list = []
    cve_file_list = []
    nvd_json_dir = sys.argv[3]
    print("source file 路径 : %s" % nvd_json_dir)
    files_list = os.listdir(nvd_json_dir)
    patern_temp_dir = os.path.join(os.getcwd(), "pattern_temp")
    patern_temp_data_dir = os.path.join(patern_temp_dir, "data")
    if not os.path.exists(patern_temp_dir):
        print("[yz] " + patern_temp_dir)
        os.mkdir(patern_temp_dir)
        os.mkdir(patern_temp_data_dir)
    else:
        shutil.rmtree(patern_temp_dir)
        os.mkdir(patern_temp_dir)
        os.mkdir(patern_temp_data_dir)

    # 扫描.json文件同时创建.cve文件
    for json_file in files_list:
        # print(json_file)
        if os.path.splitext(json_file)[1] == '.json':
            fill_path_list.append(json_file)

    # os.chdir("D:\\PyCharm\\1-My-Workplace\\cveEncrpt\\data_demo")
    if not os.path.exists('nvdcve-0.cve'):
        for i in range(len(fill_path_list)):
            # os.chdir("D:\\PyCharm\\1-My-Workplace\\cveEncrpt\\data_demo")
            cve_file_name = "nvdcve-" + str(i) + '.cve'
            open(os.path.join(patern_temp_data_dir, cve_file_name), 'w+')
            # print("cvefile:", cve_file_name)
            cve_file_list.append(cve_file_name)
            print("创建.cve文件成功")
    else:
        print(".cve文件已经创建!")
    print(len(cve_file_list))
    for json_file, cve_file in zip(fill_path_list, cve_file_list):
        # for json_file in fill_path_list:
        json_file_path = os.path.join(nvd_json_dir, json_file)
        print('正在解析文件: ' + json_file)
        # os.chdir(nvd_json_dir)
        with open(json_file_path, encoding='utf-8') as f1:
            text = f1.readlines()
            text = "".join(text)
            # 密钥des_secret_key
            des_secret_key = get_private_key()
            s = text.encode()
            des_obj = des(des_secret_key, ECB, des_secret_key, padmode=PAD_PKCS5)
            print("===正在加密...===")
            secrets_bytes = des_obj.encrypt(s)
            print("===加密完成！===")
            # 解密
            s = des_obj.decrypt(secrets_bytes)

            # print("加密后的文件内容: ", secrets_bytes)
            # print("解密后的文件内容: ", s.decode())

        print(".cve文件的数量为: ", len(cve_file_list))
        # for cve_file in cve_file_list:
        # print("cve_file: ", cve_file)
        # with open('D:\\PyCharm\\1-My-Workplace\\cveEncrpt\\data\\nvdcve-0.cve', 'w+', encoding='utf-8') as f:
        cve_file_path = os.path.join(patern_temp_data_dir, cve_file)
        with open(cve_file_path, 'w+', encoding='utf-8') as f2:
            print("===写入加密内容到文件...===", cve_file)
            f2.write(str(secrets_bytes))
            print("===写入加密内容完成！===")
        f1.close()
        f2.close()

    print("SHA256加密: ")
    sha256_list = []
    for cve_file in cve_file_list:
        cve_file_path = os.path.join(patern_temp_data_dir, cve_file)
        print("正在处理文件: ", cve_file_path)
        with open(cve_file_path, 'r', encoding='utf-8') as f3:
            text = f3.readlines()
            text = "".join(text)
            t = text.encode()
            data_sha256 = hashlib.sha256(t).hexdigest()
            print("文件sha256值为: ", data_sha256)
            sha256_list.append(data_sha256)
        f3.close()

    # 删除原json文件
    # for json_file in fill_path_list:
    #     if os.path.exists(json_file):
    #         os.remove(json_file)
    #         print("===文件删除成功！===")
    #     else:
    #         print("===文件不存在！===")

    # 产生meta_info.json
    pattern_type = sys.argv[1]
    pattern_version = sys.argv[2]

    meta_info_file_path = os.path.join(patern_temp_dir, "meta_info.json")
    meta_info(meta_info_file_path, pattern_type, pattern_version, cve_file_list, sha256_list)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("python PaternPackgeTool.py [type] [version] [source_path]")
        exit(0)
    if sys.argv[1] not in ('cve', 'baseline', 'vuln'):
        print("type must in {cve, baseline, vuln}")
        exit(0)
    if sys.argv[1] != 'cve':
        if not os.path.exists(sys.argv[3]) or not Path(sys.argv[3]).is_dir():
            print("source_path must directory")
            exit(0)

    if sys.argv[1] == 'cve':
        # 导出数据库数据为JSON
        sqlite_to_json(sys.argv[3])

     # json加密
    cve_encrpt_tool()

    # 文件压缩
    zip_file(os.path.join(os.getcwd(), "pattern_temp"))
