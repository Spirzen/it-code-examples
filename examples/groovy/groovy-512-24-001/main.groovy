plugins {
    id 'groovy'
    id 'application'
    id 'org.beryx.runtime' version '1.12.7'
}

group = 'io.github.yourgithubusername'
version = '0.0.1'

repositories {
    maven { url 'https://jitpack.io/' }
    mavenCentral()
}

dependencies {
    implementation 'io.github.lucasstarsz.fastj:fastj-library:1.7.0-SNAPSHOT-1'
    implementation 'org.slf4j:slf4j-simple:2.0.0-alpha7'
    implementation 'org.apache.groovy:groovy:4.0.4'
}
