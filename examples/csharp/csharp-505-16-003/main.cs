using Xunit;
using HelloWorld;

namespace HelloWorld.Tests
{
    public class UnitTest1
    {
        [Fact]
        public void TestGetMessage_ReturnsHelloWorld()
        {
            // Arrange
            var service = new HelloService();

            // Act
            var result = service.GetMessage();

            // Assert
            Assert.Equal("Hello, World!", result);
        }
    }
}
