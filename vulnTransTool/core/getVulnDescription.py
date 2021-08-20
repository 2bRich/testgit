import json
import os

from core.dataBase import update_vuln_description


def get_vuln_description(nvd_json_dir, fill_path_list):
    for json_file in fill_path_list:
        print('parse: ' + json_file)
        json_file_path = os.path.join(nvd_json_dir, json_file)
        json_data = json.load(open(json_file_path, 'rb'))

        for CVE_Item in json_data["CVE_Items"]:
            cve_no = str(CVE_Item["cve"]["CVE_data_meta"]["ID"])
            print("漏洞号cve_no: ", cve_no)

            description_data = CVE_Item["cve"]["description"]["description_data"]
            # print("description_data:", description_data)
            value = description_data[0]['value']
            # print("漏洞描述value:", value)
            # print(type(value))
            update_vuln_description(value, cve_no)

            print("============================================")
