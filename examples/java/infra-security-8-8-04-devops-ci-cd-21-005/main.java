
import com.pulumi.Pulumi;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.aws.s3.inputs.BucketVersioningArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var bucket = new Bucket("my-bucket", BucketArgs.builder()
                .versioning(BucketVersioningArgs.builder()
                    .enabled(true)
                    .build())
                .build());
        });
    }
}
