const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const inventorySchema = new Schema({
    itemName: {type: String, required: true},
    quantity: {type: Number, required: true},
    serNo: {type: Number, required: true}
}, {collection : 'Inventory'});

module.exports = mongoose.model("Inventory", inventorySchema)