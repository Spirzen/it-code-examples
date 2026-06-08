plugins {
    id 'groovy'
    id 'application'
}

group = 'apitester'
version = '1.0.0'

repositories {
    mavenCentral()
}

def groovyVersion = '3.0.20'
def jmeterVersion = '5.6.3'

dependencies {
    implementation "org.codehaus.groovy:groovy:${groovyVersion}"
    implementation "org.codehaus.groovy:groovy-swing:${groovyVersion}"
    implementation "org.codehaus.groovy:groovy-json:${groovyVersion}"

    implementation "org.apache.jmeter:ApacheJMeter_core:${jmeterVersion}"
    implementation "org.apache.jmeter:ApacheJMeter_http:${jmeterVersion}"
    implementation "org.apache.jmeter:ApacheJMeter_components:${jmeterVersion}"
    implementation "org.apache.jmeter:ApacheJMeter_java:${jmeterVersion}"

    implementation 'org.apache.logging.log4j:log4j-core:2.22.1'
    implementation 'org.apache.logging.log4j:log4j-api:2.22.1'
    implementation 'org.apache.logging.log4j:log4j-slf4j2-impl:2.22.1'
    implementation 'org.slf4j:slf4j-api:2.0.9'
}

application {
    mainClass = 'apitester.Main'
}

tasks.withType(JavaExec).configureEach {
    jvmArgs '-Dfile.encoding=UTF-8'
}

tasks.register('smokeTest', JavaExec) {
    group = 'verification'
    description = 'Smoke test HTTP request via JMeter'
    classpath = sourceSets.main.runtimeClasspath
    mainClass = 'apitester.SmokeTest'
}
