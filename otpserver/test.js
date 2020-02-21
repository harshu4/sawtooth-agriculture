var protobuf = require("protobufjs");
const axios = require('axios');
(async () => {
    try {
        var root = await protobuf.load("./protofiles/otptransaction.proto")
        var otptransactionMessage = root.lookupType("otptransaction")
        var payload = { number: 99, reqid: "AwesomeString", transaction: new Uint8Array(100) };
        var message = otptransactionMessage.create(payload);
        var buffer = otptransactionMessage.encode(message).finish();
        let config = {
            headers: {
                'Content-Type': 'application/octet-stream'
            }
        }
        await axios.post('http://127.0.0.1:5050/transactionapi/post', buffer, config)
            .then(response => {

                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
            });
    } catch (e) {
        console.log(e)
    }
})();