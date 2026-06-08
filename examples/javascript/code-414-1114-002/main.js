// Ошибочный подход
var data = fetchData();
if (data == "") {
  document.body.innerHTML += "<div>Пусто</div>";
}

// Корректный подход
const data = await fetchData();
if (data === "") {
  const fragment = document.createDocumentFragment();
  const div = document.createElement("div");
  div.textContent = "Пусто";
  fragment.appendChild(div);
  document.body.appendChild(fragment);
}
