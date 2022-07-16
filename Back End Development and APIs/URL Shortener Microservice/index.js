require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();
const bodyParser = require("body-parser");
const vu = require("valid-url");
const mongoose = require("mongoose");

const connection = mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true, serverSelectionTimeoutMS: 5000 });

// Basic Configuration
const port = process.env.PORT || 3000;

const urlSchema = new mongoose.Schema({
  url: { type: String, required: true }
});

const Url = mongoose.model("Url", urlSchema);

app.use(cors());

app.use(bodyParser.urlencoded({ extended: false }));
app.use('/public', express.static(`${process.cwd()}/public`));

app.get('/', function(req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

// Your first API endpoint
app.get('/api/hello', function(req, res) {
  res.json({ greeting: 'hello API' });
});

// Url Shorter POST endpoint
app.post("/api/shorturl", function(req, res)
{
    if (!vu.isWebUri(req.body.url))
    {
      return res.json({ "error": "invalid URL" });
    }

  const urlExist = Url.findOne({ url: req.body.url }, (err, data) => {
    if(err) return console.error(err);
    
    if(data != null)
    {
      return res.json({ original_url: req.body.url, short_url: data._id });
    }
  });
    
    const newUrl = new Url({ url: req.body.url });
  
    newUrl.save((err2, data2) => {
      if(err2) console.error(err);
      res.json({ original_url: req.body.url, short_url: data2._id });
    });
});

// Url Shorter GET endpoint
app.get("/api/shorturl/:id?", function(req, res) {
  const id = req.params.id;
  if(!id) res.json({ error: 'invalid id' });
  Url
    .findById(id, (err, data) => {
      if(err) return res.json(err);
      res.redirect(data.url);
    });
});

app.listen(port, function() {
  console.log(`Listening on port ${port}`);
});
