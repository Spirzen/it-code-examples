Options options = new Options();
options.addOption("h", "help", false, "Показать справку");
options.addOption(Option.builder("p")
    .longOpt("port")
    .hasArg()
    .type(Number.class)
    .desc("Порт сервера (по умолчанию: 8080)")
    .build());

CommandLineParser parser = new DefaultParser();
CommandLine cmd = parser.parse(options, args);

if (cmd.hasOption("help")) {
    new HelpFormatter().printHelp("server", options);
    return;
}

int port = Integer.parseInt(cmd.getOptionValue("port", "8080"));
