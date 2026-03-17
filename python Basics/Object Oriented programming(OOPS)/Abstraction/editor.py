from abc import ABC,abstractmethod

class Editor:

    @abstractmethod
    def open(self):pass
    @abstractmethod
    def excecute(self):pass
    @abstractmethod
    def debug(self):pass
        
class Vscode(Editor):

    def open(self):
        print("vs code open")

    def excecute(self):
        print("vs code executes")

    def debug(self):
        print("vs code debug")


vs_instance=Vscode()
vs_instance.open()
vs_instance.excecute()
vs_instance.debug()