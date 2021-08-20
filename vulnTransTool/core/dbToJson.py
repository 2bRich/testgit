import json
import os
import sqlite3
import math
from pathlib import Path
import shutil

# 每个文件最多读入的cve个数
max_cve_num = 30000


def sqlite_to_json(source_file_path):
    if not Path(source_file_path).exists():
        os.mkdir(source_file_path)
    else:
        shutil.rmtree(source_file_path)
        os.mkdir(source_file_path)
    #db_path = os.path.join(source_file_path)
    conn = sqlite3.connect("./dataBase.db")
    cur = conn.cursor()
    sql = "SELECT cve_no, alias_no, published, modified, severity, cvss, thrtype, " \
          "vuln_type, title, web_link, description, solution, cpe_match_id FROM cve_tb"
    cur.execute(sql)
    # 返回数据库所有数据
    sqlite_data = cur.fetchall()
    fields = cur.description
    # print(math.ceil(len(data)/max_read_lines))
    nvdcve_file_num = math.ceil(len(sqlite_data) / max_cve_num)
    column_list = []
    for field in fields:
        column_list.append(field[0])
    # for i in range(len(column_list)):
    # print("字段名：", column_list[i])
    # os.chdir("./data_demo")
    print("===开始导出数据...===")
    for i in range(nvdcve_file_num):
        json_file_path = os.path.join(source_file_path, 'nvdcve-demo-' + str(i) + '.json')
        with open(json_file_path, 'w+', encoding='UTF-8') as f:
            for j in range(i * max_cve_num, min((i + 1) * max_cve_num, len(sqlite_data))):
                result = {}
                # print("row: ", data[i])
                # length(0,45000)
                for field_index in range(0, len(column_list)):
                    result[column_list[field_index]] = str(sqlite_data[j][field_index])
                    # print("row[field_index]: ", data[i][field_index])
                    # cve_no = result['cve_no']

                json_data = json.dumps(result, ensure_ascii=False)
                f.write(json_data + '\n')
        pass
        f.close()
    cur.close()
    conn.close()
    print("===数据导出成功！===")
