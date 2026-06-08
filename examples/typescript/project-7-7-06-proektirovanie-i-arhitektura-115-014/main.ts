// 1. Транслятор
@Injectable()
export class InnValidatorTranslator {
  toExternalRequest(inn: string): ExternalInnRequest {
    return { taxpayerId: inn.replace(/\s/g, '') };
  }

  fromExternalResponse(res: ExternalResponse): InnValidationResult {
    if (res.status === 'VALID') return { isValid: true };
    if (res.status === 'INVALID') return { isValid: false };
    throw new ExternalSystemException('Unexpected status: ' + res.status);
  }
}

// 2. Защищённый адаптер
@Injectable()
export class ResilientInnValidator implements IInnValidator {
  constructor(
    private readonly http: HttpService,
    private readonly translator: InnValidatorTranslator,
    @Inject('CONFIG') private config: ConfigService,
  ) {}

  async validate(inn: string): Promise<InnValidationResult> {
    const request = this.translator.toExternalRequest(inn);
    
    // Circuit Breaker + Retry через @nestjs/terminus и rxjs
    return firstValueFrom(
      this.http.post<ExternalResponse>(this.config.get('INN_API_URL'), request)
        .pipe(
          retry({ count: 3, delay: (error, count) => 
            timer(Math.pow(2, count) * 1000) 
          }),
          timeout(5000),
          catchError(err => {
            if (err instanceof TimeoutError) {
              throw new ServiceUnavailableException('INN API timeout');
            }
            throw new ExternalSystemException('INN API failed', { cause: err });
          }),
          map(res => this.translator.fromExternalResponse(res.Данные))
        )
    );
  }
}

// 3. Регистрация с политиками
@Module({
  providers: [
    {
      provide: IInnValidator,
      useClass: ResilientInnValidator,
    },
    InnValidatorTranslator,
  ],
  exports: [IInnValidator],
})
export class InnValidationModule {}
