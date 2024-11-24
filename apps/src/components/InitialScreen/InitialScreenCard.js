import { Box, Typography } from "@mui/material";
import { MdOutlineSupportAgent } from "react-icons/md";
import { IoInformationCircleSharp } from "react-icons/io5";
import { FaPeopleGroup } from "react-icons/fa6";
import { GiStarShuriken } from "react-icons/gi";

const data = [
    {
        img: <FaPeopleGroup fontSize={30}/>,
        message: "Ask any questions related to the candidate"
    },
    {
        img: <MdOutlineSupportAgent fontSize={30}/>,
        message: "Get insights about the candidate before hiring"
    },
    {
        img: <IoInformationCircleSharp fontSize={30}/>,
        message: "Analyze the resumes with ease using Natural Language"
    },
    {
        img: <GiStarShuriken fontSize={30}/>,
        message: "Fire up a conversation using the built-in memory"
    },
]

export const InitialScreenCard = ({index})=>{

    return(
        <Box className="initialScreenCard" style={{width:'150px', height:'150px', border:'1px solid black', borderRadius:'10px', padding:'10px'}}>
            <Box>
                {data[index].img}
            </Box>
            <Box>
                <Typography style={{fontFamily:'monospace'}}>
                    {data[index].message}
                </Typography>
            </Box>
        </Box>
    )
}