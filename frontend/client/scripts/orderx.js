const request = require('request')
const $ = require('jquery');
const sawtooth = require('./sawtooth')
var timers = require('timers');
var setTimeout = timers.setTimeout
$(document).ready(function () {
    let signer;
    let nounce;
    if (!window.localStorage.privateKey) {
        window.location.href = "register.html";
    } else {
        signer = sawtooth.privateKeyFromHex(window.localStorage.privateKey);
    }
    request.get({
        url: 'http://127.0.0.1:6060/nounce/' + sawtooth.getPublicKeyHex(signer)
    }, (err, response) => {
        if (err) return console.log(err)
        console.log(response.body)
        let data = JSON.parse(response.body);
        nounce = data.nounce

    })

    request.get({
        url: 'http://127.0.0.1:6060/getAssetTypes'
    }, (err, response) => {
        if (err) return console.log(err)
        console.log(response.body)
        let data = JSON.parse(response.body);
        for (let type in data.types) {
            $("#assettype").append('<option value="' + data.types[type] + '">' + data.types[type] + '</option>');
        }
        $("#assettype").show();

        request.get({
            url: 'http://127.0.0.1:6060/getAssetTypes/' + $("#assettype").val()
        }, (err, response) => {
            if (err) return console.log(err)
            console.log(response.body)
            let data = JSON.parse(response.body);
            for (let type in data.values) {
                $("#assettypespecific").append('<option value="' + data.values[type] + '">' + data.values[type] + '</option>');
            }
            $("#assettypespecific").show();

        })

    })

    $('input[type=radio][name=order]').change(function () {

        if (this.value == "buy") {
            $("#buyo").show();
            $("#sello").hide();
        } else if (this.value == "sell") {
            $("#sello").show();
            $("#buyo").hide();
        }
    })


    $("#assettype").change(function () {

        $("#assettypespecific").empty();
        request.get({
            url: 'http://127.0.0.1:6060/getAssetTypes/' + $("#assettype").val()
        }, (err, response) => {
            if (err) return console.log(err)
            console.log(response.body)
            let data = JSON.parse(response.body);
            for (let type in data.values) {
                $("#assettypespecific").append('<option value="' + data.values[type] + '">' + data.values[type] + '</option>');
            }


        })

    });
    $("#sello").click(function () {
        let assetType = $("#assettype").val();
        let assetValue = $("#assettypespecific").val();
        let publicKey = sawtooth.getPublicKeyHex(signer);
        let price = $("#price").val();
        let pincode = $("#pincode").val();
        let weight = $("#weight").val();
        let payload = { assetType: assetType, assetValue: assetValue, price: parseInt(price), nounce: nounce, pincode: pincode, weight: weight }
        let payloadFinal = { payload: sawtooth.Base64.encode(JSON.stringify(payload)), signature: sawtooth.getSignature(signer, sawtooth.Base64.encode(JSON.stringify(payload))), publicKey: publicKey }
        request.post({
            url: 'http://127.0.0.1:6060/makeSellOrder',
            body: JSON.stringify(payloadFinal),
            headers: { 'Content-Type': 'application/json' }
        }, (err, response) => {
            if (err) return console.log(err)
            console.log(response.body)
	    $('#selloo').hide();
	    $('#sellooi').append('<img src="payment-.gif" alt="Cinque Terre" width=100% height="400px">');
		  setTimeout(function(){ console.log('hello'); window.location.replace = 'searchOrder.html'; }, 3000);


        })

    });

    $("#buyo").click(function () {

        let assetType = $("#assettype").val();
        let assetValue = $("#assettypespecific").val();
        let publicKey = sawtooth.getPublicKeyHex(signer);
        let price = $("#price").val();
        let pincode = $("#pincode").val();
        let weight = $("#weight").val();
        let payload = { assetType: assetType, assetValue: assetValue, price: parseInt(price), nounce: nounce, pincode: pincode, weight: weight }
        let payloadFinal = { payload: sawtooth.Base64.encode(JSON.stringify(payload)), signature: sawtooth.getSignature(signer, sawtooth.Base64.encode(JSON.stringify(payload))), publicKey: publicKey }
        request.post({
            url: 'http://127.0.0.1:6060/makeBuyOrder',
            body: JSON.stringify(payloadFinal),
            headers: { 'Content-Type': 'application/json' }
        }, (err, response) => {
            if (err) return console.log(err)
            console.log(response.body)
        })

    });

});



/*
function makeHttprequest(data) {
    request.post({
        url: 'http://127.0.0.1:6060/makeSellOrder',
        body: data,
        headers: { 'Content-Type': 'application/json' }
    }, (err, response) => {
        if (err) return console.log(err)
        console.log(response.body)
    })
}

makeHttprequest(JSON.stringify({ "lol": "dol" }))
*/
