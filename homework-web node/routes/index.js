const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('index', {
    layout: 'layouts/main',
    title: 'Home Page'
  });
});

router.get('/task', (req, res) => {
  res.render('task', {
    layout: 'layouts/main',
    title: 'Task Page'
  });
});

module.exports = router;
