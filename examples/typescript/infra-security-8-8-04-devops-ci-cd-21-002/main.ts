
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

class WebApp extends pulumi.ComponentResource {
    public readonly bucket: aws.s3.Bucket;
    public readonly cdn: aws.cloudfront.Distribution;

    constructor(name: string, opts?: pulumi.ResourceOptions) {
        super("custom:WebApp", name, {}, opts);

        this.bucket = new aws.s3.Bucket(`${name}-bucket`, {
            website: {
                indexDocument: "index.html",
            },
        }, { parent: this });

        this.cdn = new aws.cloudfront.Distribution(`${name}-cdn`, {
            origins: [{
                domainName: this.bucket.websiteEndpoint,
                originId: this.bucket.id,
            }],
            defaultCacheBehavior: {
                targetOriginId: this.bucket.id,
                viewerProtocolPolicy: "redirect-to-https",
                allowedMethods: ["GET", "HEAD"],
                cachedMethods: ["GET", "HEAD"],
                forwardedValues: {
                    cookies: { forward: "none" },
                    queryString: false,
                },
            },
            enabled: true,
            isIpv6Enabled: true,
            comment: "CDN for static website",
        }, { parent: this });
    }
}

const app = new WebApp("my-app");
