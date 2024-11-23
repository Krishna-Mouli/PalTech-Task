import React, { useState } from 'react';
import { Box, Typography, Button } from '@mui/material';
import OfflinePinIcon from '@mui/icons-material/OfflinePin';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { setResume } from '../store/slice/resumeslice';
import { setDetails } from '../store/slice/detailsslice';
import CircularProgress from '@mui/material/CircularProgress';

const UploadPage = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [loading, setLoading] = useState(false); // Manage loading state
    const navigate = useNavigate();
    const dispatch = useDispatch();

    const onFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedFile(file);
        }
    };

    const onUploadEvent = async () => {
        if (!selectedFile) {
            alert("No file selected!");
            return;
        }

        setLoading(true); // Start the loading indicator

        const formData = new FormData();
        formData.append("file", selectedFile);

        try {
            const response = await fetch('http://localhost:8000/api/v1/files/sourceid/123456/resumeid/f8b7c3a1-9d2e-4f5b-8c7a-6d4e3f2b1a9c/ingest', {
                method: 'POST',
                body: formData,
            });             
            if (response.ok) 
            { 
                dispatch(setResume(selectedFile));
                const detailsResponse = await fetch('http://127.0.0.1:8000/api/v1/resume/sourceid/123456/resumeid/f8b7c3a1-9d2e-4f5b-8c7a-6d4e3f2b1a9c/getdetails');
                if (detailsResponse.ok) 
                {
                    const detailsData = await detailsResponse.json();
                    dispatch(setDetails(detailsData)); 
                    setLoading(false);
                    alert("File uploaded and details fetched successfully!");
                    navigate('/process/view');
                } 
                else 
                {
                    setLoading(false);
                    console.error("Failed to fetch extracted details");
                }                                
            } 
            else 
            {
                alert("File upload failed!");
            }
        } catch (error) {
            setLoading(false);
            console.error("Error uploading file:", error);
            alert("An error occurred during file upload.");
        }
    };

    return (
        <Box
            sx={{
                bgcolor: '#000000',
                color: 'text.primary',
                minHeight: '100vh',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                alignItems: 'center',
                textAlign: 'center',
                padding: 0,
                margin: 0,
            }}
        >
            <Typography
                variant="h2"
                sx={{
                    background: 'linear-gradient(to right, darkcyan, cyan)',
                    WebkitBackgroundClip: 'text',
                    WebkitTextFillColor: 'transparent',
                    fontFamily: 'Courier',
                    fontWeight: 900,
                    marginBottom: 4,
                }}
            >
                Hello there, Please upload a resume to begin Processing....
            </Typography>
            {loading ? (                
                <Box
                    sx={{
                        display: 'flex',
                        flexDirection: 'column',
                        justifyContent: 'center',
                        alignItems: 'center',
                        textAlign: 'center',
                        height: '100px',
                    }}
                >
                    <CircularProgress />
                    <Typography variant="body2" sx={{ marginTop: 2, color: 'cyan' }}>
                        Uploading, please wait...
                    </Typography>
                </Box>
            ) : (
                <>
                    <input
                        type="file"
                        id="fileInput"
                        style={{ display: 'none' }} // Hide the input field
                        onChange={onFileChange}
                    />
                    <Button
                        variant="outlined"
                        startIcon={<OfflinePinIcon />}
                        onClick={() => document.getElementById('fileInput').click()}
                        sx={{ marginBottom: 2 }}
                    >
                        Select Resume
                    </Button>
                    {selectedFile && (
                        <Typography
                            variant="body1"
                            sx={{ color: 'cyan', marginBottom: 2 }}
                        >
                            Selected File: {selectedFile.name}
                        </Typography>
                    )}
                    <Button
                        variant="outlined"
                        startIcon={<CloudUploadIcon />}
                        onClick={onUploadEvent}
                        disabled={!selectedFile}
                    >
                        Upload Resume
                    </Button>
                </>
            )}
        </Box>
    );
};

export default UploadPage;
