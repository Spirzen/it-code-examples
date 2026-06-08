    private static HTTPSamplerProxy buildSampler(URI uri, HttpRequestConfig config) {
        def sampler = new HTTPSamplerProxy()
        sampler.name = 'REST Request'
        sampler.protocol = uri.scheme
        sampler.domain = uri.host
        sampler.port = uri.port > 0 ? uri.port : (uri.scheme == 'https' ? 443 : 80)

        def path = uri.rawPath ?: '/'
        if (uri.rawQuery) {
            path += "?${uri.rawQuery}"
        }
        sampler.path = path
        sampler.method = config.method.toUpperCase()
        sampler.connectTimeout = config.connectTimeoutMs
        sampler.responseTimeout = config.responseTimeoutMs
        sampler.followRedirects = true
        sampler.useKeepAlive = true

        if (config.body && config.method.toUpperCase() in ['POST', 'PUT', 'PATCH']) {
            sampler.postBodyRaw = true
            def args = new Arguments()
            args.addArgument('', config.body)
            sampler.arguments = args
        }

        sampler
    }

    private static HeaderManager buildHeaderManager(Map<String, String> headers, String body) {
        def manager = new HeaderManager()
        manager.name = 'HTTP Header Manager'

        headers.each { name, value ->
            if (name?.trim()) {
                manager.add(new Header(name.trim(), value ?: ''))
            }
        }

        if (body && !headers.keySet().any { it.equalsIgnoreCase('Content-Type') }) {
            manager.add(new Header('Content-Type', 'application/json; charset=UTF-8'))
        }

        manager.headers.size() > 0 ? manager : null
    }
