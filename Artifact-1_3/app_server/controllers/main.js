

const inventoryEndpoint = 'http://localhost:3000/api/inventory';
const option = {
    method: ['GET', 'PUT'],
            
    headers: {
        'Accept' : 'application/json'
    }
}

/* GET homepage */
const index = async function(req, res, next) {
    await fetch(inventoryEndpoint, option)
        .then(res => res.json())
        .then(json => {
            res.render('index', {title: 'Grocer Inventory Management', items : json})
                
        })
        .catch(err => res.status(500).send(e.message));
    //res.render('index', {title: 'Grocer App', items});
};

    
        



module.exports = {
    index
    
};