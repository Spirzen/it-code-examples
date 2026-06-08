// app.js
const App = (function() {
    let privateVar = "приватная";
    
    return {
        publicVar: "публичная",
        getPrivate: function() {
            return privateVar;
        }
    };
})();

console.log(App.publicVar); // "публичная"
console.log(App.getPrivate()); // "приватная"
// console.log(App.privateVar); // undefined
