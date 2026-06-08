type RegistrationForm = {
  email: string;
  password: string;
};

type FieldErrors = Partial<Record<keyof RegistrationForm, string>>;

function validate(form: RegistrationForm): FieldErrors {
  const errors: FieldErrors = {};
  if (!form.email.includes("@")) errors.email = "Некорректный email";
  if (form.password.length < 8) errors.password = "Минимум 8 символов";
  return errors;
}

function readForm(formEl: HTMLFormElement): RegistrationForm {
  const data = new FormData(formEl);
  return {
    email: String(data.get("email") ?? ""),
    password: String(data.get("password") ?? ""),
  };
}
