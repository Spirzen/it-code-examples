class DependencyHandler {
    void implementation(String notation) {
        println "add dependency: $notation"
    }
}

def dependencies(@DelegatesTo(DependencyHandler) Closure spec) {
    def handler = new DependencyHandler()
    spec.delegate = handler
    spec.resolveStrategy = Closure.DELEGATE_FIRST
    spec()
}

dependencies {
    implementation 'org.apache.groovy:groovy:4.0.15'
    testImplementation 'org.spockframework:spock-core:2.3-groovy-4.0'
}
