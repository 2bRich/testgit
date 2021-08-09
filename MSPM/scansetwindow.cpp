#include "scansetwindow.h"
#include "ui_scansetwindow.h"
#define MANX_SCAN_FILE 5
QVector<QString> not_scan_dir;
ScanSetWindow::ScanSetWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ScanSetWindow)
{
    ui->setupUi(this);
}

ScanSetWindow::~ScanSetWindow()
{
    delete ui;
}

//点击确认按钮，将输入的目录信息加入到已输入目录中
void ScanSetWindow::on_pushButton_clicked()
{
    QString scanFileSet = ui->lineEdit->text();
    if(not_scan_dir.size() <= MANX_SCAN_FILE)
        not_scan_dir.append(scanFileSet);
    ui->plainTextEdit->insertPlainText(scanFileSet += '\n');

//将目录下发到Agent端
    //...
}

//点击ok关闭窗口
void ScanSetWindow::on_buttonBox_accepted()
{
    this->close();
}

void ScanSetWindow::on_buttonBox_rejected()
{
    this->close();
}
