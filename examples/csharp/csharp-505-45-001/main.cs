switch (response.StatusCode)
{
    case HttpStatusCode.OK:
        var result = await response.Content.ReadFromJsonAsync<SuccessDto>();
        return result;

    case HttpStatusCode.BadRequest:
        var error = await response.Content.ReadFromJsonAsync<ValidationErrorDto>();
        throw new IntegrationValidationException(error.Messages);

    case HttpStatusCode.Unauthorized:
        // возможно, сессия протухла — попытка refresh + повтор
        await _authService.RefreshTokenAsync();
        return await SendAsync(request, cancellationToken); // повтор

    case HttpStatusCode.Conflict:
        throw new IntegrationConflictException("Запись уже существует во внешней системе.");

    default:
        _logger.LogWarning("Необработанный статус {StatusCode} при вызове {Endpoint}",
            response.StatusCode, request.Endpoint);
        throw new IntegrationUnexpectedResponseException(response.StatusCode);
}
