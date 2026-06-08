func apiKeyGuard(expected string) gin.HandlerFunc {
    return func(c *gin.Context) {
        key := c.GetHeader("X-API-Key")
        if key == "" {
            c.JSON(http.StatusUnauthorized, gin.H{"error": "missing api key"})
            c.Abort()
            return
        }
        if key != expected {
            c.JSON(http.StatusForbidden, gin.H{"error": "invalid api key"})
            c.Abort()
            return
        }
        c.Next()
    }
}

// api := r.Group("/api")
// api.Use(apiKeyGuard("dev-secret"))
