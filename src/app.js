const express = require('express')
const path = require("path")
const hbs = require("hbs");
const mongoose =require("mongoose");

const alert =require("alert");


require("./db/conn");

// const login = require("./models/LoginUsers");

const app = express()
const port = 80

// FOR GETTIN GHE DATA FROM FORM
app.use(express.json())
app.use(express.urlencoded({
  extended:true
}))


// ----------------------------------------
const templates_path = path.join(__dirname, "../templates/views");
const partials_path = path.join(__dirname, "../templates/partials");
const public_path = path.join(__dirname, "../public");
app.use(express.static(path.join(public_path)));
app.set("view engine", "hbs");
app.set("views",templates_path);
hbs.registerPartials(partials_path);


app.get('/', (req, res) => {
  res.render("index");

})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})




// AUTHENTICATION
  


app.post('/main', (req, res) => {

  const userName = req.body.user;
  const userPass = req.body.password;
  const Loginschema = new mongoose.Schema({ user: 'string', password: 'string' });

  const login = new mongoose.model(req.body.role, Loginschema);

  login.find({user:userName}, function(err, users){

      try{
            if(userPass == users[0].password)
              {
                res.render("main");
              }
       
        }
        catch
        {
           alert("Access Denied!");

        }

    
  
    
  
  })
 

})
