func (v *Verifier) Verify(email string) Result {
	email = strings.TrimSpace(strings.ToLower(email))
	result := Result{Email: email}

	if !emailRegex.MatchString(email) {
		result.Detail = "некорректный формат email"
		return result
	}
	result.Valid = true

	parts := strings.SplitN(email, "@", 2)
	result.Domain = parts[1]

	mxRecords, err := lookupMX(result.Domain)
	if err != nil {
		result.Error = err
		result.Detail = err.Error()
		return result
	}

	var lastErr error
	for _, mx := range mxRecords {
		host := strings.TrimSuffix(mx.Host, ".")
		exists, detail, err := verifySMTP(host, email, v.Timeout)
		if err != nil {
			lastErr = err
			continue
		}

		result.MXHost = host
		result.Exists = &exists
		result.Detail = detail
		return result
	}

	result.Error = lastErr
	if lastErr != nil {
		result.Detail = fmt.Sprintf("не удалось связаться ни с одним MX: %v", lastErr)
	} else {
		result.Detail = "нет доступных MX-серверов"
	}
	return result
}
