program FizzBuzz;

var
  n, i: integer;

begin
  ReadLn(n);
  for i := 1 to n do
  begin
    if (i mod 15 = 0) then
      WriteLn('FizzBuzz')
    else if (i mod 3 = 0) then
      WriteLn('Fizz')
    else if (i mod 5 = 0) then
      WriteLn('Buzz')
    else
      WriteLn(i);
  end;
end.
