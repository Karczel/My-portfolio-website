import React from 'react';
import Avatar from '@mui/material/Avatar';
import ProfileImage from '@/assets/default-avatar-url.svg';
import PDFViewer from './pdfViewer';

const Profile = ({ owners, skills, contacts }) => {
  return (
    <div>
      {owners.results?.map((item) => (
        <div key={item.id} style={{ 
            display: 'flex', 
            flexDirection: 'row', 
            alignItems: 'flex-start', 
            paddingTop: '30px', 
            paddingLeft: '15px',}}>
        <Avatar
            alt={item.name || item.username || 'No name'}
            src={item.profile_image || ProfileImage}
            style={{ 
                marginBottom: '10px', 
                width: '100px',  // Increase size
                height: '100px'
            }}
            />
          
          <ul style={{ padding: 20, listStyleType: 'none' }}>
            {item.first_name && item.last_name && (
              <li>{`${item.first_name} ${item.last_name}`}</li>
            )}
            {item.email && (
              <li>{item.email}</li>
            )}
            {item.quote && (
              <li>{item.quote}</li>
            )}
          </ul>
        </div>
      ))}
      {owners.results?.map((item) => (
        <div key={item.id} style={{ display: 'flex', flexDirection: 'column', marginLeft: '15px' }}>
          {item.about_me && (
            <div style={{ marginBottom: '30px' }}>
                <h2>About Me</h2>
                {item.about_me}
                </div>
          )}
          {item.requirements && (
            <div style={{ marginBottom: '30px' }}>
                <h2>Requirements</h2>
                {item.requirements.split('- ').map((line, index) => (
                <div key={index}>{line}</div>
            ))}
          </div>
          )}
          {item.resume && (
            <div style={{ marginBottom: '30px' }}>
                <h2>Resume</h2>
                <PDFViewer pdfUrl={item.resume} />
            </div>
          )}
          </div>
        ))}

        {skills.results?.map((item) => (
        <div key={item.id} style={{ display: 'flex', flexDirection: 'row', alignItems: 'flex-start' }}>
        
        </div>
      ))}

        {contacts.results?.map((item) => (
        <div key={item.id} style={{ display: 'flex', flexDirection: 'row', alignItems: 'flex-start' }}>
        
        </div>
      ))}
      {owners.results?.map((item) => (
        <div key={item.id} style={{ display: 'flex', flexDirection: 'row', alignItems: 'flex-start' }}>
        {item.location && (
            <div style={{ marginBottom: '30px' }}>
                <h2>Location</h2>
                {item.location}
                </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default Profile;
