
import csv
import json

def csv_to_json(csv_path, json_path):
    data = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Преобразование типов
            row['age'] = int(row['age'])
            row['active'] = row['active'].lower() == 'true'
            data.append(row)
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Вызов
csv_to_json('input.csv', 'output.json')
