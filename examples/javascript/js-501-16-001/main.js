let x = 10;

function outer() {
    let y = 20;

    function inner() {
        let z = 30;
        console.log(x, y, z); // 10, 20, 30
    }

    inner();
}

outer();
