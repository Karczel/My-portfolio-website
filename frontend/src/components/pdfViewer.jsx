import React from 'react';

const PDFViewer = ({ pdfUrl }) => {
    return (
        <div>
          <iframe
            src={pdfUrl}
            width="100%"
            height="600px"
            style={{ border: 'none' }}
            title="PDF Viewer"
          ></iframe>
        </div>
      );
};

export default PDFViewer;
