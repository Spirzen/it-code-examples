    private static Map<String, String> parseHeaders(String text) {
        if (!text?.trim()) {
            return [:]
        }

        def headers = [:]
        text.readLines().each { line ->
            def trimmed = line.trim()
            if (!trimmed || trimmed.startsWith('#')) {
                return
            }
            def separatorIndex = trimmed.indexOf(':')
            if (separatorIndex > 0) {
                def name = trimmed.substring(0, separatorIndex).trim()
                def value = trimmed.substring(separatorIndex + 1).trim()
                headers[name] = value
            }
        }
        headers
    }

    private static String formatBody(String body) {
        if (!body) {
            return ''
        }
        def trimmed = body.trim()
        if ((trimmed.startsWith('{') && trimmed.endsWith('}')) || (trimmed.startsWith('[') && trimmed.endsWith(']'))) {
            try {
                def json = new groovy.json.JsonSlurper().parseText(trimmed)
                return groovy.json.JsonOutput.prettyPrint(groovy.json.JsonOutput.toJson(json))
            } catch (Exception ignored) {
            }
        }
        body
    }
