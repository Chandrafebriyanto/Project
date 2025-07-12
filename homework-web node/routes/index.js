const express = require("express");
const router = express.Router();
const task = require("../models/taskWebApp");
const Task = require("../models/taskWebApp");

router.get("/", async (req, res) => {
  const tasks = await task.find();

  res.render("index", {
    layout: "layouts/main",
    title: "Home Page",
    heading: "Information Web Programming Class",
    tasks,
  });
});

router.get("/task", async (req, res) => {
  try {
    const tasks = await task.find();

    res.render("task", {
      title: "Task Page",
      layout: "layouts/main",
      heading: "Task",
      tasks,
    });
  } catch (error) {
    res.status(500).send("Terjadi kesalahan pada server");
  }
});

router.get("/task/create", (req, res) => {
  try {
    res.render("create", {
      title: "Create Page",
      layout: "layouts/main",
      heading: "Create Task",
    });
  } catch (error) {
    res.status(500).send("Terjadi kesalahan pada server");
  }
});

router.post("/task/create", async (req, res) => {
  try {
    await task.insertOne(req.body);
    res.redirect("/task");
  } catch (error) {
    res.status(500).send("Terjadi kesalahan pada server");
  }
});

router.get("/task/delete/:id", async (req, res) => {
  try {
    await task.deleteOne({ _id: req.params.id });
    res.redirect("/task");
  } catch (error) {
    console.error(error);
    res.status(500).send("Terjadi kesalahan pada server");
  }
});

router.get("/task/edit/:id", async (req, res) => {
  const task = await Task.findOne({ _id: req.params.id });
  res.render("edit", {
    title: "Edit Page",
    layout: "layouts/main",
    heading: "Edit Task",
    task,
  });
});

router.post("/task/edit/:id", async (req, res) => {
    await Task.updateOne({ _id: req.params.id }, { $set: req.body });
    res.redirect("/task");
});

module.exports = router;
