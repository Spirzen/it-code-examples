ServerConfig config = new ServerConfig();
ConfigHistory history = new ConfigHistory();

config.set("maxThreads", "200");
history.backup(config);

config.set("maxThreads", "500");
config.set("timeout", "30s");
history.backup(config);

config.set("maxThreads", "1");
history.undo(config);

System.out.println(config.get("maxThreads")); // 500
