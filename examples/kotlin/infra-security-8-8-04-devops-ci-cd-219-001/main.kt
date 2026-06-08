version = "2024.01"

project {
    buildType {
        id("Build")
        vcs { root(AbsoluteId("MyGit")) }
        steps {
            script {
                name = "Compile"
                scriptContent = "./gradlew build"
            }
        }
        triggers { vcs { } }
    }
}
