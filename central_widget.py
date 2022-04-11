# Central Widget
# - Created by J.Moon 20200413
# - A customizable widget intended to be the main app widget
# -- this only contains GUI functions and elements

ENABLE_CURRENT_SENSOR_CONFIG_WIDGET = 0


# Module Imports
try:
    import PySide2
    from pyqtgraph.Qt import QtGui, QtCore
    QtWidgets = QtGui # PyQt5/ Pyside2
except:
    try:
        import PyQt5
        from pyqtgraph.Qt import QtWidgets, QtGui, QtCore
    except:
        # print("Reverting to PyQt4")
        import PyQt4 # Force pyqtgraph to use PyQt4 (and not PySide)
        from pyqtgraph.Qt import QtGui, QtCore
        QtWidgets = QtGui # PyQt5 to PyQt4 patch
import os


from hex_files import hex_file_in

# CentralWidget: This is a customizable widget designed as the widget that will change from app to app
# - you may still need to use the MainAppWidget class to acesses some resources.
# - this class is a subclass of QFrame
class CentralWidget(QtWidgets.QFrame):
    def __init__(self):    # Standard Python Function, called at the instantiation of a class
        super(CentralWidget, self).__init__()      # Calls the basic Widget Init Sequence
        # Initialize Variables
        self.init_system()
        # Create Widgets
        self.init_widgets()
        # Assign Widgets to a local layout
        self.arrange_widgets()
        # Assign Local Widget Callbacks
        self.init_callbacks()

    # ======= Widget Creation/ Arrangement =START=
    def init_system(self):
        pass

    def init_widgets(self):
        self.open_button = QtWidgets.QPushButton("open hex/hxf file")
        pass

    def arrange_widgets(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.open_button)
        self.setLayout(self.layout)
        pass
    # ======= Widget Creation/ Arrangement ==END==

    # ======= Widget Status =START=

    # ======= Widget Status ==END==

    # ======= Callback Assignments =START=
    def init_callbacks(self):
        self.open_button.clicked.connect(self.open_button_cb)
        pass
    # ======= Callback Assignments ==END==

    # ======= Callback Implementations =START=
    def open_button_cb(self):
        print("open button: select file")
        self.file_select_title_text = "Select Firmware File"
        self.file_select_default_directory = QtCore.QDir().homePath()
        self.file_select_name_filter = "Hex files (*.hex *.hxf)"
        self.selected_file = str(QtWidgets.QFileDialog.getOpenFileName(self, self.file_select_title_text, self.file_select_default_directory, self.file_select_name_filter))
        base_file_name = os.path.basename(self.selected_file) # File name without the directory path
        # self.selected_file = self.file_select.getOpenFileName(self, 'Select Firmware File', 'c:\\',"Hex files (*.hex)")
        if self.selected_file:
            hex_file_in.import_log_file(self.selected_file)
        else:
            print("could not open file")
    # ======= Callback Implementations ==END==
