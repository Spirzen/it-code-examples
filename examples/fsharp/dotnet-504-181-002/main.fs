type OptionBuilder() =
    member _.Bind(x, f) = Option.bind f x
    member _.Return(x) = Some x
    member _.ReturnFrom(x) = x
    member _.Zero() = Some ()

let option = OptionBuilder()

let safeDivide a b =
    if b = 0 then None else Some (a / b)

let compute a b c =
    option {
        let! x = safeDivide a b
        let! y = safeDivide x c
        return y
    }
