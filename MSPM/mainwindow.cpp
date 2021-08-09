#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QAction>
#include <QMenuBar>
#include "addwindow.h"

typedef struct computerPara
{
    //计算机ip
    QString computerIp;

    //连接状态
    bool connectStatus;

    //防病毒模式
    bool avMode;

    //事件
    QString event;

}cp;
//通过Q_DECLARE_METATYPE声明后，就可以让自定义的类型设置到QVariant。
//Q_DECLARE_METATYPE(computerPara)
extern  QVector<QString> ipAddr;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    init();
}

MainWindow::~MainWindow()
{
    delete ui;
}


//主页面初始化
void MainWindow::init()
{

    //调整tableView窗口大小和主窗口一致
    ui->tableView->resize(800,700);
    //显示背景网格线设置

    ui->tableView->setShowGrid(true);

    //网格背景画笔
    ui->tableView->setGridStyle(Qt::DashLine);
    //ui->tableView->setGridStyle(Qt::DotLine);

    //表头设置
    QStandardItemModel* model = new QStandardItemModel();
    QStringList labels = QObject::tr("计算机名称,连接状态,防病毒模式,查看事件").simplified().split(",");
    model->setHorizontalHeaderLabels(labels);
    ui->tableView->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);

    //添加表中数据item
    cp m_computer;
    m_computer.computerIp = "192.168.1.1";
    m_computer.connectStatus = "Ture";
    m_computer.avMode = "False";
    m_computer.event = "查看事件";


//    extern  QVector<QString> ipAddr;
//    QVector<QString>::iterator iter;
//    QStandardItem* item;
//    int i = 0;
//    for (iter = ipAddr.begin(); iter != ipAddr.end(); iter++)
//      {
//          qDebug() << *iter;
//          item = new QStandardItem(QString("%1").arg(*iter));
//          model->setItem(i++,0,item);
//          item = new QStandardItem(QString("%1").arg("查看事件"));
//          model->setItem(i,3,item);
//      }
    QStandardItem* item;
    for(int i = 0;i < 10;i++){
        item = new QStandardItem(QString("%1").arg(m_computer.computerIp));
        model->setItem(i,0,item);
        item = new QStandardItem(QString("%1").arg(m_computer.connectStatus ));
        model->setItem(i,1,item);
        item = new QStandardItem(QString("%1").arg(m_computer.avMode));
        model->setItem(i,2,item);
        item = new QStandardItem(QString("%1").arg(m_computer.event));
        model->setItem(i,3,item);
   }
    //解绑，防止点击QTableView单元格多次触发
    disconnect(ui->tableView, SIGNAL(clicked(const QModelIndex &)), this, SLOT(showViewEventWindow()));

    //绑定，点击QTableView单元格触发
    connect(ui->tableView, SIGNAL(clicked(const QModelIndex &)), this, SLOT(showViewEventWindow()));
    ui->tableView->setEditTriggers(QAbstractItemView::NoEditTriggers);
    ui->tableView->setModel(model);
    ui->tableView->show();
}

//显示添加计算机页面
void MainWindow::showAddWindow()
{
     ad = new AddWindow;
     ad->show();
}

//显示计算机管理列表页面
void MainWindow::on_actionnew_2_triggered()
{
    co = new ComputerWindow;
    co->show();
}

//显示查看事件界面
void MainWindow::showViewEventWindow()
{
    vi = new ViewEventWindow;
    vi->show();
}

