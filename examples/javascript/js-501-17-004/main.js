function nestedScopes() {
    let level1 = "уровень 1";
    
    {
        let level2 = "уровень 2";
        console.log(level1); // "уровень 1"
        console.log(level2); // "уровень 2"
        
        {
            let level3 = "уровень 3";
            console.log(level1); // "уровень 1"
            console.log(level2); // "уровень 2"
            console.log(level3); // "уровень 3"
        }
        
        // console.log(level3); // ReferenceError
    }
    
    // console.log(level2); // ReferenceError
}

nestedScopes();
