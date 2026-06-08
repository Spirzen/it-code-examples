// Java (хороший пример)
interface Printer {
    void print(String document);
}

interface Scanner {
    String scan(String document);
}

interface Fax {
    void fax(String document);
}

class SimplePrinter implements Printer {
    public void print(String document) {
        System.out.println("Printing: " + document);
    }
}

class AllInOne implements Printer, Scanner, Fax {
    public void print(String document) {
        System.out.println("Printing: " + document);
    }

    public String scan(String document) {
        return "Scanned: " + document;
    }

    public void fax(String document) {
        System.out.println("Faxing: " + document);
    }
}
