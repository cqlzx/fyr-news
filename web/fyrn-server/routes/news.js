const express = require('express');
const rpc_client = require('../rpc-client/rpc-client');
const router = express.Router();

router.get('/userId/:userId/pageNum/:pageNum', function(req, res) {
    console.log('get news is called!');

    userId = req.params['userId'];
    pageNum = req.params['pageNum'];

    rpc_client.getNewsSummariesForUser(userId, pageNum, (res) => {
        res.json(res);
    });
});

module.exports = router;