const sawtooth = require('./sawtooth')

let signer = sawtooth.makePrivetKey()

let pvkey = signer._privateKey.asHex()
console.log(pvkey)

console.log(sawtooth.getPublicKeyHex(signer))
console.log(sawtooth.getSignature(signer, "helloWorld!"))