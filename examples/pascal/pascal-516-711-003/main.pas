unit ИмяМодуля;

interface

{ Объявления, доступные другим модулям }
uses
  ДругойМодуль1, ДругойМодуль2;

const
  PI = 3.14159;

type
  TPoint = record
    X, Y: Real;
  end;

procedure DrawLine(P1, P2: TPoint);
function Distance(P1, P2: TPoint): Real;

implementation

{ Реализация процедур и функций }
procedure DrawLine(P1, P2: TPoint);
begin
  { ... }
end;

function Distance(P1, P2: TPoint): Real;
begin
  Distance := Sqrt(Sqr(P2.X - P1.X) + Sqr(P2.Y - P1.Y));
end;

initialization
  { Код, выполняемый при загрузке модуля }

finalization
  { Код, выполняемый при выгрузке модуля }

end.
