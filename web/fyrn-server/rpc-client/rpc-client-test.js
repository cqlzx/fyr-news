const client = require('./rpc-client');


client.add(1, 2, (res) => {
    console.assert(res === 3);
});