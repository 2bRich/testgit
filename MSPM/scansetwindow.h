#ifndef SCANSETWINDOW_H
#define SCANSETWINDOW_H

#include <QWidget>
#include <QString>

namespace Ui {
class ScanSetWindow;
}

class ScanSetWindow : public QWidget
{
    Q_OBJECT

public:
    explicit ScanSetWindow(QWidget *parent = nullptr);
    ~ScanSetWindow();

private slots:

    void on_pushButton_clicked();

    void on_buttonBox_accepted();

    void on_buttonBox_rejected();

private:

    Ui::ScanSetWindow *ui;
};

#endif // SCANSETWINDOW_H
