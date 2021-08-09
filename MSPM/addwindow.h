#ifndef ADDWINDOW_H
#define ADDWINDOW_H

#include <QWidget>
#include <QAbstractButton>
#include <QPushButton>
#include <QString>
#include <computerwindow.h>
#include <QVector>
#include <QTcpSocket>

namespace Ui {
class AddWindow;
}

class AddWindow : public QWidget
{
    Q_OBJECT

public:


    explicit AddWindow(QWidget *parent = nullptr);
    ~AddWindow();

private slots:

    void on_buttonBox_rejected();

    void on_buttonBox_accepted();

//    void on_buttonBox_clicked(QAbstractButton *button);
    void judgeSocketState();    //强制断开连接的处理函数

private:
    Ui::AddWindow *ui;

};



#endif // ADDWINDOW_H
