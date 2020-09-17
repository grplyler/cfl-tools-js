var PMT = 120.0
var i = 0.10 / 12
var n = 30 * 12

// Formula for monthly retirement investment
var FVA = PMT * (((Math.pow(1 + i, n)) - 1) / i)
console.log(FVA)