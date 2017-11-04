const jayson = require('jayson');

// create a client
const client = jayson.client.http({
    port: 4040,
    hostname: 'localhost'
});

// invoke "add"

function add(num1, num2, callback) {
    client.request('add', [num1, num2], function (err, response) {
        if (err) throw err;
        console.log(response.result); // 2
        callback(response.result);
    });
}


function getNewsSummariesForUser(userId, pageNum, callback) {
    client.request('get_news_summaries_for_user', [userId, pageNum], (err, error, response) => {
        if (err) throw err;
        console.log(response);
        callback(response);
    })
}

// Log a news click event for a user
function logNewsClickForUser(user_id, news_id) {
    client.request('log_news_click_for_user', [user_id, news_id], function (err, error, response) {
        if (err) throw err;
        console.log(response);
    });
}

module.exports = {
    add: add,
    getNewsSummariesForUser: getNewsSummariesForUser,
    logNewsClickForUser: logNewsClickForUser
};