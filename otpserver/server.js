var express = require('express');
var app = express();
var otpapi = require("./router/otpapi.js");

app.use('/otpapi', otpapi);

app.get('/', function (req, res) {
    res.send("Welcome to sawtooth-agriculture otpserver.");
});

console.log("Otp server started at port 5050")
app.listen(5050)