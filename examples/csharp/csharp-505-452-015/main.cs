public class GreeterService : Greeter.GreeterBase
{
    public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
    {
        return Task.FromResult(new HelloReply { Message = $"Hello {request.Name}" });
    }

    public override async Task SayHellos(HelloRequest request, IServerStreamWriter<HelloReply> responseStream, ServerCallContext context)
    {
        for (int i = 1; i <= 5; i++)
        {
            await responseStream.WriteAsync(new HelloReply { Message = $"Hello {request.Name} #{i}" });
            await Task.Delay(500);
        }
    }
}
