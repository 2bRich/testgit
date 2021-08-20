# 获取漏洞严重等级、漏洞评分
import json
import os

from core.dataBase import update_cvss, update_severity


def get_serverity(nvd_json_dir, fill_path_list):
    for json_file in fill_path_list:
        print('parse: ' + json_file)
        json_file_path = os.path.join(nvd_json_dir, json_file)
        json_data = json.load(open(json_file_path, 'rb'))

        for CVE_Item in json_data["CVE_Items"]:
            cve_no = str(CVE_Item["cve"]["CVE_data_meta"]["ID"])
            print("漏洞号cve_no: ", cve_no)

            impact = CVE_Item["impact"]
            # print("impact: ", impact)
            if impact:
                severity = impact['baseMetricV2']['severity']
                # print(type(severity))
                update_severity(severity, cve_no)
                print("漏洞严重程度severity: ", severity)
                try:
                    cvssV3 = impact['baseMetricV3']['cvssV3']
                    baseScore = str(cvssV3['baseScore'])
                    # print("漏洞评分V3：", baseScore)
                    update_cvss(baseScore, cve_no)
                except:
                    cvssV2 = impact['baseMetricV2']['cvssV2']
                    baseScore = str(cvssV2['baseScore'])
                    # print("漏洞评分V2：", baseScore)
                    update_cvss(baseScore, cve_no)
            else:
                print("没有漏洞的严重程度severity")

            print("============================================")
