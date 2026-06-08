program Example;

uses
  Math, SysUtils;

var
  x, y: Integer;
  result: Real;

begin
  x := 5;
  y := 10;
  result := Sqrt(x * x + y * y);
  WriteLn('Гипотенуза: ', result:0:2);
end.
