// MenuButton.jsx
import * as React from 'react';
import Button from '@mui/material/Button';
import TableRowsIcon from '@mui/icons-material/TableRows';
import CircleIcon from '@mui/icons-material/Circle';

export default function SectionsButton({association}) {
  // Sidebar button modes
  const [mode, setMode] = React.useState('A'); 

  const toggleMode = () => {
    setMode((prevMode) => (prevMode === 'A' ? 'B' : 'A')); 
  };

  const handleButtonClick = () => {
    toggleMode();
    association(true)();
  };

  // Define styles based on mode
  const buttonStyles = {
    backgroundColor: mode === 'A' ? '#3b018c' : 'white',
    borderRadius: '50%', // Circle button
    padding: '16px', // Adjust padding to make it round
    minWidth: 'auto', // Avoid width expansion
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
