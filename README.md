总共包含两个工具：
1.CveImporter为cve漏洞导入工具
2.PatternPackager为pattern打包工具

操作步骤：
1.先利用CveImporter将.json文件导入到数据库，脚本运行参数为
python [参数1:默认值] [参数2：类型] [漏洞json文件的存放路径]
如： python .\CveImporter.py nvd 'D:\\PyCharm\\1-My-Workplace\\vulnTransTool\\json_file_demo'

其中：数据库的名称默认为dataBase.db；

2.利用PatternPackager将数据从数据库导出为json文件，然后加密生成.cve文件，最后将所有的.cve文件打包、压缩，脚本运行参数为：
python [参数值:默认值] [参数2:类型] [参数3:版本号] [参数4:导出的json文件将要存放的路径]
如：python .\PatternPackager.py cve 0.0.1 'D:\\PyCharm\\1-My-Workplace\\vulnTransTool\\data_demo'，同时，加密的密钥需要用户在工作目录下private_key.txt中添加，密钥的规则为字符串，且字符串长度为8的倍数；

其中：.cve文件的默认保存目录为/pattern_temp/data；生成的压缩文件.zip中的meta_info中存放.cve文件的sha256；
          
