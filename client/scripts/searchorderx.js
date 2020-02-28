const request = require('request')
const $ = require('jquery');



$(document).ready(function () {


    let handleData;
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

    $("#search").click(function () {
        let assetType = $("#assettype").val();
        let assetValue = $("#assettypespecific").val();
        let price = $("#price").val();
        let pincode = $("#pincode").val();
        let ordertype = $('input[name=order]:checked').val();
        let weight = $("#weight").val();
        let payload = { ordertype: ordertype, assetType: assetType, assetValue: assetValue, price: price, pincode: pincode, weight: weight }

        request.post({
            url: 'http://127.0.0.1:6060/searchOrder',
            body: JSON.stringify(payload),
            headers: { 'Content-Type': 'application/json' }
        }, (err, response) => {
            if (err) return console.log(err)
            console.log(response.body)

            let data = JSON.parse(response.body);
            handleData = data;

            for (let d in data['data']) {

                let g = "<div>Asset Type: " + data['data'][d].assetType + "<br>Asset Value:" + data['data'][d].assetValue + "<br>Price: " + data['data'][d].price + "<br>Pincode: " + data['data'][d].pincode + "<br><br><button id=" + data['data'][d].nounce + ">" + ordertype + "</button></div>";
                console.log(g)
                $("#rl").append(g);
            }
            $("#sr").show();
        })
    })



});