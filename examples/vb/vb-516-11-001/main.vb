Public Structure Vector2D
    Public ReadOnly X As Double
    Public ReadOnly Y As Double

    Public Sub New(x As Double, y As Double)
        Me.X = x
        Me.Y = y
    End Sub

    Public Shared Operator +(a As Vector2D, b As Vector2D) As Vector2D
        Return New Vector2D(a.X + b.X, a.Y + b.Y)
    End Operator

    Public Shared Operator -(a As Vector2D, b As Vector2D) As Vector2D
        Return New Vector2D(a.X - b.X, a.Y - b.Y)
    End Operator
End Structure

Dim v = New Vector2D(1, 0) + New Vector2D(0, 1)
