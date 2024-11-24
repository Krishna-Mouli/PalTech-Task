import { createSlice } from '@reduxjs/toolkit';
 
const initialState = {
    messages : [],
    snackBarOpen : false
} 
export const messagesSlice = createSlice({
  name: 'messages',
  initialState,
  reducers: {
    setMessages: (state, action)=>{
        state.messages = action.payload
    },
    setSnackBarOpen : (state, action)=>{
      state.snackBarOpen = action.payload
  },
  }
})
 
export const {
    setMessages, setSnackBarOpen
} = messagesSlice.actions
 
export default messagesSlice.reducer