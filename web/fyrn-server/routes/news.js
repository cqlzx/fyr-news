const express = require('express');
const rpc_client = require('../rpc-client/rpc-client');
const router = express.Router();

router.get('/userId/:userId/pageNum/:pageNum', function(req, res) {
    console.log('get news is called!');

    userId = req.params['userId'];
    pageNum = req.params['pageNum'];

    rpc_client.getNewsSummariesForUser(userId, pageNum, (response) => {
        res.json(response);
    });
});

router.post('/userId/:userId/newsId/:newsId', function(req, res, next) {
    console.log('logging news click');

    userId = req.params['userId'];
    newsId = req.params['newsId'];

    rpc_client.logNewsClickForUser(userId, newsId);
    res.status(200);
});

module.exports = router;