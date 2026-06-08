class User:
    def __init__(self, row):
        self.id = row['id']
        
        # Чтение с поддержкой обеих схем
        if row.get('first_name') and row.get('last_name'):
            self.first_name = row['first_name']
            self.last_name = row['last_name']
        else:
            parts = row['full_name'].split(' ', 1)
            self.first_name = parts[0]
            self.last_name = parts[1] if len(parts) > 1 else ''
    
    def save(self, cursor):
        # Запись в оба формата
        full_name = f"{self.first_name} {self.last_name}".strip()
        cursor.execute(
            """
            UPDATE users 
            SET full_name = %s, first_name = %s, last_name = %s 
            WHERE id = %s
            """,
            (full_name, self.first_name, self.last_name, self.id)
        )
