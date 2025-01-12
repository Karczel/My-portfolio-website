// Data from api
import { useState, useEffect } from 'react'
import axios from 'axios'

// components
import Avatar from '@mui/material/Avatar';

// custom components
import SectionsSidebar from "@/components/SectionsSidebar";
import SectionsButton from './components/SectionsButton';
import Profile from './components/Profile';

function App() {
  // State to store data for each endpoint
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  

  const endpoints = {
    owners: `${import.meta.env.VITE_API_URL}/owners/`,
    activities: `${import.meta.env.VITE_API_URL}/activities/`,
    contacts: `${import.meta.env.VITE_API_URL}/contacts/`,
    illustrations: `${import.meta.env.VITE_API_URL}/illustrations/`,
    pseudo_names: `${import.meta.env.VITE_API_URL}/pseudo_names/`,
    repositories: `${import.meta.env.VITE_API_URL}/repositories/`,
    skills: `${import.meta.env.VITE_API_URL}/skills/`,
    tags: `${import.meta.env.VITE_API_URL}/tags/`,
    videos: `${import.meta.env.VITE_API_URL}/videos/`,
    activity_images: `${import.meta.env.VITE_API_URL}/activity_images/`,
    repository_images: `${import.meta.env.VITE_API_URL}/repository_images/`,
    illustration_tags: `${import.meta.env.VITE_API_URL}/illustration_tags/`,
    repository_tags: `${import.meta.env.VITE_API_URL}/repository_tags/`,
    video_tags: `${import.meta.env.VITE_API_URL}/video_tags/`,
    skill_tags: `${import.meta.env.VITE_API_URL}/skill_tags/`,

  };

  const fetchData = async () => {
    try {
      const promises = Object.entries(endpoints).map(async ([key, url]) => {
        const response = await axios.get(url);
        return { key, data: response.data };
      });

      const results = await Promise.all(promises);

      // Map results into a key-value pair for the state
      const newData = results.reduce((acc, { key, data }) => {
        acc[key] = data;
        return acc;
      }, {});

      console.log(newData);
      setData(newData); // Update state with all fetched data

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
    <div>
      <>
      <SectionsSidebar/>
      </>
      <>
      <div
  style={{
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    overflow: 'auto',
    maxHeight: '100vh',
    width: '60vw',
    maxWidth: '90vw',
    padding: '20rem',
    boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.5)',
  }}>
    <div>
      <Profile owners={data.owners} skills={data.skills} tags={data.tags} skillTags={data.skill_tags} contacts={data.contacts}/>
      {/* Software Projects */}
    </div>

    {/* Data query test */}
      {Object.entries(data).map(([key, value]) => (
        <div key={key}>
          <h2>{key.charAt(0).toUpperCase() + key.slice(1)}</h2>
          <ul>
            {value.results?.map((item) => (
              <li key={item.id}>{item.name || item.username || 'No data'}</li>
            ))}
          </ul>
        </div>
      ))}
      </div>
      </>
    </div>
  );
}

export default App
