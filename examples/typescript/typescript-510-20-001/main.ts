const input = document.querySelector("#email");
if (!(input instanceof HTMLInputElement)) throw new Error("no input");

input.addEventListener("input", () => {
  console.log(input.value);
});

const form = document.querySelector("form");
if (!(form instanceof HTMLFormElement)) throw new Error("no form");

form.addEventListener("submit", (e: SubmitEvent) => {
  e.preventDefault();
  const data = new FormData(form);
  console.log(data.get("email"));
});
