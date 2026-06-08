
import groovy.json.JsonSlurper
import groovy.json.JsonOutput

def input = '''
[
  {"title":"Groovy in Action","author":"D. Konig","price":50,"active":true},
  {"title":"Legacy Java","author":"Team","price":35,"active":false}
]
'''

def books = new JsonSlurper().parseText(input)
def normalized = books.findAll { it.active }
                      .collect { b -> b + [price: (b.price as BigDecimal)] }
println JsonOutput.prettyPrint(JsonOutput.toJson(normalized))
