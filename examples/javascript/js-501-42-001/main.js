const input = document.getElementById('avatar');
const preview = document.getElementById('preview');

input.addEventListener('change', () => {
  const file = input.files[0];
  if (!file) return;

  if (file.size > 2 * 1024 * 1024) {
    alert('Файл больше 2 МБ');
    input.value = '';
    return;
  }

  showImagePreview(file, preview);
});
