class JMeterHttpExecutor {

    private static volatile boolean initialized = false

    static synchronized void ensureInitialized() {
        if (initialized) {
            return
        }

        def jmeterHomeUrl = JMeterHttpExecutor.classLoader.getResource('jmeter/bin/jmeter.properties')
        if (!jmeterHomeUrl) {
            throw new IllegalStateException('Не найден jmeter.properties в classpath')
        }

        def propsFile = new File(jmeterHomeUrl.toURI())
        def jmeterHome = propsFile.parentFile.parentFile.absolutePath

        JMeterUtils.setJMeterHome(jmeterHome)
        JMeterUtils.loadJMeterProperties(propsFile.absolutePath)
        JMeterUtils.setProperty('language', 'en')
        JMeterUtils.setProperty('country', 'US')
        JMeterUtils.initLocale()
        initialized = true
    }
