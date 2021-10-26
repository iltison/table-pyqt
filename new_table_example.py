from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Delegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, owner, choices):
        super().__init__(owner)
        self.items = choices

    def paint(self, painter, option, index):
        if isinstance(self.parent(), QtWidgets.QAbstractItemView):
            self.parent().openPersistentEditor(index)
        super(Delegate, self).paint(painter, option, index)

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QComboBox(parent)
        editor.currentIndexChanged.connect(self.commit_editor)
        editor.addItems(self.items)
        return editor

    def commit_editor(self):
        editor = self.sender()
        self.commitData.emit(editor)

    def setEditorData(self, editor, index):
        value = index.data(QtCore.Qt.DisplayRole)
        num = self.items.index(value)
        editor.setCurrentIndex(num)

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class Model(QtCore.QAbstractTableModel):
    ActiveRole = QtCore.Qt.UserRole + 1
    def __init__(self, datain, headerdata, parent=None):
        super().__init__()
        self.arraydata = datain
        self.headerdata = headerdata
    
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.headerdata[section])
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid(): return 0
        return len(self.arraydata)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid(): return 0
        if len(self.arraydata) > 0:
            return len(self.arraydata[0])
        return 0

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self.arraydata[index.row()][index.column()])

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        """Отображение данных в таблице. Условия добавлять сюда 

        Args:
            index ([type]): [description]
            value ([type]): [description]
            role ([type], optional): [description]. Defaults to QtCore.Qt.EditRole.

        Returns:
            [type]: [description]
        """
        r = re.compile(r"^[0-9]\d*(\.\d+)?$")
        if role == QtCore.Qt.EditRole and value != "":
            if index.column() in (0, 1):
                self.arraydata[index.row()][index.column()] = value
                self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
                return True
            else:
                if index.column() == 2:
                    if r.match(value) and (0 < float(value) <= 1):
                        self.arraydata[index.row()][index.column()] = value
                        self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
                        return True
                else:
                    if r.match(value):
                        self.arraydata[index.row()][index.column()] = value
                        self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
                        return True
        return False

    def print_arraydata(self):
        print(self.arraydata)

    def insert_row(self, data, position, rows=1):
        self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i, e in enumerate(data):
            self.arraydata.insert(i+position, e[:])
        self.endInsertRows()
        return True

    def remove_row(self, positions, rows=1):
        for position in positions:
            self.beginRemoveRows(QtCore.QModelIndex(), position, position)
            self.arraydata = self.arraydata[:position] + self.arraydata[position + rows:]
            self.endRemoveRows()
        return True

    def append_row(self, data):
        self.insert_row([data], self.rowCount())


class Main(QtWidgets.QDialog):
    def __init__(self, data_struct, parent=None):
        super().__init__(parent)
        from Ui_new_table_example import Ui_Form
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        
        # табличные данные
        self.data_struct = data_struct
        # combobox value
        self.choices = ['type_7', 'type_2', 'type_3', 'type_4', 'type_5']
        # header value
        self.header = ['name', 'type', 'var1', 'var2', 'var5'] 
        
        # заполнение таблицы
        self.tableview = self._ui.tableView
        self.createTable()

        # сигналы кнопок
        self._ui.addbtn.clicked.connect(self.insert_row)
        self._ui.deletebtn.clicked.connect(self.remove_row)
        self._ui.exportbtn.clicked.connect(self.export_tv)

    def createTable(self):
        """Создание таблицы 
        """
        tablemodel = Model(self.data_struct, self.header, self)
        self.tableview.setModel(tablemodel)
        self.tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableview.resizeRowsToContents()
        # Добавление combobox в 2(1) столбец
        self.tableview.setItemDelegateForColumn(1, Delegate(self.tableview, self.choices))

    def export_tv(self):
        """Получение измененных табличных данных

        Returns:
            [List]: Измененная таблица
        """
        print(self.tableview.model().arraydata)
        return self.tableview.model().arraydata

    def remove_row(self):
        r = self.tableview.selectionModel().selectedRows()
        rows = sorted(set(index.row() for index in self.tableview.selectedIndexes()),reverse=True)
        self.tableview.model().remove_row(rows)

    def insert_row(self):
        self.tableview.model().append_row(['Name', self.choices[0], 0.0, 0.0, 0.0])

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main([['Name', 'type_2', 0.0, 0.0, 0.0],['Name', 'type_3', 0.0, 0.0, 0.0]])
    main.show()
    sys.exit(app.exec_())