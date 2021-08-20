import os
import sys
import zipfile


def zip_file(pattern_temp_dir):
    # os.chdir("D:\\PyCharm\\1-My-Workplace\\cveEncrpt")
    # print("当前目录:", os.getcwd())
    cve_file_list = []
    nvd_cve_dir = os.path.join(pattern_temp_dir, "data")
    metaInfo_file_path = os.path.join(pattern_temp_dir, "meta_info.json")
    # print("当前工作过目录 : %s" % nvd_cve_dir)
    files_list = os.listdir(nvd_cve_dir)

    for cve_file in files_list:
        # print(json_file)
        #if os.path.splitext(cve_file)[1] == '.cve':
        cve_file_list.append(cve_file)

    # 压缩包的名称,设置压缩方法zipfile.ZIP_DEFLATED

    pattern_zip_name = sys.argv[1] + '_pattern_' + sys.argv[2] + '.zip'
    z_file = zipfile.ZipFile(pattern_zip_name, 'w', zipfile.ZIP_DEFLATED)
    pwd = os.getcwd()
    os.chdir(pattern_temp_dir)
    # 压缩的内容
    for cve_file in cve_file_list:
        print("添加到压缩文件cvefile: ", cve_file)
        z_file.write(os.path.join('data', cve_file))
    z_file.write("meta_info.json")

    print("===添加压缩文件成功！===")
    print("生成的压缩文件路径为: ", os.getcwd())
    z_file.close()
    os.chdir(pwd)
