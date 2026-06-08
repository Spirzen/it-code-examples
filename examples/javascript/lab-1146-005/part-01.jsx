const VARIANT_CLASS = {
  primary: 'button button--primary',
  outline: 'button button--outline',
  danger: 'button button--danger',
};

export function Button({
  variant = 'primary',
  loading = false,
  disabled = false,
  children,
  ...rest
}) {
  const isDisabled = disabled || loading;
  return (
    <button
      type="button"
      className={VARIANT_CLASS[variant] ?? VARIANT_CLASS.primary}
      disabled={isDisabled}
      aria-busy={loading || undefined}
      {...rest}
    >
      {loading ? 'Загрузка…' : children}
    </button>
  );
}
