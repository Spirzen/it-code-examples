Public Class Cache
    Private ReadOnly _data As New Dictionary(Of String, String)

    Default Public Property Item(key As String) As String
        Get
            Return _data(key)
        End Get
        Set(value As String)
            _data(key) = value
        End Set
    End Property
End Class

Dim c As New Cache()
c("user:1") = "Anna"
Console.WriteLine(c("user:1"))
