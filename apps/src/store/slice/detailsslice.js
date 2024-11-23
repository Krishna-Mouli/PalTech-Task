import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  details: null,
};

const detailsSlice = createSlice({
  name: 'details',
  initialState,
  reducers: {
    setDetails(state, action) {
      state.details = action.payload;
    },
    clearDetails(state) {
      state.details = null;
    },
  },
});

export const { setDetails, clearDetails } = detailsSlice.actions;
export default detailsSlice.reducer;
