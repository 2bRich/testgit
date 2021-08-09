#ifndef COMPUTERWINDOW_H
#define COMPUTERWINDOW_H

#include "funccofigwindow.h"
#include "addwindow.h"
#include <QWidget>
#include <QStandardItemModel>
#include <QListView>
#include <QTableView>
#include <QStringListModel>
#include <QDialogButtonBox>
#include <QPushButton>
#include <QDebug>
#include <QVector>
#include <QMenu>
#include <QAction>

namespace Ui {
class ComputerWindow;
}

class ComputerWindow : public QWidget
{
    Q_OBJECT

public:
    explicit ComputerWindow(QWidget *parent = nullptr);
    ~ComputerWindow();

private slots:

    //右键菜单栏
    void contextMenu(QPoint);

    //显示功能配置界面
    void showFuncCofigWindow();

    //删除计算机
    void deleteComputer();

    //执行右键菜单
    void menuChoiceAction(QAction*);

private:
    QAction *actionUpdateInfo;
    QAction *actionDelete;
    QMenu *popMenu;

    //界面初始化
    void init();

    //list数据模型
    QStringListModel *Model;

    //保存数据
    QStandardItemModel *ItemModel;

    //窗口对象
    FuncCofigWindow *fu;

    Ui::ComputerWindow *ui;
};

#endif // COMPUTERWINDOW_H
