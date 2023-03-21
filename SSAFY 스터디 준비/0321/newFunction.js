const add1 = (function () {
    const a = 10
    return function (x, y) {
        return x + y + a
    }
}())

console.log(add1(1, 2))




const add2 = (function () {
    const a = 10
    return new Function ('x', 'y', 'return x + y + a')
}())
const a = 20
console.log(add2)