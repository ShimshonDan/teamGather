const {Schema, model} = require("moongoose")

const UserShema = Schema({
    e_mail: {type:String, unique:true, required: true},
    password: {type:String, unique:true, required: false},
    isActivated: {type:Boolean, default:false},
    activatedLink: {type:String}
});

module.exports = model("User", UserShema);