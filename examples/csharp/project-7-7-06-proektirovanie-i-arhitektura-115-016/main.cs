// Состояние саги
public class OrderProcessingState : SagaStateMachineInstance
{
    public Guid CorrelationId { get; set; }
    public string CurrentState { get; set; }
    public Guid OrderId { get; set; }
    public Guid PaymentId { get; set; }
}

// Машинное состояние
public class OrderProcessingSaga : MassTransitStateMachine<OrderProcessingState>
{
    public State PaymentCompleted { get; private set; }
    public State InventoryReserved { get; private set; }
    public State Completed { get; private set; }

    public Event<OrderSubmitted> OrderSubmitted { get; private set; }
    public Event<PaymentCompleted> PaymentCompleted { get; private set; }
    public Event<InventoryReserved> InventoryReserved { get; private set; }

    public OrderProcessingSaga()
    {
        InstanceState(x => x.CurrentState);

        Event(() => OrderSubmitted, x => x.CorrelateById(m => m.Message.OrderId));

        Initially(
            When(OrderSubmitted)
                .Then(context => context.Instance.OrderId = context.Data.OrderId)
                .Send(new ProcessPayment(context.Data.OrderId))
                .TransitionTo(PaymentCompleted)
        );

        During(PaymentCompleted,
            When(PaymentCompleted)
                .Then(context => context.Instance.PaymentId = context.Data.PaymentId)
                .Send(new ReserveInventory(context.Data.OrderId))
                .TransitionTo(InventoryReserved)
        );

        During(InventoryReserved,
            When(InventoryReserved)
                .Publish(new OrderProcessed(context.Instance.OrderId))
                .TransitionTo(Completed)
        );
    }
}
