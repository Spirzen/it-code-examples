package com.example.crm.controller;

import com.example.crm.model.Customer;
import com.example.crm.service.CustomerService;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
public class CustomerWebController {

    private final CustomerService customerService;

    public CustomerWebController(CustomerService customerService) {
        this.customerService = customerService;
    }

    @GetMapping("/")
    public String home() {
        return "redirect:/customers";
    }

    @GetMapping("/customers")
    public String list(Model model) {
        model.addAttribute("customers", customerService.findAll());
        return "customers/list";
    }

    @GetMapping("/customers/new")
    public String createForm(Model model) {
        model.addAttribute("customer", new Customer());
        model.addAttribute("formTitle", "Новый клиент");
        model.addAttribute("formAction", "/customers");
        return "customers/form";
    }

    @PostMapping("/customers")
    public String create(@Valid @ModelAttribute("customer") Customer customer,
                         BindingResult bindingResult,
                         Model model,
                         RedirectAttributes redirectAttributes) {
        if (bindingResult.hasErrors()) {
            model.addAttribute("formTitle", "Новый клиент");
            model.addAttribute("formAction", "/customers");
            return "customers/form";
        }
        customerService.create(customer);
        redirectAttributes.addFlashAttribute("message", "Клиент добавлен");
        return "redirect:/customers";
    }

    @GetMapping("/customers/{id}/edit")
    public String editForm(@PathVariable Long id, Model model) {
        model.addAttribute("customer", customerService.findById(id));
        model.addAttribute("formTitle", "Редактирование клиента");
        model.addAttribute("formAction", "/customers/" + id);
        return "customers/form";
    }

    @PostMapping("/customers/{id}")
    public String update(@PathVariable Long id,
                         @Valid @ModelAttribute("customer") Customer customer,
                         BindingResult bindingResult,
                         Model model,
                         RedirectAttributes redirectAttributes) {
        if (bindingResult.hasErrors()) {
            model.addAttribute("formTitle", "Редактирование клиента");
            model.addAttribute("formAction", "/customers/" + id);
            return "customers/form";
        }
        customerService.update(id, customer);
        redirectAttributes.addFlashAttribute("message", "Клиент обновлён");
        return "redirect:/customers";
    }

    @PostMapping("/customers/{id}/delete")
    public String delete(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        customerService.delete(id);
        redirectAttributes.addFlashAttribute("message", "Клиент удалён");
        return "redirect:/customers";
    }
}
