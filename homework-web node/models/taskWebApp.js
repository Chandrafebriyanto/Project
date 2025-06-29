const mongoose = require("mongoose");

const task = mongoose.model("task", {
  tittle: {
    type: String,
    required: true,
  },
  dateline: {
    type: Date,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  link: {
    type: String,
    required: true,
  },

});
