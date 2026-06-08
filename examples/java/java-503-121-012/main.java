SSLParameters params = sslContext.getDefaultSSLParameters();

// Протоколы
params.setProtocols(new String[]{"TLSv1.2", "TLSv1.3"});

// Шифронаборы
params.setCipherSuites(new String[]{
    "TLS_AES_128_GCM_SHA256",
    "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
});

// ALPN (для HTTP/2)
params.setApplicationProtocols(new String[]{"h2", "http/1.1"});

// Hostname verification
params.setEndpointIdentificationAlgorithm("HTTPS"); // включает проверку CN/SAN
