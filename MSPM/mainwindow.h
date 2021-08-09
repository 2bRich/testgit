#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QStandardItemModel>
#include <QStringListModel>
#include <QListView>
#include <QTableView>
#include <QHeaderView>
#include <QAction>
#include <QMenuBar>
#include "addwindow.h"
#include "computerwindow.h"
#include "vieweventwindow.h"
#include <QMetaType>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:



    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    //界面初始化
    void init();
    static void reinit();

private slots:

    //展示添加页面
    void showAddWindow();

    //展示查看事件页面
    void showViewEventWindow();

    //展示计算机管理页面
    void on_actionnew_2_triggered();

private:



    //QStringListModel *Model;

    //QStandardItemModel *ItemModel;

    ViewEventWindow *vi;

    ComputerWindow *co;

    AddWindow *ad;

    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
