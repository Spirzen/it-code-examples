// appsettings.json
{
  "Memcached": {
    "Servers": [
      { "Address": "10.0.0.11", "Port": 11211 },
      { "Address": "10.0.0.12", "Port": 11211 }
    ],
    "ConnectTimeout": 500,
    "ReceiveTimeout": 1000,
    "SendTimeout": 1000,
    "UseBinaryProtocol": true,
    "KeyTransformer": "Enyim.Caching.Memcached.TigerHashKeyTransformer"
  }
}

// Startup.cs
services.AddEnyimMemcached(options =>
{
    Configuration.GetSection("Memcached").Bind(options);
});

services.AddStackExchangeRedisCache(...); // ← не путать с Redis!
