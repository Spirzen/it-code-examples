ExecutorService ioPool = Executors.newFixedThreadPool(8);

CompletableFuture<User> userFuture = CompletableFuture
    .supplyAsync(() -> loadUser(id), ioPool);

CompletableFuture<List<Order>> ordersFuture = CompletableFuture
    .supplyAsync(() -> loadOrders(id), ioPool);

CompletableFuture<Profile> profileFuture = userFuture
    .thenCombine(ordersFuture, Profile::new);

Profile profile = profileFuture
    .orTimeout(3, TimeUnit.SECONDS)
    .exceptionally(ex -> Profile.empty())
    .join();
