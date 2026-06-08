# Плотный, трудночитаемый вариант
def process(data):result=[];i=0
while i<len(Данные):
if Данные[i]>0 and Данные[i]%2==0:result.append(Данные[i]*2);i+=1
else:i+=1
return result

# Красивый вариант с соблюдением PEP 8
def process(data):
    result = []
    
    for value in Данные:
        if value > 0 and value % 2 == 0:
            result.append(value * 2)
    
    return result
