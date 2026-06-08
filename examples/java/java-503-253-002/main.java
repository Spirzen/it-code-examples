package com.xmlvalidator.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public final class ValidationResult {

    private final boolean valid;
    private final List<ValidationError> errors;
    private final String summary;

    private ValidationResult(boolean valid, List<ValidationError> errors, String summary) {
        this.valid = valid;
        this.errors = List.copyOf(errors);
        this.summary = summary;
    }

    public static ValidationResult success() {
        return new ValidationResult(true, List.of(), "Документ соответствует XSD-схеме.");
    }

    public static ValidationResult failure(List<ValidationError> errors) {
        String summary = errors.isEmpty()
                ? "Документ не прошёл валидацию."
                : "Найдено ошибок: " + errors.size();
        return new ValidationResult(false, errors, summary);
    }

    public static ValidationResult configurationError(String message) {
        ValidationError error = new ValidationError(message, null, null, null);
        return new ValidationResult(false, List.of(error), message);
    }

    public boolean isValid() {
        return valid;
    }

    public List<ValidationError> getErrors() {
        return errors;
    }

    public String getSummary() {
        return summary;
    }

    public record ValidationError(
            String message,
            Integer lineNumber,
            Integer columnNumber,
            String severity
    ) {
        public String formatted() {
            StringBuilder sb = new StringBuilder();
            if (severity != null && !severity.isBlank()) {
                sb.append('[').append(severity).append("] ");
            }
            if (lineNumber != null && columnNumber != null) {
                sb.append("Строка ").append(lineNumber)
                        .append(", столбец ").append(columnNumber).append(": ");
            }
            sb.append(message);
            return sb.toString();
        }
    }

    public static final class Builder {
        private final List<ValidationError> errors = new ArrayList<>();

        public void addError(String message, Integer line, Integer column, String severity) {
            errors.add(new ValidationError(message, line, column, severity));
        }

        public ValidationResult build() {
            if (errors.isEmpty()) {
                return success();
            }
            return failure(Collections.unmodifiableList(new ArrayList<>(errors)));
        }
    }
}
