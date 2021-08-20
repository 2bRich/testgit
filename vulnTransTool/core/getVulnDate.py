import json
import os

from core.dataBase import update_published_date, update_lastModified_date


def get_vuln_date(nvd_json_dir, fill_path_list):
    for json_file in fill_path_list:
        print('parse: ' + json_file)
        json_file_path = os.path.join(nvd_json_dir, json_file)
        json_data = json.load(open(json_file_path, 'rb'))

        for CVE_Item in json_data["CVE_Items"]:
            cve_no = str(CVE_Item["cve"]["CVE_data_meta"]["ID"])
            print("漏洞号cve_no: ", cve_no)

            publishedDate = str(CVE_Item["publishedDate"])
            lastModifiedDate = str(CVE_Item["lastModifiedDate"])
            #print("发布时间publishedDate:", publishedDate)
            #print("最近修改时间lastModifiedDate:", lastModifiedDate)

            update_published_date(publishedDate, lastModifiedDate, cve_no)
            #update_lastModified_date(lastModifiedDate, cve_no)

            print("============================================")
