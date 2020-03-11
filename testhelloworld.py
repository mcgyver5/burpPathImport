from mock_callback import MockCallbacks
import unittest
import javax.swing.table.AbstractTableModel
from burp import IBurpExtender
import helloworld

class TestHello(unittest.TestCase):
    def test_hello(self):
        e = helloworld.BurpExtender()
        response = e.hello()
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
        ext = helloworld.BurpExtender()
        ext.registerExtenderCallbacks(mock)
        model = ext.fileTable
        rowCount = model.getRowCount()

        self.assertEqual(rowCount,1)
    
    def test_file_import(self):
        file = open("url_list.txt")
        ext = helloworld.BurpExtender()
        result = ext.process_file(file)
        result_len = len(result)
        self.assertEqual(result_len,10)
    
    def test_first_result(self):
        file = open("url_list.txt")
        ext = helloworld.BurpExtender()
        result = ext.process_file(file)
        firstResult = result[0]
        firstScheme = firstResult[0]
        self.assertEqual(firstScheme,"http")
    
    def test_populate_tablemodel(self):
        mock = MockCallbacks()
        ext = helloworld.BurpExtender()
        ext.registerExtenderCallbacks(mock)
        file = open("url_list.txt")
        result = ext.process_file(file)
        ext.populateTableModel(result)
        tableModel = ext.fileTable.getModel()
        rows = tableModel.getRowCount()
        self.assertEqual(rows, 11)
        
       
if __name__ == '__main__':
    unittest.main()
