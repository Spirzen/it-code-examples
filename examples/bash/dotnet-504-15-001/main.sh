# Прямые зависимости
dotnet list package
# Project 'MyApp' has the following package references
#    [net8.0] —
#    Top-level Package      Requested   Resolved
#    > Newtonsoft.Json      13.0.1      13.0.1
#    > Serilog              3.1.1       3.1.1

# Полное дерево с транзитивными
dotnet list package --include-transitive
#    Top-level Package      Requested   Resolved
#    > Serilog              3.1.1       3.1.1
#      └── System.Text.Json 6.0.0       6.0.0   <-- транзитивная

# Пакеты, которые можно безопасно обновить (только патчи/миноры)
dotnet list package --outdated --vulnerable
