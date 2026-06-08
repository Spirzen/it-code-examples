// auth/TokenManager.java
public class TokenManager {
    private final JwtSigner jwtSigner;
    private final Clock clock;
    
    public TokenManager(JwtSigner jwtSigner, Clock clock) {
        this.jwtSigner = jwtSigner;
        this.clock = clock;
    }
    
    public String generateDerivedToken(String masterToken, String moduleId, Set<String> scopes) {
        // Валидация мастер-токена
        JwtClaims masterClaims = jwtSigner.validate(masterToken);
        if (!masterClaims.isActive(clock.instant())) {
            throw new InvalidTokenException("Мастер-токен недействителен");
        }
        
        // Формирование производного токена с ограниченными правами
        Instant now = clock.instant();
        JwtClaims derivedClaims = new JwtClaims()
            .setSubject(masterClaims.getSubject())
            .setIssuer("superapp-core")
            .setIssuedAt(now)
            .setExpiration(now.plus(Duration.ofHours(2)))
            .setAudience(moduleId)
            .setClaim("scopes", scopes)
            .setClaim("derived_from", masterClaims.getJwtId());
        
        return jwtSigner.sign(derivedClaims);
    }
    
    public boolean hasScope(String token, String requiredScope) {
        JwtClaims claims = jwtSigner.validate(token);
        @SuppressWarnings("unchecked")
        Set<String> scopes = (Set<String>) claims.getClaim("scopes");
        return scopes != null && scopes.contains(requiredScope);
    }
}
