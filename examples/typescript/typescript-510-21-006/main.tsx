type IconButtonProps = {
  label: string;
} & React.ComponentProps<"button">;

function IconButton({ label, ...rest }: IconButtonProps) {
  return (
    <button type="button" aria-label={label} {...rest}>
      ★
    </button>
  );
}

type NativeInputProps = React.ComponentProps<"input">;
type SearchInputProps = Pick<NativeInputProps, "placeholder" | "disabled">;
