Imports System.Collections.Generic

Public Class TagList
    Implements IEnumerable(Of String)

    Private ReadOnly _items As New List(Of String)

    Public Sub Add(tag As String)
        If Not String.IsNullOrWhiteSpace(tag) Then
            _items.Add(tag.Trim())
        End If
    End Sub

    Public ReadOnly Property Count As Integer
        Get
            Return _items.Count
        End Get
    End Property

    Public Iterator Function GetEnumerator() As IEnumerator(Of String) _
        Implements IEnumerable(Of String).GetEnumerator

        For Each tag In _items
            Yield tag
        Next
    End Function
End Class
