// modules/ModuleLoader.java
public class ModuleLoader {
    private final Map<String, ModuleMetadata> availableModules;
    private final Map<String, LoadedModule> activeModules = new ConcurrentHashMap<>();
    private final File modulesDirectory;
    
    public ModuleLoader(Map<String, ModuleMetadata> availableModules, File modulesDirectory) {
        this.availableModules = availableModules;
        this.modulesDirectory = modulesDirectory;
    }
    
    public CompletableFuture<ModuleInstance> loadModuleAsync(String moduleId) {
        if (activeModules.containsKey(moduleId)) {
            return CompletableFuture.completedFuture(activeModules.get(moduleId).instance);
        }
        
        return CompletableFuture.supplyAsync(() -> {
            ModuleMetadata metadata = availableModules.get(moduleId);
            if (metadata == null) {
                throw new ModuleNotFoundException("Модуль не зарегистрирован в манифесте");
            }
            
            File moduleFile = new File(modulesDirectory, metadata.bundleFileName);
            if (!moduleFile.exists()) {
                downloadModuleBundle(metadata);
            }
            
            ModuleInstance instance = instantiateModule(moduleFile, metadata);
            activeModules.put(moduleId, new LoadedModule(instance, System.currentTimeMillis()));
            return instance;
        });
    }
    
    private void downloadModuleBundle(ModuleMetadata metadata) {
        // Загрузка бандла из CDN с проверкой цифровой подписи
        byte[] bundle = HttpDownloader.downloadWithRetry(
            metadata.cdnUrl,
            metadata.expectedChecksum
        );
        Files.write(new File(modulesDirectory, metadata.bundleFileName).toPath(), bundle);
    }
    
    private record LoadedModule(ModuleInstance instance, long loadedAt) {}
}
