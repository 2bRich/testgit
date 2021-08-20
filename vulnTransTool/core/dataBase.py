import sqlite3


# 连接数据库，创建表格cve_tb，cpe_match_id_tb
def create_tb():
    # conn = sqlite3.connect("dataBase.db")
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()

    sql1 = " CREATE TABLE IF NOT EXISTS cve_tb(cve_no string primary key not null," \
           "alias_no string, published date, modified date, severity int, cvss string, " \
           "thrtype string, vuln_type string, title string, web_link string, description string," \
           "solution string, cpe_match_id int)"

    sql2 = "CREATE TABLE IF NOT EXISTS cpe_match_id_tb(cve_no string primary key  not null, " \
           "cpe_match_id int, foreign key(cve_no) references cve_tb(cve_no) on delete cascade on update cascade," \
           "foreign key(cpe_match_id) references cve_tb(cpe_match_id) on delete cascade on update cascade)"
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.close()
    conn.commit()
    print("数据库创建成功！")


# 插入主键cve_no数据到表cve_tb，cpe_match_id_tb
def insert_cve_no(cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql1 = "INSERT or IGNORE INTO cve_tb(cve_no) VALUES('%s')" % cve_no
    sql2 = "INSERT or IGNORE INTO cpe_match_id_tb(cve_no) VALUES('%s')" % cve_no
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()
    cursor.close()
    conn.close()
    print("添加数据成功")


# 删除表中所有数据
def remove_data():
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "DELETE FROM cve_tb "
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("删除数据成功！")


# 更新web链接
def update_web_link(value, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "UPDATE cve_tb SET web_link = ? WHERE cve_no = ? "
    cursor.execute(sql, (value, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")


# 更新波及产品列表
def update_cpe_match_id(value, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql1 = "UPDATE cve_tb SET cpe_match_id = ? WHERE cve_no = ? "
    sql2 = "UPDATE cpe_match_id_tb SET cpe_match_id = ? WHERE cve_no = ? "
    cursor.execute(sql1, (value, cve_no))
    cursor.execute(sql2, (value, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")


# 更新漏洞别名
def update_alias_no(value1, value2, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "UPDATE cve_tb SET alias_no = ?,vuln_type = ? WHERE cve_no = ? "
    cursor.execute(sql, (value1, value2, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")


# 更新漏洞类型
def update_vuln_type(value, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "UPDATE cve_tb SET vuln_type = ? WHERE cve_no = ? "
    cursor.execute(sql, (value, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")


# 更新漏洞等级
def update_severity(value, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "UPDATE cve_tb SET severity = ? WHERE cve_no = ? "
    cursor.execute(sql, (value, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")


# 更新漏洞评分
def update_cvss(value, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "UPDATE cve_tb SET cvss = ? WHERE cve_no = ? "
    cursor.execute(sql, (value, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")


# 更新漏洞发布时间和最近修改时间
def update_published_date(value1, value2, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "UPDATE cve_tb SET published = ?, modified = ? WHERE cve_no = ? "
    cursor.execute(sql, (value1, value2, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")


def update_lastModified_date(value, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "UPDATE cve_tb SET modified = ? WHERE cve_no = ? "
    cursor.execute(sql, (value, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")


def update_vuln_description(value, cve_no):
    conn = sqlite3.connect("/dataBase.db")
    cursor = conn.cursor()
    sql = "UPDATE cve_tb SET description = ? WHERE cve_no = ? "
    cursor.execute(sql, (value, cve_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("更新数据成功！")

# if __name__ == '__main__':
# remove_data()
