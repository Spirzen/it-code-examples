program DynamicArray;

var
  n, i: integer;
  a: array of integer;

begin
  ReadLn(n);
  SetLength(a, n);
  for i := 0 to n - 1 do
    Read(a[i]);
  ReadLn;
  { работа с a[0].a[n-1] }
end.
