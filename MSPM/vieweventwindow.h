#ifndef VIEWEVENTWINDOW_H
#define VIEWEVENTWINDOW_H

#include <QWidget>
#include <QListView>
#include <QStringListModel>
#include <QStandardItemModel>
#include <QTcpSocket>

extern QTcpSocket TcpClient;

namespace Ui {
class ViewEventWindow;
}

class ViewEventWindow : public QWidget
{
    Q_OBJECT

public:
    explicit ViewEventWindow(QWidget *parent = nullptr);
    ~ViewEventWindow();

private slots:
    void recvData();   //接收Agent端传送的结构体信息

private:

    void init();

    QStringListModel *Model;

    QStandardItemModel *ItemModel;

    Ui::ViewEventWindow *ui;

    QStringList strList;
};

#endif // VIEWEVENTWINDOW_H
