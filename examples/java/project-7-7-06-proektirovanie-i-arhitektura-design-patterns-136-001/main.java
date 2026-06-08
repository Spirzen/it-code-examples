interface ReportExporter {
    void export(String payload);
}

class PdfExporter implements ReportExporter {
    @Override
    public void export(String payload) {
        System.out.println("PDF export: " + payload);
    }
}

class CsvExporter implements ReportExporter {
    @Override
    public void export(String payload) {
        System.out.println("CSV export: " + payload);
    }
}

abstract class ExportJob {
    protected abstract ReportExporter createExporter();

    public final void run(String payload) {
        ReportExporter exporter = createExporter();
        exporter.export(payload);
    }
}

class PdfExportJob extends ExportJob {
    @Override
    protected ReportExporter createExporter() {
        return new PdfExporter();
    }
}

class CsvExportJob extends ExportJob {
    @Override
    protected ReportExporter createExporter() {
        return new CsvExporter();
    }
}
