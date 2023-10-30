const {Schema, model} = require("moongoose")

const TokenShema = Schema({
   refreshToken:{type: String, required:true},
   user:{type:Schema.Types.ObjectId, ref:"User"}
});

module.exports = model("User", TokenShema);