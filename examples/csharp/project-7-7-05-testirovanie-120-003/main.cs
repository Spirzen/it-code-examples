using Xunit;
using FluentAssertions; // рекомендуемая библиотека для выразительных утверждений

public class EmailValidatorTests
{
    [Theory]
    [InlineData("user@example.com")]
    [InlineData("test.email+tag@sub.domain.co.uk")]
    [InlineData("a@b.c")]
    public void Validate_ValidEmail_ReturnsSuccess(string email)
    {
        // Act
        var result = EmailValidator.Validate(email);

        // Assert
        result.IsValid.Should().BeTrue();
        result.ErrorMessage.Should().BeNull();
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public void Validate_NullOrWhitespace_ReturnsEmptyError(string email)
    {
        var result = EmailValidator.Validate(email);
        result.IsValid.Should().BeFalse();
        result.ErrorMessage.Should().Be("Email не может быть пустым");
    }

    [Theory]
    [InlineData("missing-at.com")]
    [InlineData("double@@example.com")]
    [InlineData("@domain.com")]
    public void Validate_InvalidAtCount_ReturnsAtError(string email)
    {
        var result = EmailValidator.Validate(email);
        result.IsValid.Should().BeFalse();
        result.ErrorMessage.Should().Be("Email должен содержать ровно один символ '@'");
    }

    [Theory]
    [InlineData("user@")]
    [InlineData("user@.com")]
    [InlineData("user@com.")]
    [InlineData("user@com")]
    public void Validate_InvalidDomain_ReturnsDomainError(string email)
    {
        var result = EmailValidator.Validate(email);
        result.IsValid.Should().BeFalse();
        result.ErrorMessage.Should().Be("Некорректный домен: должен содержать точку и не начинаться/заканчиваться ею");
    }

    [Fact]
    public void Validate_EmptyLocalPart_ReturnsLocalError()
    {
        var result = EmailValidator.Validate("@example.com");
        result.IsValid.Should().BeFalse();
        result.ErrorMessage.Should().Be("Локальная часть email не может быть пустой");
    }
}
