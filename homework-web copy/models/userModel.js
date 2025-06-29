const mongoose = require('mongoose')

const user = mongoose.Schema({
    subject: {
        type: String,
        required: true,
    },
    description: {
        type: String,
        required: true,
    },
    dateline: {
        type: Date,
        required: true,
    },
})

module.exports = user