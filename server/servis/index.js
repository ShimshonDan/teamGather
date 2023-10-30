require("dotenv").config()

const express = require("express");
const cors = require("cors");
const cookieParser = require("cookie-parser");

const mongouse = require("mongoose");

const app = express();
app.use(express.json());
app.use(cookieParser());
app.use(cors());


const PORT = process.env.Port||7000;
const start = async()=>{
    try{
        await mongouse.connect(process.env.DB_URL, {
            useNewURLParser: true,
            useUnifiedTopology: true
        });
        app.listen(PORT, ()=>console.log('Server worked on Port = ' + PORT));
    } catch(e){
        console.log(e);
    }
}

start()