from burp import IBurpExtenderCallbacks
import java.io.ByteArrayOutputStream as ByteoutputStream
import java.io.OutputStream as JoutputStream
class MockCallbacks(IBurpExtenderCallbacks):

    def addSuiteTab(self,tab):
        pass

    def issueAlert(self,message):
        pass

    def getStderr(self):
        p = ByteoutputStream()
        return p

    def getStdout(self):
        p = ByteoutputStream()
        return p


    def setExtensionName(self,extensionName):
        pass
 
