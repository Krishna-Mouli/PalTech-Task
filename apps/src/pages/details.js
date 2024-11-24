import React from 'react';
import { useSelector } from 'react-redux';
import {
  Box,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableRow,
  Typography,
  Paper,
  Button,
} from '@mui/material';
import * as XLSX from 'xlsx';

const Details = () => {
  const details = useSelector((state) => state.details.details);
  const resume = useSelector((state) => state.resume.file);

  if (!details) {
    return (
      <Typography variant="body1" sx={{ textAlign: 'center', marginTop: 3 }}>
        No details available. Please upload a resume.
      </Typography>
    );
  }

  const detail = details[0];

  const exportToExcel = () => {
    const formattedData = Object.entries(detail).map(([key, value]) => ({
      Key: key.replace(/([A-Z])/g, ' $1'),
      Value: typeof value === 'string' ? value : JSON.stringify(value),
    }));

    const worksheet = XLSX.utils.json_to_sheet(formattedData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'ExtractedDetails'); 
    XLSX.writeFile(workbook, 'ExtractedDetails.xlsx'); 
  };

  return (
    <Box sx={{ padding: 3 }}>
      <Typography variant="h4" sx={{ marginBottom: 3, textAlign: 'center' }}>
        Extracted Details for {resume.name}
      </Typography>

      <TableContainer component={Paper}>
        <Table>
          <TableBody>          
            {Object.entries(detail).map(([key, value], index) => (
              <TableRow key={index}>
                <TableCell
                  sx={{
                    fontWeight: 'bold',
                    textTransform: 'capitalize',
                    whiteSpace: 'nowrap',
                  }}
                >
                  {key.replace(/([A-Z])/g, ' $1')}
                </TableCell>
                <TableCell>
                  {typeof value === 'string' ? value : JSON.stringify(value)}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Box sx={{ textAlign: 'center', marginTop: 3 }}>
        <Button
          variant="contained"
          onClick={exportToExcel}
          sx={{ backgroundColor: 'darkcyan', color: 'white', '&:hover': { backgroundColor: 'cyan' } }}
        >
          Download as Excel
        </Button>
      </Box>
    </Box>
  );
};

export default Details;
