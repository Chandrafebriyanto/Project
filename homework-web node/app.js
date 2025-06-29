const express = require('express');
const expressLayouts = require('express-ejs-layouts'); 
const mongoose = require('mongoose');
const flash = require('connect-flash');
const task = require('./models/taskWebApp');

// Middleware
const methodOverride = require('method-override');
const session = require('express-session');
const cookieParser = require('cookie-parser');

// Express app
const app = express();

// MongoDB connection
mongoose.connect('mongodb://127.0.0.1:27017/task-web-app', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));
app.use(methodOverride('_method'));
app.use(cookieParser('secretKey'));
app.use(session({
  cookie: { maxAge: 6000 },
  secret: 'secretKey',
  resave: true,
  saveUninitialized: true
}));
app.use(flash());

// View engine
app.set('view engine', 'ejs');
app.use(expressLayouts);

// Flash message middleware
app.use((req, res, next) => {
  res.locals.success_msg = req.flash('success');
  res.locals.error_msg = req.flash('error');
  next();
});

// Routes
app.use('/', require('./routes/index'));

// Server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
