type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'danger';
type ControlSize = 'sm' | 'md' | 'lg';

type ButtonProps = {
  variant?: ButtonVariant;
  size?: ControlSize;
  loading?: boolean;
} & React.ButtonHTMLAttributes<HTMLButtonElement>;

function Button({
  variant = 'primary',
  size = 'md',
  loading = false,
  children,
  disabled,
  ...rest
}: ButtonProps) {
  return (
    <button
      type="button"
      className={`btn btn--${variant} btn--${size}`}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
      {...rest}
    >
      {loading ? 'Загрузка…' : children}
    </button>
  );
}
