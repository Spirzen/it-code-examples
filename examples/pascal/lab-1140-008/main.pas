program ReverseArray;

var
  n, i, tmp: integer;
  a: array[1.1000] of integer;

begin
  ReadLn(n);
  for i := 1 to n do
    Read(a[i]);
  ReadLn;
  for i := 1 to n div 2 do
  begin
    tmp := a[i];
    a[i] := a[n - i + 1];
    a[n - i + 1] := tmp;
  end;
  for i := 1 to n do
    Write(a[i], ' ');
  WriteLn;
end.
