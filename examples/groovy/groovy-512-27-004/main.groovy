    HttpResponseResult execute(HttpRequestConfig config) {
        ensureInitialized()

        URI uri
        try {
            uri = URI.create(config.url.trim())
        } catch (Exception e) {
            return HttpResponseResult.error("Некорректный URL: ${e.message}")
        }

        if (!uri.scheme || !uri.host) {
            return HttpResponseResult.error('URL должен содержать схему и хост, например https://api.example.com/users')
        }

        def capture = new CaptureResultCollector()

        def loopController = new LoopController()
        loopController.loops = 1
        loopController.first = true
        loopController.initialize()

        def threadGroup = new ThreadGroup()
        threadGroup.name = 'API Tester Thread Group'
        threadGroup.numThreads = 1
        threadGroup.rampUp = 1
        threadGroup.samplerController = loopController

        def testPlan = new TestPlan('REST API Test')
        testPlan.userDefinedVariables = (Arguments) new Arguments().tap { addArgument('API_TEST', 'true') }

        def tree = new ListedHashTree()
        def testPlanTree = tree.add(testPlan)
        def threadGroupTree = testPlanTree.add(threadGroup)
        threadGroupTree.add(loopController)

        def sampler = buildSampler(uri, config)
        def samplerTree = threadGroupTree.add(sampler)

        def headerManager = buildHeaderManager(config.headers, config.body)
        if (headerManager) {
            samplerTree.add(headerManager)
        }

        samplerTree.add(capture)

        def engine = new StandardJMeterEngine()
        engine.configure(tree)

        try {
            engine.run()
            waitForEngine(engine)
        } catch (Exception e) {
            return HttpResponseResult.error("Ошибка JMeter: ${e.message}")
        } finally {
            engine.exit()
        }

        def sample = capture.capturedResult
        if (!sample) {
            return HttpResponseResult.error('JMeter не вернул результат запроса')
        }

        if (!sample.successful && sample.responseCode == null) {
            return HttpResponseResult.error(sample.responseMessage ?: 'Запрос завершился с ошибкой')
        }

        new HttpResponseResult(
            success: sample.successful,
            statusCode: parseStatusCode(sample.responseCode),
            responseTimeMs: sample.time,
            responseSizeBytes: sample.bytesAsLong,
            responseBody: sample.responseDataAsString ?: '',
            responseHeaders: sample.responseHeaders ?: '',
            requestHeaders: formatRequestHeaders(sample),
            contentType: sample.contentType ?: '',
            errorMessage: sample.successful ? null : (sample.responseMessage ?: 'HTTP ошибка')
        )
    }
