import React from 'react';
import { useSelector } from 'react-redux';
import '../styles/theme.css';

const View = () => {
  const resume = useSelector((state) => state.resume.file);

  if (!resume) {
    return  (
    <div 
        className='theme'  
        style={{
          display: 'flex', 
          justifyContent: 'center', 
          alignItems: 'center',    
          textAlign: 'center',     
          flexDirection: 'column', 
          height: '100vh'         
        }}
    >
        <p>No resume selected. Please upload a resume.</p>
    </div>
    );
  }

  return (
    <div >
        <div
        style={{
            display: 'flex', 
            alignItems: 'center',  
            textAlign: 'center',   
            flexDirection: 'column',
          }}>
        <h2>Uploaded Resume</h2>
        <p>{resume.name}</p> 
        </div>
      {resume.type === 'application/pdf' && (
        <embed
          src={URL.createObjectURL(resume)}
          type="application/pdf"
          width="100%"
          height="600px"
          display="block"
        />
      )}
    </div>
  );
};

export default View;
