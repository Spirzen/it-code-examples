program ArrayExample;
var
  A: array[1..5] of Integer;
  i, Sum: Integer;
begin
  for i := 1 to 5 do
    A[i] := i * i;

  Sum := 0;
  for i := 1 to 5 do
    Sum := Sum + A[i];

  WriteLn('Сумма квадратов: ', Sum);
end.
