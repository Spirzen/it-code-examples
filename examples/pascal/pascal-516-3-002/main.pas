unit MathUtils;

interface

function Factorial(n: Integer): Int64;

implementation

function Factorial(n: Integer): Int64;
begin
  if n <= 1 then
    Result := 1
  else
    Result := n * Factorial(n - 1);
end;

end.
