class ReportService {
    private final java.time.Clock clock;

    ReportService(java.time.Clock clock) {
        this.clock = clock;
    }

    String filename() {
        var date = java.time.LocalDate.now(clock);
        return "report-" + date + ".csv";
    }
}

// в тесте: Clock.fixed(Instant.parse("2020-01-15T00:00:00Z"), ZoneOffset.UTC)
