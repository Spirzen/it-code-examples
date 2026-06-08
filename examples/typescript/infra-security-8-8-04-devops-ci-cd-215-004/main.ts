
import * as gcp from "@pulumi/gcp";
import * as k8s from "@pulumi/kubernetes";

const cluster = new gcp.container.Cluster("app-cluster", {
    initialNodeCount: 2,
    nodeVersion: "1.28",
    minMasterVersion: "1.28",
    nodeConfig: {
        machineType: "e2-medium",
        oauthScopes: [
            "https://www.googleapis.com/auth/cloud-platform"
        ],
    },
});

const kubeconfig = gcp.container.getClusterKubeconfig({
    name: cluster.name,
    location: cluster.location,
});

const provider = new k8s.Provider("k8s-provider", {
    kubeconfig: kubeconfig.kubeconfig,
});

const appLabels = { app: "nginx" };
const deployment = new k8s.apps.v1.Deployment("nginx-deployment", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 3,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: "nginx",
                    image: "nginx:1.25",
                    ports: [{ containerPort: 80 }],
                }],
            },
        },
    },
}, { provider: provider });

export const clusterName = cluster.name;
