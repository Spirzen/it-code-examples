package com.example.orderservice.service;

import com.example.orderservice.model.Order;
import com.example.orderservice.model.Order.OrderStatus;
import com.example.orderservice.repository.OrderRepository;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class OrderProcessingService {

    @Autowired
    private OrderRepository orderRepository;

    @Autowired
    private RabbitTemplate rabbitTemplate;

    private static final String QUEUE_NAME = "order_events";

    public void processPendingOrders() {
        List<Order> pendingOrders = orderRepository.findByStatusOrderByCreatedAtAsc(OrderStatus.PENDING);
        
        for (Order order : pendingOrders) {
            try {
                order.setStatus(OrderStatus.PROCESSING);
                orderRepository.save(order);
                
                // Имитация обработки
                Thread.sleep(1000);
                
                order.setStatus(OrderStatus.COMPLETED);
                orderRepository.save(order);
                
                // Отправка события
                rabbitTemplate.convertAndSend("", QUEUE_NAME, 
                    String.format("{\"orderId\": %d, \"status\": \"%s\"}", order.getId(), order.getStatus()));
                    
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                order.setStatus(OrderStatus.FAILED);
                orderRepository.save(order);
            }
        }
    }
}
