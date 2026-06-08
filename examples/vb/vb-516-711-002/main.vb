Public Class Car
    Private _brand As String

    Public Property Brand As String
        Get
            Return _brand
        End Get
        Set(value As String)
            _brand = value
        End Set
    End Property

    Public Sub StartEngine()
        Console.WriteLine("Двигатель запущен")
    End Sub
End Class
