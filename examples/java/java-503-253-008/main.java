package com.xmlvalidator.service;

import com.xmlvalidator.model.ValidationResult;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class XsdValidatorServiceTest {

    private XsdValidatorService service;
    private Path examplesDir;

    @BeforeEach
    void setUp() {
        service = new XsdValidatorService();
        examplesDir = Path.of("examples").toAbsolutePath();
    }

    @Test
    void validXmlPassesValidation() {
        ValidationResult result = service.validate(
                examplesDir.resolve("book-valid.xml"),
                examplesDir.resolve("book.xsd")
        );
        assertTrue(result.isValid(), result.getSummary());
    }

    @Test
    void invalidXmlFailsValidation() {
        ValidationResult result = service.validate(
                examplesDir.resolve("book-invalid.xml"),
                examplesDir.resolve("book.xsd")
        );
        assertFalse(result.isValid());
        assertFalse(result.getErrors().isEmpty());
    }

    @Test
    void inlineContentValidationWorks() {
        String xsd = """
                <?xml version="1.0" encoding="UTF-8"?>
                <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                  <xs:element name="note" type="xs:string"/>
                </xs:schema>
                """;
        String xml = """
                <?xml version="1.0" encoding="UTF-8"?>
                <note>Hello</note>
                """;

        ValidationResult result = service.validate(xml, xsd);
        assertTrue(result.isValid());
    }
}
