/*const bitcoints = require('bitcoin-ts')
const { randomBytes } = require('crypto')
let publicKey;
let privKey;
let pubHex = "";

function bufferToHex(buffer) {
    return Array
        .from(new Uint8Array(buffer))
        .map(b => b.toString(16).padStart(2, "0"))
        .join("");
}
bitcoints.instantiateSecp256k1().then(secp256k1 => {

    do {
        privKey = randomBytes(32)
    } while (!secp256k1.validatePrivateKey(privKey));
    publicKey = secp256k1.derivePublicKeyUncompressed("939a998e61e5c84cd1f98c8701be0287af7f42a6ec0acd95be21a0fc56c02acc");
    pubHextemp = bufferToHex(publicKey);
    for (let i = 0; i < 66; i++) {
        pubHex = pubHex + pubHextemp[i];
    }

    //console.log(bufferToHex(privKey))
    //console.log("--")
    console.log(bufferToHex(secp256k1.signMessageHashRecoverableCompact(privKey, "hi")))
    console.log("--")
    //console.log(bufferToHex(secp256k1.signMessageHashSchnorr(privKey, "hi")))
    console.log(pubHex)
    //console.log(secp256k1.validatePrivateKey("939a998e61e5c84cd1f98c8701be0287af7f42a6ec0acd95be21a0fc56c02acc"))
    //console.log(secp256k1.verifySignatureCompact("ee0cef3124fb48cc7ae068f99b5430fc6fec02ecec9eadcb7ab5434155a4e88952c56f2f920ee1471e5ccb8687460af67b6cb5d3360c7fee927c8bc5d792863b", pubHex, "hi"))
    //console.log(pubHex)
}).catch(error => {
    console.log("error!")
})*/
function bufferToHex(buffer) {
    return Array
        .from(new Uint8Array(buffer))
        .map(b => b.toString(16).padStart(2, "0"))
        .join("");
}
const secp256k1 = require('secp256k1')
var s = "939a998e61e5c84cd1f98c8701be0287af7f42a6ec0acd95be21a0fc56c02acc";
var pk = [];

for (var i = 0; i < s.length; i += 2) {
    pk.push(parseInt(s.substring(i, i + 2), 16));
}
pk = Uint8Array.from(pk)


var sx = "150a14ed5bea6cc731cf86c41566ac427a8db48ef1b9fd626664b3bfbb99071fa4c922f33dde38719b8c8354e2b7ab9d77e0e67fc12843920a712e73d558e197"
var result = [];

for (var i = 0; i < sx.length; i += 2) {
    result.push(parseInt(sx.substring(i, i + 2), 16));
}
result = Uint8Array.from(result)
const pubKey = secp256k1.publicKeyCreate(pk)
const sigObj = secp256k1.ecdsaSign(result, pk)
console.log(bufferToHex(pubKey))
console.log("-----")
console.log(bufferToHex(sigObj['signature']))