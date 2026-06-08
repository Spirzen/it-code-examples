const list = document.getElementById("users");

function onListClick(event) {
  const actionNode = event.target.closest("[data-action]");
  if (!actionNode || !list.contains(actionNode)) {
    return;
  }

  if (actionNode.dataset.action === "remove") {
    actionNode.closest("li")?.remove();
  }
}

list.addEventListener("click", onListClick);
