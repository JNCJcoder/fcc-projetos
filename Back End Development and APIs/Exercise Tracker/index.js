const express = require('express')
const app = express()
const cors = require('cors')
const bodyParser = require("body-parser")
const mongoose = require("mongoose");
require('dotenv').config()

mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const exerciseSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  description: String,
  duration: Number,
  date: Date
});

const userSchema = new mongoose.Schema({
  username: String
});

const User = mongoose.model("UserExercise", userSchema);

const Exercise = mongoose.model("Exercise", exerciseSchema);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors())
app.use(express.static('public'))

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html')
});

app.post("/api/users", (req, res) => {
  const newUser = new User({ username: req.body.username });
  
  newUser.save((err, data) => {
    if(err || !data)
    {
      return res.send("Error saving the user")
    }
    res.json(data)
  })
})

app.get("/api/users", (req, res) => {
  User.find({}, (err, data) => {
    if(!data)
    {
      return res.send("No users found")
    }
    
    res.json(data)
  })
})

app.post("/api/users/:id/exercises", (req, res) => {
  const id = req.params.id
  const { description, duration, date } = req.body
  
  User.findById(id, (err, userData) => {
    if(err || !userData)
    {
      return res.send("User not found");
    }
    
    const newExercise = new Exercise({
      userId: id, 
      description,
      duration,
      date: new Date(date), 
    });
    
    newExercise.save((err, data) => {
      if(err || !data)
      {
        return res.send("Error saving this exercise")
      }
      
      res.json({
        username: userData.username,
        description: data.description,
        duration: data.duration,
        date: data.date.toDateString(),
        _id: userData.id
      });
    })
  })
})

app.get("/api/users/:id/logs", (req, res) => {
  const { id } = req.params;
  const { from, to, limit } = req.query;
  
  User.findById(id, (err, userData) => {
    if(err || !userData)
    {
      return res.send("user not found");
      console.log('user not found');
    }
    
    let dateObj = {}
    
    if(from)    dateObj["$gte"] = new Date(from)
    if(to)      dateObj["$lte"] = new Date(to)
    
    let filter = { userId: id }
    
    if(from || to) filter.date = dateObj
    
    let nonNullLimit = Number(limit) ?? 500
    
    Exercise.find(filter).limit(+nonNullLimit).exec((err, data) => {
      if(err || !data)
      {
        return res.json([])
        console.log('deu erro');
      }
      
      const log = data.map(item => ({
        description: item.description,
        duration: Number(item.duration),
        date: item.date.toDateString()
      }))
      
      console.log({
        username: userData.username,
        count: Number(data.length),
        _id: userData._id,
        log
      });
      
      res.json({
        username: userData.username,
        count: Number(data.length),
        _id: userData._id,
        log
      })
    }) 
  })
})

const listener = app.listen(process.env.PORT || 3000, () => {
  console.log('Your app is listening on port ' + listener.address().port)
})
