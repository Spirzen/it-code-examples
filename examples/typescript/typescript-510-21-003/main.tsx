type TextFieldProps = {
  label: string;
  error?: string;
} & React.InputHTMLAttributes<HTMLInputElement>;

function TextField({ label, error, id, ...inputProps }: TextFieldProps) {
  const autoId = React.useId();
  const fieldId = id ?? autoId;
  return (
    <div className="form-group">
      <label htmlFor={fieldId}>{label}</label>
      <input
        id={fieldId}
        className={error ? 'input input--error' : 'input'}
        aria-invalid={error ? true : undefined}
        aria-describedby={error ? `${fieldId}-err` : undefined}
        {...inputProps}
      />
      {error ? (
        <span id={`${fieldId}-err`} className="input-hint error" role="alert">
          {error}
        </span>
      ) : null}
    </div>
  );
}
