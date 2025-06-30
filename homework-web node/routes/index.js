const express = require("express");
const router = express.Router();
const task = require("../models/taskWebApp");

router.get("/", async (req, res) => {
  const tasks = await task.find();

  res.render("index", {
    layout: "layouts/main",  
    title: "Home Page",
    tasks
  });
});

router.get('/tambah-task', async (req, res) => {
  try {
    const tasks = await task.find(); // Ambil data dari MongoDB

    res.render('task', { // Render file view 'task.ejs'
      title: 'Task Page',
      layout: 'layouts/main',
      tasks: tasks, // Kirim variabel 'tasks' ke EJS
    });

  } catch (error) {
    console.error('Error saat mengambil data dari database:', error);
    res.status(500).send('Terjadi kesalahan pada server');
  }
});

module.exports = router;
