#ifndef PYTHONCONSOLE_H
#define PYTHONCONSOLE_H

#include <QPlainTextEdit>
#include <QContextMenuEvent>
#include <QMenu>
#include <QDebug>

class PythonConsole : public QPlainTextEdit
{

    Q_OBJECT

public:
    PythonConsole(QWidget* parent = 0);
    ~PythonConsole();
    void contextMenuEvent(QContextMenuEvent *event);

public slots:
    void slotChangeColorTheme();

private:
    //Context menu actions
    QAction* _clearConsole;
    QAction* _lightTheme;
    QAction* _darkTheme;
    QActionGroup* _colorThemeGroup;

};

#endif // PYTHONCONSOLE_H
