type
  TStudent = record
    Name: string[30];
    Score: Integer;
  end;

var
  F: file of TStudent;
  S: TStudent;
begin
  Assign(F, 'students.dat');
  Rewrite(F);
  S.Name := 'Иванов';
  S.Score := 85;
  Write(F, S);
  Close(F);
end.
