program LinearSearch;

var
  n, i, key, index: integer;
  a: array[1.100000] of integer;

begin
  ReadLn(n);
  for i := 1 to n do
    Read(a[i]);
  ReadLn;
  ReadLn(key);
  index := -1;
  for i := 1 to n do
    if (index = -1) and (a[i] = key) then
      index := i;
  WriteLn(index);
end.
