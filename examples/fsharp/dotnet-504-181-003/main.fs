open Suave
open Suave.Filters
open Suave.Operators

let app =
    choose [
        GET >=> path "/hello" >=> Successful.OK "Hello from F#!"
        POST >=> path "/echo" >=> Request.streamReader >>= fun body -> Successful.OK body
    ]

[<EntryPoint>]
let main _ =
    WebApp.startWebServer defaultConfig app
    0
