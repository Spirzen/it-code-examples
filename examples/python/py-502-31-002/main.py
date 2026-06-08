def create_project_structure(base_path):
    structure = [
        'src',
        'src/utils',
        'tests',
        'docs',
        'data/raw',
        'data/processed',
        'notebooks'
    ]
    
    base = Path(base_path)
    for folder in structure:
        (base / folder).mkdir(parents=True, exist_ok=True)
    
    # Создание файлов-заглушек
    (base / 'src' / '__init__.py').touch()
    (base / 'README.md').write_text('# Проект\nОписание\n')

create_project_structure('./my_project')
