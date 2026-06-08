program StudentRecord;

type
  TStudent = record
    name: string;
    age: integer;
    grade: real;
  end;

var
  st: TStudent;

begin
  ReadLn(st.name);
  ReadLn(st.age);
  ReadLn(st.grade);
  WriteLn(st.name, ', ', st.age, ' лет, средний балл ', st.grade:0:2);
end.
