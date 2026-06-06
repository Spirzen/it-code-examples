import groovy.json.JsonBuilder

def payload = new JsonBuilder([
    service: 'it-code-examples',
    version: 1,
    tags   : ['groovy', 'json']
])

println payload.toPrettyString()
