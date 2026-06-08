// src/com/example/ci/DeployHelper.groovy
package com.example.ci

class DeployHelper implements Serializable {
    def steps

    DeployHelper(steps) {
        this.steps = steps
    }

    void deploy(String env) {
        steps.sh "./deploy.sh ${env}"
    }
}
