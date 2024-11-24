import { configureStore } from '@reduxjs/toolkit';
import resumeReducer from './slice/resumeslice';
import detailsReducer from './slice/detailsslice';
import questionnaireReducer from './slice/questionslice';
import messagesReducer from './slice/messagesslice';
const store = configureStore({
  reducer: {
    resume: resumeReducer,
    details: detailsReducer,
    questionnaire: questionnaireReducer,
    messages: messagesReducer,
  },
});

export default store;
