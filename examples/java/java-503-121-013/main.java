TrustManager[] trustAll = new TrustManager[]{
    new X509TrustManager() {
        public X509Certificate[] getAcceptedIssuers() { return new X509Certificate[0]; }
        public void checkClientTrusted(X509Certificate[] certs, String authType) {}
        public void checkServerTrusted(X509Certificate[] certs, String authType) {}
    }
};

SSLContext sslContext = SSLContext.getInstance("TLS");
sslContext.init(null, trustAll, new SecureRandom());

HttpClient client = HttpClient.newBuilder()
    .sslContext(sslContext)
    .sslParameters(new SSLParameters())
    .build();
