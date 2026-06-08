Imports System.Collections.Generic

Dim scores As New List(Of Integer) From {10, 20, 15}
scores.Sort()
Dim best = scores(scores.Count - 1)

Dim byId As New Dictionary(Of Integer, String)
byId(1) = "Anna"
Dim name As String = Nothing
If byId.TryGetValue(2, name) Then
    Console.WriteLine(name)
Else
    byId(2) = "Boris"
End If
