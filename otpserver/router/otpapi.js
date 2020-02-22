var express = require('express');
var router = express.Router();
var db = require("../dbhelper/dblogic.js")
const axios = require('axios');
const bitcoints = require('bitcoin-ts')
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
    publicKey = secp256k1.derivePublicKeyUncompressed(privKey);
    pubHextemp = bufferToHex(publicKey);
    for (let i = 2; i < 64; i++) {
        pubHex = pubHex + pubHextemp[i];
    }
    pubHex = "03" + pubHex;
}).catch(error => {
    console.log("error!")
})

router.get("/:number", function (req, res) {

    let number = req.params.number;
    if (number == "" || number == undefined || number.length != 10) {
        res.status(404).send({ sucess: false, message: "please input correct phone number!" });
    }
    let otp = Math.floor(Math.random() * 999999) + 111111;
    db.store(number, otp)
    axios.get('http://2factor.in/API/V1/ab7006ba-5252-11ea-9fa5-0200cd936042/SMS/' + number + '/' + otp)
        .then(response => {
            console.log(response.data)
            if (response.data.Status == "Sucess") {
                protobuf.load("./protofiles/payload.proto", function (err, root) {
                    if (err) {
                        res.status(404).send({ sucess: false, messsage: "Error!" });
                    }
                    var otp_transactionMessage = root.lookupType("Otp_transaction");
                    var otptrans_payload = { mobilenumber: number, otp: otp };
                    var otptrans_message = otp_transactionMessage.create(otptrans_payload);
                    var realPayloadMessage = root.lookupType("Realpayload");
                    var realPayload = { Action: 3, otp_tra: otptrans_message }
                    var realPayloadData = realPayloadMessage.create(realPayload);
                    var buffer = realPayloadMessage.encode(realPayloadData).finish();
                    let pubHex = bufferToHex(p)
                    protobuf.load("./protofiles/transaction.proto")
                        .then(root => {
                            var TransactionHeaderMessage = root.lookupType("TransactionHeader");
                            var TransactionHeaderpayload = {
                                familyName: 'agriculture_market',
                                familyVersion: '0.1',
                                inputs: ['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'],
                                outputs: ['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'],
                                signerPublicKey: signer.getPublicKey().asHex(),
                                // In this example, we're signing the batch with the same private key,
                                // but the batch can be signed by another party, in which case, the
                                // public key will need to be associated with that key.
                                batcherPublicKey: signer.getPublicKey().asHex(),
                                // In this example, there are no dependencies.  This list should include
                                // an previous transaction header signatures that must be applied for
                                // this transaction to successfully commit.
                                // For example,
                                // dependencies: ['540a6803971d1880ec73a96cb97815a95d374cbad5d865925e5aa0432fcf1931539afe10310c122c5eaae15df61236079abbf4f258889359c4d175516934484a'],
                                dependencies: [],
                                payloadSha512: createHash('sha512').update(payloadBytes).digest('hex')
                            };

                        })
                        .catch(err => {
                            // Deal with the fact the chain failed
                            res.status(404).send({ sucess: false, messsage: "Error!" });
                        });

                })
                res.send({ sucess: true, message: "Otp sentsucessfully!", transid: "" });
                //send data to block chain

            } else {
                res.status(404).send({ sucess: false, message: "Error from otp service provide!" });
            }
        })
        .catch(error => {
            res.status(404).send({ sucess: false, message: error });
        });
});



module.exports = router;
