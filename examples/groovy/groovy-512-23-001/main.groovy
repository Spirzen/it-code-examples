plugins {
    id 'java'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.apache.groovy:groovy:4.0.21'
}

tasks.named('test') {
    useJUnitPlatform()
}
