type CounterMsg =
    | Add of int
    | Get of AsyncReplyChannel<int>

let createCounter () =
    MailboxProcessor.Start(fun inbox ->
        let rec loop total =
            async {
                let! msg = inbox.Receive()
                match msg with
                | Add n -> return! loop (total + n)
                | Get reply ->
                    reply.Reply total
                    return! loop total
            }
        loop 0)

let agent = createCounter ()
agent.Post (Add 10)
let current = agent.PostAndReply (fun reply -> Get reply)
