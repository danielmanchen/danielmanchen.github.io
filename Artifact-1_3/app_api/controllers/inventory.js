const mongoose = require('mongoose');
const items = require('../models/inventory');
const Model = mongoose.model('Inventory');

// Get items from inventory
const itemList = async(req, res) => {
    const q = await Model.find({}).exec();

    //console.log(q);

    if(!q)
    {
        
        return res.status(404).json(q);
    }
    else
    {
        return res.status(200).json(q);
    }
};

const itemFindByName = async(req, res) => {
    const q = await Model.find({'itemName' : req.params.itemName}).exec();

    console.log(q);

    if(!q)
    {
        
        return res.status(404).json(q);
    }
    else
    {
        return res.status(200).json(q);
    }
};

const createItem = async(req, res) => {
    const q = await Model.insertOne({req}).exec();

    //console.log(q);

    if(!q)
    {
        
        return res.status(404).json(q);
    }
    else
    {
        return res.status(200).json(q);
    }
};

const update = async(req, res) => {
    
    let result = await Model.findOneAndUpdate({'itemName' : req.params.itemName}, {'quantity' : req.params.quantity}).exec();
    res.send(result);
};

const itemDelete = async(req, res) => {
    const q = await Model.deleteOne({'itemName' : req.params.itemName}).exec();
    
    res.send(q);
};

module.exports = {
    itemList,
    itemFindByName,
    createItem,
    update,
    itemDelete
    
};