import React from 'react';
import { useSelector } from 'react-redux';
import { Box, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography, Paper } from '@mui/material';

const Details = () => {
  const details = useSelector((state) => state.details.details);

  if (!details) {
    return (
      <Typography variant="body1" sx={{ textAlign: 'center', marginTop: 3 }}>
        No details available. Please upload a resume.
      </Typography>
    );
  }

  const detail = details[0]; // Assuming you're showing the first entry for now

  return (
    <Box sx={{ padding: 3 }}>
      <Typography variant="h4" sx={{ marginBottom: 3, textAlign: 'center' }}>
        Extracted Details
      </Typography>

      <TableContainer component={Paper}>
        <Table>
          <TableBody>
            {/* Map over keys and values to generate rows dynamically */}
            {Object.entries(detail).map(([key, value], index) => (
              <TableRow key={index}>
                {/* Left aligned header */}
                <TableCell
                  sx={{
                    fontWeight: 'bold',
                    textTransform: 'capitalize', // Optional: Formats keys nicely
                    whiteSpace: 'nowrap',
                  }}
                >
                  {key.replace(/([A-Z])/g, ' $1')} {/* Formats camelCase to "Camel Case" */}
                </TableCell>
                {/* Right aligned content */}
                <TableCell>
                  {typeof value === 'string' ? value : JSON.stringify(value)}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default Details;
