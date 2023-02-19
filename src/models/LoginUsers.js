const mongoose =require("mongoose");


const Loginschema = new mongoose.Schema({ user: 'string', password: 'string' });

const login = new mongoose.model('login', Loginschema);

module.exports = login;
