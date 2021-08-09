#include "funccofigwindow.h"
#include "ui_funccofigwindow.h"
extern QVector<QString> not_scan_dir;

FuncCofigWindow::FuncCofigWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::FuncCofigWindow)
{
    ui->setupUi(this);
}

FuncCofigWindow::~FuncCofigWindow()
{
    delete ui;
}


void FuncCofigWindow::showScanSetWindow()
{
    sc = new ScanSetWindow;
    sc->show();
}

//点击扫描例外，显示扫描例外的设置界面
void FuncCofigWindow::on_pushButton_clicked()
{
    showScanSetWindow();
}

//点击Cancel按钮关闭当前窗口
void FuncCofigWindow::on_buttonBox_rejected()
{
    this->close();
}

//点击ok，向agent下发配置
void FuncCofigWindow::on_buttonBox_accepted()
{
    conf.scan_num=1;
    strcpy(conf.scan_path[0],"/home");
    conf.not_scan_num=not_scan_dir.size();
    for (int i=0;i<not_scan_dir.size();i++) {
        strcpy(conf.not_scan_path[i],not_scan_dir[i].toLatin1().data());
    }
    if(ui->radioButton->isChecked())
        conf.scan_switch = 'Y';
    else
        conf.scan_switch = 'N';
    TcpClient.write((char*)&conf,sizeof (conf));//下发配置
    this->close();
}
