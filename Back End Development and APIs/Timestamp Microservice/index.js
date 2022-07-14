// index.js
// where your node app starts

// init project
var express = require('express');
var app = express();

// enable CORS (https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
// so that your API is remotely testable by FCC 
var cors = require('cors');
app.use(cors({ optionsSuccessStatus: 200 }));  // some legacy browsers choke on 204

// http://expressjs.com/en/starter/static-files.html
app.use(express.static('public'));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (_req, res)
{
    res.sendFile(__dirname + '/views/index.html');
});

// your first API endpoint... 
app.get("/api/hello", function (_req, res)
{
    res.json({ greeting: 'hello API' });
});

// TimeStamp API endpoint
app.get("/api/:date?", (req, res) => {
    const givenDate = req.params.date || new Date();

    const checkUnixTime = givenDate * 1;
    const date = isNaN(checkUnixTime) ? new Date(givenDate) : new Date(checkUnixTime);

    if (date == "Invalid Date")
    {
        return res.json({ error: "Invalid Date" });
    }
  
    const unix = date.getTime();
    const utc = date.toUTCString();

    res.json({ unix, utc });
});

// listen for requests :)
var listener = app.listen(process.env.PORT, function () 
{
    console.log('Your app is listening on port ' + listener.address().port);
});
