// MenuButton.jsx
import * as React from 'react';
import Button from '@mui/material/Button';
import TableRowsIcon from '@mui/icons-material/TableRows';
import CircleIcon from '@mui/icons-material/Circle';

export default function SectionsButton({mode, setMode, association}) {

  const toggleMode = () => {
    setMode((prevMode) => (prevMode === 'A' ? 'B' : 'A')); 
  };

  const handleButtonClick = () => {
    toggleMode();
    if (mode == 'A'){
        association(true)();
    } else {
        association(false)();
    }
  };

  // Define styles based on mode
  const buttonStyles = {
    zIndex: 1000,
    position: 'fixed',
    top: mode === 'A' ? '10px' : '100px',
    left: mode === 'A' ? '10px' : '100px',
    backgroundColor: mode === 'A' ? '#3b018c' : 'white',
    borderRadius: '50%', // Circle button
    padding: '16px', // Adjust padding to make it round
    minWidth: 'auto', // Avoid width expansion
    transition: 'top 0.3s ease, left 0.3s ease'
  };

  return (
    <Button
      style={buttonStyles}
      variant="contained"
      onClick={handleButtonClick}
    >
        <TableRowsIcon sx={{ color: mode === 'A' ? 'white' : '#3b018c'}}/>
    </Button>
  );
}
