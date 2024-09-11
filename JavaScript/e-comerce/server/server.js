const express = require("express");
const app = express();
const cors = require("cors");
const mercadopago = require("mercadopago");
const path = require('path')

// REPLACE WITH YOUR ACCESS TOKEN AVAILABLE IN: https://developers.mercadopago.com/panel


const config = new mercadopago.MercadoPagoConfig({
	access_token: "TEST-3755708515207387-091111-e4ec628606559989aa8eff51e80f9405-253493776"
});




app.use(express.urlencoded({ extended: false }));
app.use(express.json());
/* app.use(express.static("../../client/html-js")); */
app.use(express.static(path.join(__dirname,"../client")))
app.use(cors());
app.get("/", function (req, res) {
    res.sendFile(path.join(__dirname, "../client/media", "index.html"));
});

app.post("/create_preference", (req, res) => {
	console.log("este es el req: "+req.body)
	let preference = {
		items: [
			{
				title: req.body.description,
				unit_price: Number(req.body.price),
				quantity: Number(req.body.quantity),
			}
		],
		back_urls: {
			"success": "http://localhost:8080/feedback",
			"failure": "http://localhost:8080/feedback",
			"pending": ""
		},
		auto_return: "approved",
	};

	mercadopago.preferences.create(preference)
		.then(function (response) {
			res.json({
				id: response.body.id
			});
		}).catch(function (error) {
			console.log(error);
		});
});

app.get('/feedback', function (req, res) {
	res.json({
		Payment: req.query.payment_id,
		Status: req.query.status,
		MerchantOrder: req.query.merchant_order_id
	});
});

app.listen(8080, () => {
	console.log("The server is now running on Port 8080");
});