plugins {
    id "java"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation "org.apache.groovy:groovy:4.0.21"
    testImplementation "org.spockframework:spock-core:2.3-groovy-4.0"
}

test {
    useJUnitPlatform()
}
