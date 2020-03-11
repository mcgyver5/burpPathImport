from burp import IBurpExtender
from java.io import PrintWriter
from java.lang import RuntimeException
from javax.swing.table import AbstractTableModel
from javax.swing import JFileChooser
from javax.swing import JPanel
from javax.swing import JLabel
from javax.swing import JButton
from javax.swing import JTable
from urlparse import urlparse

class BurpExtender(IBurpExtender):
    
    #
    # implement IBurpExtender
    #
    def hello(self):
        return "hello"
    def process_file(self,file):
        freshrows = []
        # return list of list of file parts
        for url in file:
            result = urlparse(url)
            scheme = result[0]
            domain = result[0]
            path = result[0]
            params = ''
            query = ''
            fragment = ''
            next = [scheme,domain,path,params,query,fragment]
            freshrows.append(next)
        return freshrows

    def	registerExtenderCallbacks(self, callbacks):
    
        # set our extension name
        callbacks.setExtensionName("Hello world extension")
        
        # obtain our output and error streams
        stdout = PrintWriter(callbacks.getStdout(), True)
        stderr = PrintWriter(callbacks.getStderr(), True)
        
        # write a message to our output stream
        stdout.println("Hello output")
        
        # write a message to our error stream
        stderr.println("Hello errors")
        
        # write a message to the Burp alerts tab
        callbacks.issueAlert("Hello alerts")
        
        #create and populate a jtable:
        initial_row = ['http', 'www.meetup.com', 'PyMNtos-Twin-Cities-Python-User-Group/events/267977020/','','','']
        self.fileTable = JTable(ResourceTableModel(initial_row))
        self.infoPanel = JPanel()
        footerPanel = JPanel()
        footerPanel.add(JLabel("by Tim mcgyver5 McGuire"))
        self._chooseFileButton = JButton("OPEN WAR FILE", actionPerformed=self.fileButtonClick)
        self.infoPanel.add(JLabel("THIS IS INFORMATION PANE"))
        self.infoPanel.add(self._chooseFileButton)

        self._chooseFileButton.setEnabled(True)

    def populateTableModel(self,results):
        tableModel = self.fileTable.getModel()
        for row in results:
            tableModel.addRow(row)

    def fileButtonClick(self,callbacks):
        fileTypeList = ["war","ear","zip","txt","json"]
        warFilter = FileNameExtensionFilter("war", fileTypeList)
        fileChooser = JFileChooser()
        fileChooser.addChoosableFileFilter(warFilter)
        result = fileChooser.showOpenDialog(self._splitpane)

        if result == JFileChooser.APPROVE_OPTION:
            f = fileChooser.getSelectedFile()
            fileName = f.getPath()
            self.populateJTable(f)

class ResourceTableModel(AbstractTableModel):

    COLUMN_NAMES = ('Scheme','domain','path', 'params','query','fragment')

    def __init__(self, *rows):
        self.data = list(rows)

    def getRowCount(self):
        return len(self.data)

    def getValueAt(self, rowIndex, columnIndex):
        row_values = self.data[rowIndex-1]
        return row_values[columnIndex -1]

    def hello_table_model(self):
        return "hello table model"

    def getColumnCount(self):
        return len(self.COLUMN_NAMES)

    def getColumnName(self, columnIndex):
        return self.COLUMN_NAMES[columnIndex]

    def addRow(self, row=None):
        self.data.append(row)
        self.fireTableRowsInserted(len(self.data) -1, len(self.data )-1)

