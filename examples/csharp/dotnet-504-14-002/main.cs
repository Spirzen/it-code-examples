var typeBuilder = moduleBuilder.DefineType("Calculator", TypeAttributes.Public);
var methodBuilder = typeBuilder.DefineMethod(
    "Add", 
    MethodAttributes.Public | MethodAttributes.Static,
    typeof(int),
    new[] { typeof(int), typeof(int) }
);

var il = methodBuilder.GetILGenerator();
il.Emit(OpCodes.Ldarg_0);   // загрузить первый аргумент
il.Emit(OpCodes.Ldarg_1);   // загрузить второй аргумент
il.Emit(OpCodes.Add);       // сложить
il.Emit(OpCodes.Ret);       // вернуть результат

var calcType = typeBuilder.CreateType(); // → System.Type
var addMethod = calcType.GetMethod("Add");
int result = (int)addMethod.Invoke(null, new object[] { 2, 3 }); // → 5
