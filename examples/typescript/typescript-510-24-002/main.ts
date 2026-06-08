type Visibility = "draft" | "active" | "archived";

interface Product {
  readonly id: string;
  name: string;
  price: number;
  visibility: Visibility;
}

type Updatable<T> = Omit<T, "id">;

type SafeUpdate<T> = <K extends keyof Updatable<T>>(
  key: K,
  value: Updatable<T>[K],
) => T;

const createUpdater =
  <T,>(entity: T): SafeUpdate<T> =>
  (key, value) => ({ ...entity, [key]: value });

const product: Product = {
  id: "p1",
  name: "Стол",
  price: 899,
  visibility: "draft",
};

const update = createUpdater(product);
update("price", 699);           // OK
update("visibility", "active"); // OK
// update("id", "x");          // ошибка: id исключён
// update("price", "free");     // ошибка: нужен number
