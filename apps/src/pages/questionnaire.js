import React from 'react';
import { useSelector } from 'react-redux';
import { Box, Typography, Table, TableBody, TableCell, TableContainer, TableRow, Paper } from '@mui/material';

const Questionnaire = () => {
  const questions = useSelector((state) => state.questionnaire.questions);
  const resume = useSelector((state) => state.resume.file);

  if (!questions) {
    return (
      <Typography variant="body1" sx={{ textAlign: 'center', marginTop: 3 }}>
        No questionnaire data available. Please upload a resume.
      </Typography>
    );
  }

  return (
    <Box sx={{ padding: 3 }}>
      <Typography variant="h4" sx={{ marginBottom: 3, textAlign: 'center' }}>
        Questionnaire for {resume.name}
      </Typography>

      <TableContainer component={Paper}>
        <Table>
          <TableBody>
            {Object.entries(questions[0]).map(([category, questionList], index) => (
              <React.Fragment key={index}>
                <TableRow>
                  <TableCell
                    colSpan={2}
                    sx={{
                      fontWeight: 'bold',
                      fontSize: '1.1rem',
                      textTransform: 'capitalize',
                      backgroundColor: '#f5f5f5',
                    }}
                  >
                    {category} Questions
                  </TableCell>
                </TableRow>                
                {Array.isArray(questionList) ? (
                  questionList.map((question, qIndex) => (
                    <TableRow key={qIndex}>
                      <TableCell sx={{ fontWeight: 'bold', width: '20%' }}>Q{qIndex + 1}</TableCell>
                      <TableCell>{question}</TableCell>
                    </TableRow>
                  ))
                ) : (
                  <TableRow>
                    <TableCell colSpan={2}>No questions available for {category}.</TableCell>
                  </TableRow>
                )}
              </React.Fragment>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default Questionnaire;

