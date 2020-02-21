const { randomBytes } = require('crypto')
const bitcoints = require('bitcoin-ts')
const protobuf = require("protobufjs");
const $ = require("jquery");
const axios = require('axios');

$(document).ready(function () {

    bitcoints.instantiateSecp256k1().then(secp256k1 => {

        let privKey;
        do {
            privKey = randomBytes(32)
        } while (!secp256k1.validatePrivateKey(privKey));

        localStorage.setItem("privatekey", privKey);

        let publicKey = secp256k1.derivePublicKeyUncompressed(privKey);

        $('#register-account input[type=radio][name=actype]').change(function () {

            if (this.value == 'transporter') {

                $("#drivinglisence").show();

            } else {

                $("#drivinglisence").hide();

            }

        });
        let otpserver_transactionID;
        $("#sendotp").click(function () {
            $("#sendotp").hide();
            $("#otp").show();
            let mobile_number = $("#mobile_number").val();
            axios({
                method: 'get',
                url: 'http://127.0.0.1/otpapi/' + mobile_number
            }).then(function (response) {
                console.log(response.data)
                otpserver_transactionID = JSON.parse(response.data)['transid'];
            });

        })

        $("#register").click(function () {
            console.log(otpserver_transactionID)
            let actype = $("#register-account input[type='radio']:checked").val();
            let aadhar_card = $("#aadhar_card").val();
            let full_name = $("#full_name").val();
            let state = $("#state").val();
            let mobile_number = $("#mobile_number").val();
            let district = $("#district").val();
            let pincode = $("#pincode").val();
            let drivinglisence = $("#drivinglisence").val();
            let otp = $("#otp").val();

        });

    }).catch(err => {
        console.log("Secp256k1 can't initiate!")
    });


});
