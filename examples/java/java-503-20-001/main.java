Properties props = new Properties();
props.put("mail.smtp.host", "smtp.example.com");
props.put("mail.smtp.auth", "true");

Session session = Session.getInstance(props, new Authenticator() {
    protected PasswordAuthentication getPasswordAuthentication() {
        return new PasswordAuthentication("user", "pass");
    }
});

MimeMessage message = new MimeMessage(session);
message.setFrom(new InternetAddress("noreply@example.com"));
message.addRecipient(Message.RecipientType.TO, new InternetAddress("user@domain.com"));
message.setSubject("Подтверждение");
message.setText("Ваш код: 123456");

Transport.send(message);
