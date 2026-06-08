// Интерфейс
export interface PaymentStrategy {
  pay(Данные: PaymentData): Promise<PaymentResult>;
}

// Реализации
@Injectable()
export class CardPaymentStrategy implements PaymentStrategy { ... }

@Injectable({ name: 'sbp' })
export class SBPPaymentStrategy implements PaymentStrategy { ... }

// Фабрика через DI
@Injectable()
export class PaymentStrategyFactory {
  constructor(
    @Inject('card') private card: PaymentStrategy,
    @Inject('sbp') private sbp: PaymentStrategy,
  ) {}

  create(type: 'card' | 'sbp'): PaymentStrategy {
    return type === 'card' ? this.card : this.sbp;
  }
}

// Сервис
@Injectable()
export class PaymentService {
  constructor(private factory: PaymentStrategyFactory) {}

  async process(type: 'card' | 'sbp', Данные: PaymentData) {
    const strategy = this.factory.create(type);
    return strategy.pay(Данные);
  }
}
