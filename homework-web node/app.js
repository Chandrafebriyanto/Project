const express = require("express");
const expressLayouts = require("express-ejs-layouts");
const mongoose = require("mongoose");
const flash = require("connect-flash");
// const { MongoClient, ServerApiVersion } = require("mongodb");

// Middleware
const methodOverride = require("method-override");
const session = require("express-session");
const cookieParser = require("cookie-parser");

// Express app
const app = express();

// MongoDB connection
mongoose.connect("mongodb://127.0.0.1:27017/task-web-app"); //note: task-web-app nama database
// const uri = "mongodb+srv://Candra:C123470r@dbonline.seg3bcu.mongodb.net/?retryWrites=true&w=majority&appName=dbOnline";

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));
app.use(methodOverride("_method"));
app.use(cookieParser("secretKey"));
app.use(
  session({
    cookie: { maxAge: 6000 },
    secret: "secretKey",
    resave: true,
    saveUninitialized: true,
  })
);
app.use(flash());

// View engine
app.set("view engine", "ejs");
app.use(expressLayouts);

// Flash message middleware
app.use((req, res, next) => {
  res.locals.success_msg = req.flash("success");
  res.locals.error_msg = req.flash("error");
  next();
});

// Routes
app.use("/", require("./routes/index"));

// // Create a MongoClient with a MongoClientOptions object to set the Stable API version
// const client = new MongoClient(uri, {
//   serverApi: {
//     version: ServerApiVersion.v1,
//     strict: true,
//     deprecationErrors: true,
//   },
// });
// async function run() {
//   try {
//     // Connect the client to the server	(optional starting in v4.7)
//     await client.connect();
//     // Send a ping to confirm a successful connection
//     await client.db("admin").command({ ping: 1 });
//     console.log(
//       "Pinged your deployment. You successfully connected to MongoDB!"
//     );
//   } finally {
//     // Ensures that the client will close when you finish/error
//     await client.close();
//   }
// }
// run().catch(console.dir);

// Server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
