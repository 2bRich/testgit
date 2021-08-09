#ifndef FUNCCOFIGWINDOW_H
#define FUNCCOFIGWINDOW_H

#include <QWidget>
#include <QTcpSocket>
#include <QRadioButton>
#include "scansetwindow.h"

extern QTcpSocket TcpClient;

namespace Ui {
class FuncCofigWindow;
}

class FuncCofigWindow : public QWidget
{
    Q_OBJECT

public:
    explicit FuncCofigWindow(QWidget *parent = nullptr);
    ~FuncCofigWindow();
    struct scan_info
    {
        char filename[50];
        char filepath[50];
        char scan_date[50];
    }info;
    struct agent_conf{
        char scan_switch;  // 扫描功能开关true为开，false为关
        int scan_num;
        char scan_path[5][50];   //需要扫描的路径，最多5个
        int not_scan_num;
        char not_scan_path[5][50];  //不需要扫描的路径，最多5个
    }conf;

private slots:
    //显示扫描例外的设置界面
    void showScanSetWindow();

    void on_pushButton_clicked();

    void on_buttonBox_rejected();

    void on_buttonBox_accepted();

private:

    //窗口对象
    ScanSetWindow *sc;

    Ui::FuncCofigWindow *ui;
};

#endif // FUNCCOFIGWINDOW_H
