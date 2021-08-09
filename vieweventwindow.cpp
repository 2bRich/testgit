#include "vieweventwindow.h"
#include "ui_vieweventwindow.h"

ViewEventWindow::ViewEventWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ViewEventWindow)
{
    ui->setupUi(this);
    init();
    //当Agent发送数据时，触发readyRead信号，此时就可以读取Agent发送的数据
    connect(&TcpClient, &QTcpSocket::readyRead, this, &ViewEventWindow::recvData);
}

void ViewEventWindow::init()
{
    ItemModel = new QStandardItemModel(this);

          //接受病毒文件名，目录信息，添加到listview中
//          strList.append("A""A");
//          strList.append("B");
//          strList.append("C");
//          strList.append("D");
//          strList.append("E");
//          strList.append("F");
//          strList.append("G");

          int nCount = strList.size();
          for(int i = 0; i < nCount; i++)
          {
              QString string = static_cast<QString>(strList.at(i));
              QStandardItem *item = new QStandardItem(string);
              ItemModel->appendRow(item);
          }
         ui->listView->setEditTriggers(QAbstractItemView::NoEditTriggers);
         ui->listView->setModel(ItemModel);

}
ViewEventWindow::~ViewEventWindow()
{
    delete ui;
}

void ViewEventWindow::recvData()
{
    struct scan_info
    {
        char filename[50];
        char filepath[50];
        char scan_date[50];
    }info;
    TcpClient.read((char *)&info,sizeof(info));
    qDebug()<<"病毒文件："<<info.filename<<endl;
    qDebug()<<"所在目录："<<info.filepath<<endl;
    qDebug()<<"捕获日期："<<info.scan_date<<endl;
    QString fname(info.filename);
    QString fpath(info.filepath);
    QString date(info.scan_date);
    strList.append("病毒文件："+ fname+"; 所在目录："+fpath+ "; "+date);
    init();
}
