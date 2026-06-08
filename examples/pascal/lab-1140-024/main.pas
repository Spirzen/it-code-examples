program MenuLoop;

var
  choice: integer;
  a, b: integer;

begin
  repeat
    WriteLn('1 — сложить два числа');
    WriteLn('2 — выход');
    Write('Выбор: ');
    ReadLn(choice);
    case choice of
      1:
        begin
          ReadLn(a, b);
          WriteLn('Сумма = ', a + b);
        end;
      2: WriteLn('Пока!');
      else
        WriteLn('Нет такого пункта');
    end;
  until choice = 2;
end.
