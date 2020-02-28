const { createContext, CryptoFactory } = require('sawtooth-sdk/signing')
const { Secp256k1PrivateKey } = require('sawtooth-sdk/signing/secp256k1')
const context = createContext('secp256k1')
const { createHash } = require('crypto')
const { protobuf } = require('sawtooth-sdk')
const request = require('request')

const FAMILY_NAME = 'agriculture_market'
const FAMILY_VERSION = '0.1'
const NAMESPACE = _hash(FAMILY_NAME).substring(0, 6)
const FARMER_PREFIX = '00'
const BUYER_PREFIX = '01'
const TRANSPORTER_PREFIX = '02'
const OTP_PREFIX = '03'
const ASSET_PREFIX = '04'

const Base64 = { _keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=", encode: function (e) { var t = ""; var n, r, i, s, o, u, a; var f = 0; e = Base64._utf8_encode(e); while (f < e.length) { n = e.charCodeAt(f++); r = e.charCodeAt(f++); i = e.charCodeAt(f++); s = n >> 2; o = (n & 3) << 4 | r >> 4; u = (r & 15) << 2 | i >> 6; a = i & 63; if (isNaN(r)) { u = a = 64 } else if (isNaN(i)) { a = 64 } t = t + this._keyStr.charAt(s) + this._keyStr.charAt(o) + this._keyStr.charAt(u) + this._keyStr.charAt(a) } return t }, decode: function (e) { var t = ""; var n, r, i; var s, o, u, a; var f = 0; e = e.replace(/[^A-Za-z0-9\+\/\=]/g, ""); while (f < e.length) { s = this._keyStr.indexOf(e.charAt(f++)); o = this._keyStr.indexOf(e.charAt(f++)); u = this._keyStr.indexOf(e.charAt(f++)); a = this._keyStr.indexOf(e.charAt(f++)); n = s << 2 | o >> 4; r = (o & 15) << 4 | u >> 2; i = (u & 3) << 6 | a; t = t + String.fromCharCode(n); if (u != 64) { t = t + String.fromCharCode(r) } if (a != 64) { t = t + String.fromCharCode(i) } } t = Base64._utf8_decode(t); return t }, _utf8_encode: function (e) { e = e.replace(/\r\n/g, "\n"); var t = ""; for (var n = 0; n < e.length; n++) { var r = e.charCodeAt(n); if (r < 128) { t += String.fromCharCode(r) } else if (r > 127 && r < 2048) { t += String.fromCharCode(r >> 6 | 192); t += String.fromCharCode(r & 63 | 128) } else { t += String.fromCharCode(r >> 12 | 224); t += String.fromCharCode(r >> 6 & 63 | 128); t += String.fromCharCode(r & 63 | 128) } } return t }, _utf8_decode: function (e) { var t = ""; var n = 0; var r = c1 = c2 = 0; while (n < e.length) { r = e.charCodeAt(n); if (r < 128) { t += String.fromCharCode(r); n++ } else if (r > 191 && r < 224) { c2 = e.charCodeAt(n + 1); t += String.fromCharCode((r & 31) << 6 | c2 & 63); n += 2 } else { c2 = e.charCodeAt(n + 1); c3 = e.charCodeAt(n + 2); t += String.fromCharCode((r & 15) << 12 | (c2 & 63) << 6 | c3 & 63); n += 3 } } return t } }

function makePrivetKey() {
    let privateKey = context.newRandomPrivateKey()
    let signer = new CryptoFactory(context).newSigner(privateKey)
    window.localStorage.setItem("privateKey", privateKey.asHex())
    return signer
}


function privateKeyFromHex(PrivateKeyInHex) {
    let privateKey = Secp256k1PrivateKey.fromHex(PrivateKeyInHex)
    let signer = new CryptoFactory(context).newSigner(privateKey)
    window.localStorage.setItem("privateKey", privateKey.asHex())
    return signer
}

function getPublicKeyHex(signer) {
    return signer.getPublicKey().asHex()
}


function getTransactionHeader(signer, tokey, payloadBytes, dependencies) {
    dependencies = typeof bar !== 'undefined' ? dependencies : [];
    let transactionHeaderBytes = protobuf.TransactionHeader.encode({
        familyName: 'agriculture_market',
        familyVersion: '0.1',
        inputs: tokey,
        outputs: tokey,
        signerPublicKey: signer.getPublicKey().asHex(),
        batcherPublicKey: signer.getPublicKey().asHex(),
        dependencies: dependencies,
        payloadSha512: createHash('sha512').update(payloadBytes).digest('hex')
    }).finish()
    return transactionHeaderBytes;
}

function getSignature(signer, payload) {
    return signer.sign(payload)
}

function getTransaction(signer, transactionHeaderBytes, payloadBytes) {
    let signature = getSignature(signer, transactionHeaderBytes)
    let transaction = protobuf.Transaction.create({
        header: transactionHeaderBytes,
        headerSignature: signature,
        payload: payloadBytes
    })
    return transaction;
}

function getBatchHeader(signer, transactions) {
    let batchHeaderBytes = protobuf.BatchHeader.encode({
        signerPublicKey: signer.getPublicKey().asHex(),
        transactionIds: transactions.map((txn) => txn.headerSignature),
    }).finish()
    return batchHeaderBytes;
}

function getBatch(signer, batchHeaderBytes, transactions) {
    let signature = getSignature(signer, batchHeaderBytes)
    let batch = protobuf.Batch.create({
        header: batchHeaderBytes,
        headerSignature: signature,
        transactions: transactions
    })
    let batchListBytes = protobuf.BatchList.encode({
        batches: [batch]
    }).finish()
    return batchListBytes;
}

function sendBatch(batchListBytes) {
    request.post({
        url: 'http://127.0.0.1:6060/batches',
        body: batchListBytes,
        headers: { 'Content-Type': 'application/octet-stream' }
    }, (err, response) => {
        if (err) return console.log(err)
        console.log(response.body)
    })
}

function _hash(x) {
    return createHash('sha512').update(x).digest('hex').toLowerCase()
}

function get_farmer_address(signer) {
    return NAMESPACE + FARMER_PREFIX + _hash(getPublicKeyHex(signer)).substring(0, 62)
}

function get_buyer_address(signer) {
    return NAMESPACE + BUYER_PREFIX + _hash(getPublicKeyHex(signer)).substring(0, 62)
}

function get_transporter_address(signer) {
    return NAMESPACE + TRANSPORTER_PREFIX + _hash(getPublicKeyHex(signer)).substring(0, 62)
}

function get_otp_address(mobilenumber, otp) {
    return NAMESPACE + OTP_PREFIX + (mobilenumber.toString()).substring(0, 10) + otp.toString()
}


module.exports = {
    makePrivetKey: makePrivetKey,
    privateKeyFromHex: privateKeyFromHex,
    getPublicKeyHex: getPublicKeyHex,
    getTransactionHeader: getTransactionHeader,
    getSignature: getSignature,
    getTransaction, getTransaction,
    getBatchHeader: getBatchHeader,
    getBatch: getBatch,
    sendBatch: sendBatch,
    get_buyer_address: get_buyer_address,
    get_farmer_address: get_farmer_address,
    get_transporter_address: get_transporter_address,
    get_otp_address: get_otp_address,
    Base64: Base64
}