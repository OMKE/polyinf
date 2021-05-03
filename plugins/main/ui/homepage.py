from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from plugins.main.utils.db_utils import connection, use_database, get_all_tables, get_table_data
from core.support.config.config_provider import ConfigProvider

class Homepage(QWidget):
    def __init__(self):
        super().__init__()
        self.current_connection = None
        self.current_cursor = None
        config = ConfigProvider().mysql()
        connection(config['host'], config['user'], config['password'], self)
        use_database(config['database'], self)
        self.tables = get_all_tables(self)
        self.initiate_view()
        self.parentContainer = None

    def initiate_view(self):
        table_horizontal_layout = QHBoxLayout()
        left_side_vertical_layout = QVBoxLayout()

        tables_label = QLabel()
        tables_label.setText("Tables:")
        left_side_vertical_layout.addWidget(tables_label, alignment=Qt.AlignHCenter)

        self.tables_combo_box = QComboBox()
        self.tables_combo_box.setMinimumWidth(200)
        self.tables_combo_box.setEditable(True)
        self.tables_combo_box.addItems(self.tables)
        self.tables_combo_box.currentIndexChanged.connect(self.selected_table_changed)
        completer = QCompleter(self.tables, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.tables_combo_box.setCompleter(completer)

        left_side_vertical_layout.addWidget(self.tables_combo_box)
        left_side_vertical_layout.addStretch(1)

        logout_button = QPushButton('Logout', self)
        logout_button.clicked.connect(self.logout_event)

        left_side_vertical_layout.addWidget(logout_button, alignment=Qt.AlignHCenter)
        
        table_horizontal_layout.addLayout(left_side_vertical_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        table_horizontal_layout.addWidget(self.table)

        self.setLayout(table_horizontal_layout)

    def set_parent(self, parent):
        self.parentContainer = parent

    @pyqtSlot()
    def logout_event(self):
        if self.parentContainer:
            self.parentContainer.logout()

    @pyqtSlot()
    def selected_table_changed(self):
        current_index = self.tables_combo_box.currentIndex()
        if (current_index > len(self.tables) - 1):
            self.tables_combo_box.setCurrentIndex(0)
            self.tables_combo_box.removeItem(current_index)
        else:
            column_names, records = get_table_data(self, self.tables_combo_box.currentText())
            self.update_table(column_names, records)

    def update_table(self, column_names, records):
        num_rows = len(records)
        num_cols = len(column_names)

        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)

        self.table.setHorizontalHeaderLabels(column_names)

        for row in range(num_rows):
            for column in range(num_cols):
                self.table.setItem(row, column, QTableWidgetItem((str(records[row][column]))))
