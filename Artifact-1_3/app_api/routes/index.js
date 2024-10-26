const express = require('express');
const router = express.Router();
const cors = require('cors')
const itemController = require('../controllers/inventory');

router.use(cors());
// find entire list
router.get('/inventory', itemController.itemList);


// Search for individual
router.get('/inventory/:itemName', itemController.itemFindByName);

router.post("/inventory", itemController.createItem);

router.delete('/inventory/:itemName', itemController.itemDelete);

router.route('/inventory/:itemName').put(itemController.update);

module.exports = router;