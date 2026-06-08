type ListProps<T> = {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
  keyFn: (item: T) => string;
};

function List<T>({ items, renderItem, keyFn }: ListProps<T>) {
  return (
    <ul>
      {items.map((item) => (
        <li key={keyFn(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}
