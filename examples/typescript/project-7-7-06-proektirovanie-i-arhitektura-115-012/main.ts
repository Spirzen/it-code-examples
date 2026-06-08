// Команда
export class CreateOrderCommand {
  constructor(public readonly userId: string, public readonly items: Item[]) {}
}

// Обработчик команды
@CommandHandler(CreateOrderCommand)
export class CreateOrderHandler 
  implements ICommandHandler<CreateOrderCommand, OrderId> 
{
  constructor(private repo: OrderRepository) {}

  async execute(command: CreateOrderCommand): Promise<OrderId> {
    const order = Order.create(command.userId, command.items);
    await this.repo.save(order);
    return order.id;
  }
}

// Использование
const id = await this.commandBus.execute(
  new CreateOrderCommand(userId, items)
);
