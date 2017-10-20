const jayson = require('jayson');

// create a client
const client = jayson.client.http({
    port: 4040,
    hostname: 'localhost'
});

// invoke "add"

function add(num1, num2, callback) {
    client.request('add', [num1, num2], function(err, response) {
        if(err) throw err;
        console.log(response.result); // 2
        callback(response.result);
    });
}


module.exports = {
    add: add
};