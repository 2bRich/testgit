import json
import time


def meta_info(filename, pattern_type, pattern_version, cve_file_list, sha256_list):
    with open(filename, 'w+', encoding='UTF-8') as f:
        meta_info_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("meta_info创建时间为: ", meta_info_create_time)
        meta_info = {}
        meta_info['pattern_type'] = pattern_type
        meta_info['pattern_version'] = pattern_version
        meta_info['date'] = meta_info_create_time

        meta_info['sha256'] = []
        temp_dict = {}
        for length in range(len(cve_file_list)):
            temp_dict['path'] = cve_file_list[length]
            temp_dict['sha256'] = sha256_list[length]
            meta_info['sha256'].append(temp_dict.copy())
        # print(meta_info['sha256'])
        json_data = json.dumps(meta_info, ensure_ascii=False)
        f.write(json_data)
        print("===meta_info写入完成!===")
        f.close()

