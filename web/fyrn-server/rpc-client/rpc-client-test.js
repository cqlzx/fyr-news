const client = require('./rpc-client');


client.add(1, 2, (res) => {
    console.assert(res === 3);
});

client.getNewsSummariesForUser('test_user', 1, (response) => {
    console.assert(response !== null);
});