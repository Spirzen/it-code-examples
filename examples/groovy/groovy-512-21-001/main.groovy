plugins {
    id 'java'
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation 'org.spockframework:spock-core:2.3-groovy-4.0'
    testImplementation 'org.apache.groovy:groovy:4.0.21'
}

test {
    useJUnitPlatform()
}
