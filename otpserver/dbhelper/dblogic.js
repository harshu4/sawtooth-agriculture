const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')

const adapter = new FileSync('./dbhelper/db.json')
const db = low(adapter)


function store(reqid, otp, number) {
    db.set(reqid, { number: number, otp: otp }).write()
}

function get(reqid) {
    return db.get(reqid).value();
}

module.exports = { store: store, get: get }

