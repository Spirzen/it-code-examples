package com.example.crm.config;

import com.example.crm.model.Customer;
import com.example.crm.repository.CustomerRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DataInitializer {

    @Bean
    CommandLineRunner seedCustomers(CustomerRepository customerRepository) {
        return args -> {
            if (customerRepository.count() > 0) {
                return;
            }

            Customer alice = new Customer();
            alice.setName("Алиса Иванова");
            alice.setEmail("alice@example.com");
            alice.setPhone("+7 900 111-22-33");
            alice.setCompany("ООО Альфа");
            alice.setNotes("Интересуется корпоративным тарифом");

            Customer bob = new Customer();
            bob.setName("Борис Петров");
            bob.setEmail("boris@example.com");
            bob.setPhone("+7 900 444-55-66");
            bob.setCompany("ИП Петров");
            bob.setNotes("Постоянный клиент");

            customerRepository.save(alice);
            customerRepository.save(bob);
        };
    }
}
