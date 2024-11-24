
import Navbar from './components/navbar';
import Chat from './pages/chat';
import Details from './pages/details';
import Questionnaire from './pages/questionnaire';
import View from './pages/view';
import UploadPage from './components/upload';
import { BrowserRouter as Router, Routes, Route, Navigate, Outlet   } from 'react-router-dom';

function App() {
  const ProcessLayout = () => {
    return (
      <div>
        <Navbar /> 
        <div style={{ marginTop: '64px' }}>
          <Outlet />
        </div>
      </div>
    );
  };
  return (
    <div>
      <Router>      
        <Routes>
          <Route path="/" element={<UploadPage />} />  
          <Route path="/process" element={<ProcessLayout />}>
            <Route index element={<Navigate to="view" />} />
            <Route path="view" element={<View />} />
            <Route path="details" element={<Details />} />
            <Route path="chat" element={<Chat />} />
            <Route path="questionnaire" element={<Questionnaire />} />
          </Route>  
        </Routes>
      </Router>
    </div>
  );
}

export default App;
