class SimplePrinter(IMultiFunctionDevice):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        raise NotImplementedError("This device cannot scan")

    def fax(self, document):
        raise NotImplementedError("This device cannot fax")

    def copy(self, document):
        raise NotImplementedError("This device cannot copy")
