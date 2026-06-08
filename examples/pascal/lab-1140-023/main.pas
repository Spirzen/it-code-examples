program WriteTable;

var
  f: text;
  i: integer;

begin
  Assign(f, 'output.txt');
  Rewrite(f);
  for i := 1 to 10 do
    Writeln(f, '2 x ', i, ' = ', 2 * i);
  Close(f);
  WriteLn('Готово: output.txt');
end.
