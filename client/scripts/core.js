
const $ = require("jquery");
const request = require('request');
const sawtooth = require('./sawtooth');
const protobuf = require('./proto/agpayload')
const Pbf = require('pbf');


$(document).ready(function () {
    let txn_id;
    let signer;

    if (!window.localStorage.privateKey) {
        signer = sawtooth.makePrivetKey();
    } else {
        signer = sawtooth.privateKeyFromHex(window.localStorage.privateKey);
    }
    $("#sendotp").click(function () {
        $("#sendotp").hide();
        $("#otp").show();
        let mobile_number = $("#mobile_number").val();
        request('http://127.0.0.1:6060/otp/' + mobile_number, function (error, response, body) {
            if (error) {
                console.error("Error: while requesting otp!")
                $("#sendotp").show();
                $("#otp").hide();
                return;
            }
            let res = JSON.parse(body)
            //console.log(res)

            if (res.status) {
                console.log(res.message)
                txn_id = res.txnid;
            } else {
                console.error("Error!, " + res.message)
                $("#sendotp").show();
                $("#otp").hide();
            }

        });
    })

    $("#register").click(function () {

        let actype = $("#register-account input[type='radio']:checked").val();
        let aadhar_card = $("#aadhar_card").val();
        let full_name = $("#full_name").val();
        let state = $("#state").val();
        let mobile_number = parseInt($("#mobile_number").val());
        let district = $("#district").val();
        let pincode = parseInt($("#pincode").val());
        let drivinglisence = $("#drivinglisence").val();
        let otp = parseInt($("#otp").val());
        let date = new Date();
        let timestamp = parseInt(date.getTime());
        let payload = {}
        let tokey;
        if (actype == "farmer") {
            payload.Action = 0;
            payload.reg_far = {};
            payload.reg_far.aadhar_card = aadhar_card;
            payload.reg_far.timestamp = timestamp;
            payload.reg_far.full_name = full_name;
            payload.reg_far.State = state;
            payload.reg_far.pincode = pincode;
            payload.reg_far.mobilenumber = mobile_number;
            payload.reg_far.district = district;
            //payload.reg_far.photo = "";
            payload.reg_far.otp = otp;
            tokey = sawtooth.get_farmer_address(signer)
        } else if (actype == "buyer") {
            payload.Action = 1;
            payload.reg_buy = {};
            payload.reg_buy.aadhar_card = aadhar_card;
            payload.reg_buy.timestamp = timestamp;
            payload.reg_buy.full_name = full_name;
            payload.reg_buy.State = state;
            payload.reg_buy.pincode = pincode;
            payload.reg_buy.mobilenumber = mobile_number;
            payload.reg_buy.district = district;
            //payload.reg_far.photo = "";
            payload.reg_buy.otp = otp;
            tokey = sawtooth.get_buyer_address(signer)
        } else if (actype == "transporter") {
            payload.Action = 2;
            payload.reg_tra = {}
            payload.reg_tra.aadhar_card = aadhar_card;
            payload.reg_tra.timestamp = timestamp;
            payload.reg_tra.full_name = full_name;
            payload.reg_tra.State = state;
            payload.reg_tra.pincode = pincode;
            payload.reg_tra.mobilenumber = mobile_number;
            payload.reg_tra.district = district;
            payload.reg_tra.driving_license = drivinglisence;
            //payload.reg_far.photo = "";
            payload.reg_tra.otp = otp;
            tokey = sawtooth.get_transporter_address(signer)
        }
        let pbf = new Pbf();
        protobuf.Realpayload.write(payload, pbf)
        let otpTransactionKey = sawtooth.get_otp_address(mobile_number, otp)
        console.log(otpTransactionKey)
        let payloadBytes = pbf.finish();
        let trans_header = sawtooth.getTransactionHeader(signer, [tokey, otpTransactionKey], payloadBytes, [txn_id]);
        let transaction = sawtooth.getTransaction(signer, trans_header, payloadBytes);
        let batch_header = sawtooth.getBatchHeader(signer, [transaction]);
        let batch = sawtooth.getBatch(signer, batch_header, [transaction])
        //console.log(new TextDecoder().decode(payloadBytes))
        sawtooth.sendBatch(batch)
    });
});
