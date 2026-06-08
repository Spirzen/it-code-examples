# Плотный код без визуальных разделов
def calculate_report(Данные):
    total=sum(Данные);valid=[x for x in Данные if x>0];avg=total/len(valid)if valid else 0;return {"total":total,"valid_count":len(valid),"average":avg}

# Разреженная структура с группировкой операций
def calculate_report(Данные):
    total = sum(Данные)
    
    valid = [x for x in Данные if x > 0]
    valid_count = len(valid)
    
    average = total / valid_count if valid_count > 0 else 0
    
    return {
        "total": total,
        "valid_count": valid_count,
        "average": average
    }
