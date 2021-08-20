import json
import os.path

from core.dataBase import update_cpe_match_id


def get_product_list(nvd_json_dir, fill_path_list):

    for json_file in fill_path_list:
        print('parse: ' + json_file)
        json_file_path = os.path.join(nvd_json_dir, json_file)
        json_data = json.load(open(json_file_path, 'rb'))

        for CVE_Item in json_data["CVE_Items"]:
            cve_no = str(CVE_Item["cve"]["CVE_data_meta"]["ID"])
            print("漏洞号cve_no: ", cve_no)

            nodes = CVE_Item["configurations"]["nodes"]
            # print("nodes: ", nodes)
            for node in nodes:
                cpe23Uri_list = []
                # print(node)
                try:
                    cpe_match = node["cpe_match"]
                    #print("cpe_match1的长度: ", len(cpe_match))
                    # print("cpe_match1: ", cpe_match)
                    for length in range(len(cpe_match)):
                        cpe23Uri = cpe_match[length]['cpe23Uri']
                        #print("波及产品list: ", cpe23Uri)
                        cpe23Uri_list.append(cpe23Uri)

                except:
                    for child in node["children"]:
                        try:
                            cpe_match = child["cpe_match"]
                            # print("cpe_match2: ", cpe_match)
                            #print("cpe_match2的长度: ", len(cpe_match))
                            for length in range(len(cpe_match)):
                                cpe23Uri = cpe_match[length]['cpe23Uri']
                                #print("波及产品list--c: ", cpe23Uri)
                                cpe23Uri_list.append(cpe23Uri)
                        except:
                            # print('chilren not found cpe_match')
                            # print(child)
                            continue
                #print(len(cpe23Uri_list))
                cpe = ''
                for i in range(len(cpe23Uri_list)):
                    cpe = cpe + cpe23Uri_list[i] + ' '
                #print(cpe)
                update_cpe_match_id(cpe, cve_no)
            print("============================================")
