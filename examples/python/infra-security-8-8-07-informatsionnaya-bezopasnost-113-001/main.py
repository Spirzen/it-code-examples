
import os
import magic

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
UPLOAD_FOLDER = '/var/app/uploads'  # Вне webroot

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Проверка размера
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    if size > MAX_FILE_SIZE:
        return jsonify({'error': 'File too large'}), 400

    # Проверка расширения
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    # Проверка MIME-типа
    mime = magic.from_buffer(file.read(2048), mime=True)
    file.seek(0)
    if mime not in ['image/png', 'image/jpeg', 'image/gif']:
        return jsonify({'error': 'Invalid MIME type'}), 400

    # Безопасное имя файла
    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4().hex}_{filename}"
    file.save(os.path.join(UPLOAD_FOLDER, unique_filename))
    return jsonify({'success': True, 'filename': unique_filename}), 200
