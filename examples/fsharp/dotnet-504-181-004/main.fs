type Message = 
    | Add of int
    | Get of AsyncReplyChannel<int>

let counterAgent = MailboxProcessor.Start(fun inbox ->
    let rec loop total =
        async {
            let! msg = inbox.Receive()
            match msg with
            | Add n -> return! loop (total + n)
            | Get reply -> 
                reply.Reply(total)
                return! loop total
        }
    loop 0)

// Использование
counterAgent.Post(Add 5)
let current = counterAgent.PostAndReply(fun reply -> Get reply)
