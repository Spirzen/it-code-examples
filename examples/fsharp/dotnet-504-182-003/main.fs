module CounterModule =
    let mutable currentCount = 0
    
    let increment () =
        currentCount <- currentCount + 1
        currentCount
        
    let decrement () =
        if currentCount > 0 then
            currentCount <- currentCount - 1
        currentCount
        
    let reset () =
        currentCount <- 0
        0
