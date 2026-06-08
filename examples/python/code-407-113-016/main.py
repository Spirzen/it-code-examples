# Python (хороший пример)
class IPrinter:
    def print(self, document):
        pass

class IScanner:
    def scan(self, document):
        pass

class IFax:
    def fax(self, document):
        pass

class ICopy:
    def copy(self, document):
        pass

class SimplePrinter(IPrinter):
    def print(self, document):
        print(f"Printing: {document}")

class AllInOneDevice(IPrinter, IScanner, IFax, ICopy):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

    def fax(self, document):
        print(f"Faxing: {document}")

    def copy(self, document):
        print(f"Copying: {document}")
