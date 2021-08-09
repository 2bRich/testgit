#include "computerwindow.h"
#include "ui_computerwindow.h"

ComputerWindow::ComputerWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ComputerWindow)
{
    ui->setupUi(this);
    init();
}


void ComputerWindow::menuChoiceAction(QAction* act)
{
    if(act->text() == QString("功能配置..."))
    {
        showFuncCofigWindow();
    }
    else
    {
        //...删除计算机
    }
}
//点击计算机管理页面的功能配置，显示功能配置页面
void ComputerWindow::showFuncCofigWindow()
{
    fu = new FuncCofigWindow;
    fu->show();
}

//点击计算机管理页面的删除，删除对应的计算机
void ComputerWindow::deleteComputer()
{
    //...
}
void ComputerWindow::init()
{
    //获得主窗口的大小
    int width = this->width();
    int height = this->height();

    //调整tableView窗口大小和主窗口一致
    ui->tableView->resize(width-50,height-50);

    //显示背景网格线设置

    ui->tableView->setShowGrid(true);

    //网格背景画笔

    ui->tableView->setGridStyle(Qt::DotLine);

    //排序功能
    //ui->tableView->setSortingEnabled(true);
    QStandardItemModel* model = new QStandardItemModel();
    QStringList labels = QObject::tr("计算机IP地址").simplified().split(",");
    model->setHorizontalHeaderLabels(labels);
    ui->tableView->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);


    //定义item
    extern  QVector<QString> ipAddr;
    QVector<QString>::iterator iter;
    QStandardItem* item;
    int i = 0;
    for (iter = ipAddr.begin(); iter != ipAddr.end(); iter++)
      {
          qDebug() << *iter;
          item = new QStandardItem(QString("%1").arg(*iter));
          model->setItem(i++,0,item);
      }


 //   QStandardItem* item = 0;
//    for(int i = 0;i < 10;i++)
//    {
//        item = new QStandardItem(QString("%1").arg(i));
//        model->setItem(i,0,item);
//    }
    ui->tableView->setEditTriggers(QAbstractItemView::NoEditTriggers);
    ui->tableView->setModel(model);

    // 设置tableview鼠标选中形式
    ui->tableView->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui->tableView->setContextMenuPolicy(Qt::CustomContextMenu);
    popMenu = new QMenu(ui->tableView);
    actionUpdateInfo = new QAction;
    actionDelete = new QAction;
    actionUpdateInfo->setText("功能配置...");
    actionDelete->setText("删除计算机");
    popMenu->addAction(actionUpdateInfo);
    popMenu->addAction(actionDelete);
    connect(ui->tableView, SIGNAL(customContextMenuRequested(QPoint)), this, SLOT(contextMenu(QPoint)));
    connect(popMenu, SIGNAL(triggered(QAction*)), this, SLOT(menuChoiceAction(QAction*)));
    ui->tableView->show();
}
void ComputerWindow::contextMenu(QPoint pos)
{
    QModelIndex index = ui->tableView->indexAt(pos);
    if(index.isValid())
    {
        actionUpdateInfo->setEnabled(true);
        actionDelete->setEnabled(true);

    }
    else
    {
        actionUpdateInfo->setEnabled(false);
        actionDelete->setEnabled(false);
    }
     popMenu->exec(QCursor::pos());//菜单出现位置为鼠标右键点击的位置
}
//往管理列表写数据
//void ComputerWindow::init()
//{
//    ItemModel = new QStandardItemModel(this);

//          QStringList strList;
//          QVector<QString>::iterator iter2;
//          extern  QVector<QString> ipAddr;

//          for (iter2 = ipAddr.begin(); iter2 != ipAddr.end(); iter2++)
//          {
//              qDebug() << *iter2;
//              strList.append(*iter2);
//          }
//          int nCount = strList.size();
//          int moveCount = 29;
//          for(int i = 0; i < nCount; i++)
//          {
//              QString string = static_cast<QString>(strList.at(i));
//              QStandardItem *item = new QStandardItem(string);
//              ItemModel->appendRow(item);
//              QPushButton *btn1 = new QPushButton;
//              QPushButton *btn2 = new QPushButton;
//              connect(btn1,&QPushButton::clicked,this,&ComputerWindow::showFuncCofigWindow);
//              connect(btn2,&QPushButton::clicked,this,&ComputerWindow::deleteComputer);
//              btn1->setFixedSize(100,28);
//              btn2->setFixedSize(100,28);
//              btn1->setText("功能配置");
//              btn2->setText("删除");
//              btn1->setParent(this);
//              btn2->setParent(this);
//              btn1->move(400,moveCount);
//              btn2->move(500,moveCount);
//              moveCount +=26;
//          }
//         ui->listView->setEditTriggers(QAbstractItemView::NoEditTriggers);
//         ui->listView->setModel(ItemModel);

//}
ComputerWindow::~ComputerWindow()
{
    delete ui;
}
