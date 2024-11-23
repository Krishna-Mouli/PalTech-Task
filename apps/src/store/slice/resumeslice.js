import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  file: null,
};

const resumeSlice = createSlice({
  name: 'resume',
  initialState,
  reducers: {
    setResume(state, action) {
      state.file = action.payload;
    },
    clearResume(state) {
      state.file = null;
    },
  },
});

export const { setResume, clearResume } = resumeSlice.actions;
export default resumeSlice.reducer;
