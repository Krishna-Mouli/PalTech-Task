import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  questions: null, 
};

const questionnaireSlice = createSlice({
  name: 'questionnaire',
  initialState,
  reducers: {
    setQuestions(state, action) {
      state.questions = action.payload;
    },
    clearQuestions(state) {
      state.questions = null;
    },
  },
});

export const { setQuestions, clearQuestions } = questionnaireSlice.actions;
export default questionnaireSlice.reducer;
