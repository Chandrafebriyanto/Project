import user  from "../models/userModel";
export const getUsers = async (req,res) => {
    try {
        const users = await user.find()
        res.json(users)
    } catch (error) {
        res.status(500).json({message: error.message})
    }
}