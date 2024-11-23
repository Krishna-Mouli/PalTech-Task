import { configureStore } from '@reduxjs/toolkit';
import resumeReducer from './slice/resumeslice';
import detailsReducer from './slice/detailsslice'

const store = configureStore({
  reducer: {
    resume: resumeReducer,
    details: detailsReducer,
  },
});

export default store;
