from burp import IBurpExtender
from java.io import PrintWriter
from java.lang import RuntimeException

class BurpExtender(IBurpExtender):
    
    def	registerExtenderCallbacks(self, callbacks):
    
        # set our extension name
        callbacks.setExtensionName("My New Hello world sample extension")
        
        # obtain our output and error streams
        stdout = PrintWriter(callbacks.getStdout(), True)
        stderr = PrintWriter(callbacks.getStderr(), True)
        
        # write a message to our output stream
        stdout.println("Hello output")
        
        # write a message to our error stream
        stderr.println("Hello errors")
        
        # write a message to the Burp alerts tab
        callbacks.issueAlert("Hello alerts")
        
