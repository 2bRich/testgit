import os
import sys
from pathlib import Path

from core.dataBase import create_tb
from core.getCveInfo import get_cve_info
from core.getProductList import get_product_list
from core.getVulnDate import get_vuln_date
from core.getSeverity import get_serverity
from core.getVulnDescription import get_vuln_description

if __name__ == '__main__':
    # os.chdir("../vulnTransTool")
    if len(sys.argv) < 3:
        print("python vulnTransTool.py [type] [data_path]")
        exit(0)
    if sys.argv[1] not in ('nvd', 'cnnvd', 'cnvd'):
        print("[type] must in ('nvd', 'cnnvd', 'cnvd')")
        exit(0)
    if not Path(sys.argv[2]).exists() or not Path(sys.argv[2]).is_dir():
        print("[data_path] not existed")
        exit(0)
    # 创建数据库
    create_tb()

    if sys.argv[1] == 'nvd':
        fill_path_list = []
        # print("当前工作过目录 : %s" % pwd)
        nvd_json_dir = sys.argv[2]
        print("当前工作过目录 : %s" % nvd_json_dir)
        files_list = os.listdir(nvd_json_dir)
        for json_file in files_list:
            print(json_file)
            if os.path.splitext(json_file)[1] == '.json':
                fill_path_list.append(json_file)

        # 获取漏洞id、漏洞别名、漏洞类型、漏洞web链接
        get_cve_info(nvd_json_dir, fill_path_list)
        # 获取漏洞严重程度、漏洞评分
        get_serverity(nvd_json_dir, fill_path_list)
        # 获取漏洞发布时间和最近修改时间
        get_vuln_date(nvd_json_dir, fill_path_list)
        # 获取波及产品列表
        get_product_list(nvd_json_dir, fill_path_list)
        # 获取漏洞描述
        get_vuln_description(nvd_json_dir, fill_path_list)
    elif sys.argv[2] == 'cnnvd':
        pass
    elif sys.argv[2] == 'cnvd':
        pass


