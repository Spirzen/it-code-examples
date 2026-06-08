ProxySelector customSelector = new ProxySelector() {
    @Override
    public List<Proxy> select(URI uri) {
        if (uri.getHost().endsWith(".intranet")) {
            return List.of(Proxy.NO_PROXY);
        }
        return List.of(new Proxy(Proxy.Type.HTTP, new InetSocketAddress("proxy.local", 3128)));
    }

    @Override
    public void connectFailed(URI uri, SocketAddress sa, IOException ioe) {
        logger.warn("Proxy failed for {}: {}", uri, sa, ioe);
    }
};
