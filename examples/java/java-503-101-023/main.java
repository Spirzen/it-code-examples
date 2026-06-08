public class ExchangeRateService {
    private final Cache<String, BigDecimal> rateCache = 
        CacheBuilder.newBuilder()
            .maximumSize(1000)
            .expireAfterWrite(1, TimeUnit.HOURS)
            .build();
    
    public BigDecimal getRate(String fromCurrency, String toCurrency) {
        String key = fromCurrency + "_" + toCurrency;
        return rateCache.get(key, () -> fetchRateFromExternalApi(fromCurrency, toCurrency));
    }
    
    private BigDecimal fetchRateFromExternalApi(String from, String to) {
        // Вызов внешнего API
        return externalApi.getExchangeRate(from, to);
    }
}
