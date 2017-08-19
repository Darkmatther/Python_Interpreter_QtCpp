#include "PythonConsole.h"

PythonConsole::PythonConsole(QWidget *parent) : QPlainTextEdit(parent)
{

    //Set font to "console style"
    QFont consoleFont("consolas", 8, QFont::Medium, false);
    this->setFont(consoleFont);

    //Set maximum sroll limit for the console
    this->setMaximumBlockCount(10000);

    //Context menu actions
    this->_clearConsole = new QAction(tr("&Clear"), this);
    this->_lightTheme = new QAction(tr("&Light"), this);
    this->_darkTheme = new QAction(tr("&Dark"), this);

    //Group for color theme actions
    this->_colorThemeGroup = new QActionGroup(this);
    this->_colorThemeGroup->addAction(this->_lightTheme);
    this->_colorThemeGroup->addAction(this->_darkTheme);
    this->_lightTheme->setCheckable(true);
    this->_lightTheme->setChecked(true);
    this->_darkTheme->setCheckable(true);

    //Context menu slots
    QObject::connect(this->_clearConsole, SIGNAL(triggered()), this, SLOT(clear()));
    QObject::connect(this->_lightTheme, SIGNAL(triggered()), this, SLOT(slotChangeColorTheme()));
    QObject::connect(this->_darkTheme, SIGNAL(triggered()), this, SLOT(slotChangeColorTheme()));
}


PythonConsole::~PythonConsole()
{
    delete this->_clearConsole;
    delete this->_lightTheme;
    delete this->_darkTheme;
    delete this->_colorThemeGroup;
}


void PythonConsole::contextMenuEvent(QContextMenuEvent *event)
{

    //Get existing (default) context menu
    QMenu* menu = createStandardContextMenu();

    //Create and insert "Clear" action (+ separator) at the head of the existing context menu
    menu->insertSeparator(menu->actions()[0]);
    menu->insertAction(menu->actions()[0], this->_clearConsole);

    //Create and insert a "Color theme" menu with actions at the end of the existing context menu
    menu->addSeparator();
    QMenu* colorTheme = menu->addMenu(tr("&Color theme"));
    colorTheme->addAction(this->_lightTheme);
    colorTheme->addAction(this->_darkTheme);

    //Open context menu
    menu->exec(event->globalPos());
    delete menu;
}


void PythonConsole::slotChangeColorTheme()
{

    QObject* theme = QObject::sender();
    QPalette p = this->palette();

    if (theme == this->_lightTheme)
    {
        p.setColor(QPalette::Base, Qt::white);
        p.setColor(QPalette::Text, Qt::black);
    }
    else if (theme == this->_darkTheme)
    {
        p.setColor(QPalette::Base, Qt::black);
        p.setColor(QPalette::Text, Qt::white);
    }
    this->setPalette(p);

}
