import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {

  const [productsData, setProductsData] = useState([])

  const endpoint = `${import.meta.env.VITE_API_URL}/owners/`

  const fetchData = async() => {
    console.log('fetching...')
    const response = await axios.get(endpoint)
    const {data} = response
    console.log(data)
    return data
  }

  useEffect(() => {
    setProductsData(fetchData())
  }, [])

  return (
    <>
    <ul>
        {productsData.map(el => (
          <li key={el.id}>{el.username || 'No username'}</li>
        ))}
    </ul>
    </>
  )
}

export default App
