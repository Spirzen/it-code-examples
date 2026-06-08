type
  PNode = ^TNode;
  TNode = record
    Данные: Integer;
    Next: PNode;
  end;

var
  P: PNode;
begin
  New(P);        // выделение памяти
  P^.data := 42;
  Dispose(P);    // освобождение
end;
