#include "addwindow.h"
#include "ui_addwindow.h"
#include <QWidget>
#include <QMenu>
#include <QDebug>
QVector<QString> ipAddr;//存放ip地址的容器
QTcpSocket TcpClient; //目前单个连接
AddWindow::AddWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AddWindow)
{
    ui->setupUi(this);
}

AddWindow::~AddWindow()
{
    delete ui;
}

//点击cancel关闭此窗口
void AddWindow::on_buttonBox_rejected()
{
    this->close();
}

//点击ok按钮，将ip添加到计算机管理列表中
void AddWindow::on_buttonBox_accepted()
{
    QString ipAddrText = ui->lineEdit->text();

    //建立连接
    if(TcpClient.state() == QAbstractSocket::UnconnectedState)
    {
        //连接到服务器
        TcpClient.connectToHost(ipAddrText, 8080);
        //判断通信套接字的状态，若强制断开会触发stateChanged信号，就连接槽函数judgeSocketState进行相应的处理
        connect(&TcpClient,&QTcpSocket::stateChanged,this,&AddWindow::judgeSocketState);
    }
    if(TcpClient.state() == QAbstractSocket::UnconnectedState)
    {
        TcpClient.disconnectFromHost();      //断开与服务器的连接

        qDebug()<<"连接失败"<<endl;
    }else{
        ipAddr.append(ipAddrText);
    }
    this->close();
}

void AddWindow::judgeSocketState()
{
    //判断服务器端是否已强制断开连接
    if(TcpClient.state() == QAbstractSocket::UnconnectedState)
    {
        TcpClient.disconnectFromHost();      //断开与服务器的连接

        qDebug()<<"断开连接"<<endl;
    }
}


