from mock_callback import MockCallbacks
import unittest
import javax.swing.table.AbstractTableModel
from burp import IBurpExtender
import helloworld

class TestHello(unittest.TestCase):
    def setUp(self):
        self.ext = helloworld.BurpExtender()
        self.txtFile = open("url_list.txt")

    def test_hello(self):
        response = self.ext.hello()
        self.assertEqual(response, "hello")
    def test_hello_tablemodel(self):
        e = helloworld.ResourceTableModel()
        response = e.hello_table_model()
        self.assertEqual(response,"hello table model")
    def test_column_count(self):
        e = helloworld.ResourceTableModel()
        column_count = e.getColumnCount()
        self.assertEqual(column_count,6)

    def test_one_row(self):
        mock = MockCallbacks()
        self.ext.registerExtenderCallbacks(mock)
        model = self.ext.fileTable
        rowCount = model.getRowCount()

        self.assertEqual(rowCount,1)
    
    def test_file_import(self):
        result = self.ext.process_file(self.txtFile)
        result_len = len(result)
        self.assertEqual(result_len,10)
    
    def test_first_result(self):
        result = self.ext.process_file(self.txtFile)
        firstResult = result[0]
        firstScheme = firstResult[0]
        self.assertEqual(firstScheme,"http")
    
    def test_populate_tablemodel(self):
        mock = MockCallbacks()
        self.ext.registerExtenderCallbacks(mock)
        result = self.ext.process_file(self.txtFile)
        self.ext.populateTableModel(result)
        tableModel = self.ext.fileTable.getModel()
        rows = tableModel.getRowCount()
        self.assertEqual(rows, 11)
        
    def test_user_clicks_fileChooser(self):
        mock = MockCallbacks()
        self.ext.registerExtenderCallbacks(mock)
        self.ext.fileButtonClick(mock)
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
