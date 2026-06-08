package com.xmlvalidator.service;

import com.xmlvalidator.model.ValidationResult;
import org.xml.sax.ErrorHandler;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

import javax.xml.XMLConstants;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public final class XsdValidatorService {

    public ValidationResult validate(Path xmlPath, Path xsdPath) {
        if (xmlPath == null || !Files.isRegularFile(xmlPath)) {
            return ValidationResult.configurationError("Укажите существующий XML-файл.");
        }
        if (xsdPath == null || !Files.isRegularFile(xsdPath)) {
            return ValidationResult.configurationError("Укажите существующий XSD-файл.");
        }

        Source xmlSource = new StreamSource(xmlPath.toFile());
        xmlSource.setSystemId(xmlPath.toUri().toString());
        return validate(xmlSource, new StreamSource(xsdPath.toFile()));
    }

    public ValidationResult validate(String xmlContent, String xsdContent) {
        if (xmlContent == null || xmlContent.isBlank()) {
            return ValidationResult.configurationError("XML не может быть пустым.");
        }
        if (xsdContent == null || xsdContent.isBlank()) {
            return ValidationResult.configurationError("XSD не может быть пустым.");
        }

        Source xmlSource = streamSource(xmlContent, "inline.xml");
        Source xsdSource = streamSource(xsdContent, "inline.xsd");
        return validate(xmlSource, xsdSource);
    }

    private ValidationResult validate(Source xmlSource, Source xsdSource) {
        try {
            SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
            factory.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
            factory.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "file");

            Schema schema = factory.newSchema(xsdSource);
            Validator validator = schema.newValidator();
            validator.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
            validator.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "file");

            ValidationResult.Builder builder = new ValidationResult.Builder();
            validator.setErrorHandler(new CollectingErrorHandler(builder));
            validator.validate(xmlSource);
            return builder.build();
        } catch (SAXException ex) {
            if (ex instanceof SAXParseException parseEx) {
                return ValidationResult.failure(List.of(new ValidationResult.ValidationError(
                        parseEx.getMessage(),
                        parseEx.getLineNumber() > 0 ? parseEx.getLineNumber() : null,
                        parseEx.getColumnNumber() > 0 ? parseEx.getColumnNumber() : null,
                        "fatal"
                )));
            }
            return ValidationResult.configurationError("Ошибка схемы или XML: " + ex.getMessage());
        } catch (IOException ex) {
            return ValidationResult.configurationError("Ошибка чтения: " + ex.getMessage());
        }
    }

    private static Source streamSource(String content, String systemId) {
        InputStream input = new ByteArrayInputStream(content.getBytes(StandardCharsets.UTF_8));
        StreamSource source = new StreamSource(input, systemId);
        source.setSystemId(systemId);
        return source;
    }

    private static final class CollectingErrorHandler implements ErrorHandler {
        private final ValidationResult.Builder builder;

        private CollectingErrorHandler(ValidationResult.Builder builder) {
            this.builder = builder;
        }

        @Override
        public void warning(SAXParseException exception) {
            add(exception, "warning");
        }

        @Override
        public void error(SAXParseException exception) {
            add(exception, "error");
        }

        @Override
        public void fatalError(SAXParseException exception) throws SAXException {
            add(exception, "fatal");
            throw exception;
        }

        private void add(SAXParseException exception, String severity) {
            builder.addError(
                    exception.getMessage(),
                    exception.getLineNumber() > 0 ? exception.getLineNumber() : null,
                    exception.getColumnNumber() > 0 ? exception.getColumnNumber() : null,
                    severity
            );
        }
    }
}
