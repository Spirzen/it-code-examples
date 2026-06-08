# translators.py
class OrderCsvTranslator:
    LEGACY_COLUMNS = ['Номер', 'Дата', 'Сумма_без_НДС', 'Ставка_НДС']
    
    @classmethod
    def to_domain(cls, row: dict) -> OrderImportDto:
        try:
            # Валидация и преобразование
            amount = Decimal(row['Сумма_без_НДС'].replace(',', '.'))
            rate = Decimal(row['Ставка_НДС'].rstrip('%')) / 100
            
            return OrderImportDto(
                external_id=row['Номер'],
                date=datetime.strptime(row['Дата'], '%d.%m.%Y'),
                amount=amount,
                tax_rate=rate
            )
        except (KeyError, ValueError, InvalidOperation) as e:
            raise TranslationError(f"Invalid row {row}: {e}")

# adapters.py
class CsvOrderAdapter:
    def __init__(self, file_path: Path, translator: OrderCsvTranslator):
        self.file_path = file_path
        self.translator = translator

    def read_orders(self) -> Iterator[OrderImportDto]:
        try:
            with self.file_path.open('r', encoding='cp1251') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    try:
                        yield self.translator.to_domain(row)
                    except TranslationError as e:
                        logger.warning("Skipped invalid row: %s", e)
        except FileNotFoundError:
            logger.error("CSV file not found: %s", self.file_path)
            return

# services.py
class OrderImportService:
    def __init__(self, adapter: CsvOrderAdapter):
        self.adapter = adapter

    @transaction.atomic
    def import_orders(self):
        for dto in self.adapter.read_orders():
            Order.objects.update_or_create(
                external_id=dto.external_id,
                defaults={
                    'date': dto.date,
                    'amount': dto.amount,
                    'tax_rate': dto.tax_rate,
                    'total': dto.amount * (1 + dto.tax_rate)
                }
            )
        # После успешного импорта — архивация файла
        self._archive_file()
