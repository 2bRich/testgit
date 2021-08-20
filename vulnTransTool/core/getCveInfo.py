import json
import os

from core.dataBase import insert_cve_no, update_web_link, update_alias_no, update_vuln_type


# 漏洞号、漏洞别名、漏洞类型、漏洞web_link
def get_cve_info(nvd_json_dir, fill_path_list):
    for json_file in fill_path_list:
        print('parse: ' + json_file)
        # os.chdir(nvd_json_dir)
        json_file_path = os.path.join(nvd_json_dir, json_file)
        json_data = json.load(open(json_file_path, 'rb'))

        for CVE_Item in json_data["CVE_Items"]:
            cve_no = str(CVE_Item["cve"]["CVE_data_meta"]["ID"])
            print("漏洞号cve_no: ", cve_no)
            insert_cve_no(cve_no)

            reference_data = CVE_Item["cve"]["references"]["reference_data"]
            # print("reference_data: ", reference_data)
            if reference_data:
                url_list = []
                # for i in range (len(reference_data)):
                for reference in reference_data:
                    url = reference["url"]
                    # print("web链接url: ", url)
                    url_list.append(url)

            else:
                print("没有url")
            # print(len(url_list))
            web_link = ''
            for i in range(len(url_list)):
                # print("url_list: ", url_list[i])
                url_list[i] += '|'
                web_link += url_list[i]
            # print('web_link: ', web_link)
            update_web_link(web_link, cve_no)

            problemtype = CVE_Item["cve"]["problemtype"]
            # print("漏洞类型problemtype: ", problemtype)
            # print(type(problemtype))

            problemtype_data = CVE_Item["cve"]["problemtype"]["problemtype_data"]
            # print("problemtype_data: ", problemtype_data)
            # print("problemtype_data_length: ", len(problemtype_data))
            # print("problemtype_data[0]: ", problemtype_data[0])

            description = problemtype_data[0]["description"]
            # print("长度: ", len(description))
            if description:
                # print("description: ", description)
                alias_no = description[0]['value']
                # print("漏洞别名alias_no: ", alias_no)

                # 更新漏洞别名和类型
                update_alias_no(alias_no, alias_no, cve_no)

            else:
                # print("漏洞没有别名value")
                continue

            print("============================================")
