function LogCall(
  _target: object,
  propertyKey: string,
  descriptor: PropertyDescriptor,
): void {
  const original = descriptor.value as (...args: unknown[]) => unknown;

  descriptor.value = function (this: unknown, ...args: unknown[]) {
    console.log(`[${propertyKey}]`, args);
    return original.apply(this, args);
  };
}

class UserService {
  @LogCall
  findById(id: string): string {
    return `user:${id}`;
  }
}
