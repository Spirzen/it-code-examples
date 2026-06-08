type Visibility = 'draft' | 'active' | 'archived' | 'out_of_stock';

interface Product {
  readonly id: string;
  price: number;
  stock: number;
  visibility: Visibility;
}

type Updatable<T> = Omit<T, 'id'>;

type SafeUpdate<T> = <K extends keyof Updatable<T>>(
  key: K,
  value: Updatable<T>[K]
) => T;

const createUpdater =
  <T,>(entity: T): SafeUpdate<T> =>
  (key, value) => ({ ...entity, [key]: value });

const product: Product = {
  id: 'prod_001',
  price: 100,
  stock: 10,
  visibility: 'draft'
};

const updateProduct = createUpdater(product);

updateProduct('price', 120);         // OK
updateProduct('visibility', 'active'); // OK

// updateProduct('id', 'prod_002');      // Ошибка: ключ исключён
// updateProduct('stock', '100');        // Ошибка: string не number
// updateProduct('visibility', 'deleted'); // Ошибка: нет в union
