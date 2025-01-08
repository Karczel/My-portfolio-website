import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [ownersData, setOwnersData] = useState([]); // State to store fetched data
  const [loading, setLoading] = useState(true); // State to indicate loading
  const [error, setError] = useState(null); // State to handle errors

  const endpoint = `${import.meta.env.VITE_API_URL}/owners/`;

  const fetchData = async () => {
    try {
      console.log('Fetching...');
      const response = await axios.get(endpoint);
      setOwnersData(response.data); // Update state with fetched data
    } catch (err) {
      setError(err.message); // Handle errors
    } finally {
      setLoading(false); // Stop loading indicator
    }
  };

  useEffect(() => {
    fetchData(); // Call the fetch function
  }, []); // Empty dependency array ensures it runs once

  if (loading) return <p>Loading...</p>; // Show loading state
  if (error) return <p>Error: {error}</p>; // Show error state

  return (
    <>
      <ul>
        {ownersData.results?.map((owner) => (
          <li key={owner.id}>{owner.username || 'No username'}</li>
        ))}
      </ul>
    </>
  )
}

export default App
