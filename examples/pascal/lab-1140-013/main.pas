program BubbleSort;

var
  n, i, j, tmp: integer;
  a: array[1.1000] of integer;

begin
  ReadLn(n);
  for i := 1 to n do
    Read(a[i]);
  ReadLn;
  for i := 1 to n - 1 do
    for j := 1 to n - i do
      if a[j] > a[j + 1] then
      begin
        tmp := a[j];
        a[j] := a[j + 1];
        a[j + 1] := tmp;
      end;
  for i := 1 to n do
    Write(a[i], ' ');
  WriteLn;
end.
